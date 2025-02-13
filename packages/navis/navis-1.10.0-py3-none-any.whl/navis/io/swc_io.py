#    This script is part of navis (http://www.github.com/navis-org/navis).
#    Copyright (C) 2018 Philipp Schlegel
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

import csv
import datetime
import io
import json

import pandas as pd

from pathlib import Path
from textwrap import dedent
from typing import List, Union, Iterable, Dict, Optional, Any, TextIO, IO
from urllib3 import HTTPResponse

from .. import config, utils, core
from . import base

__all__ = ["SwcReader", "read_swc", "write_swc"]

# Set up logging
logger = config.get_logger(__name__)

NODE_COLUMNS = ("node_id", "label", "x", "y", "z", "radius", "parent_id")
COMMENT = "#"
DEFAULT_DELIMITER = " "
DEFAULT_PRECISION = 32
DEFAULT_FMT = "{name}.swc"
NA_VALUES = [None, "None"]


class SwcReader(base.BaseReader):
    def __init__(
        self,
        connector_labels: Optional[Dict[str, Union[str, int]]] = None,
        soma_label: Union[str, int] = 1,
        delimiter: str = DEFAULT_DELIMITER,
        precision: int = DEFAULT_PRECISION,
        read_meta: bool = False,
        fmt: str = DEFAULT_FMT,
        errors: str = "raise",
        attrs: Optional[Dict[str, Any]] = None,
    ):
        if not fmt.endswith(".swc"):
            raise ValueError('`fmt` must end with ".swc"')

        super().__init__(
            fmt=fmt, attrs=attrs, file_ext=".swc", errors=errors, name_fallback="SWC"
        )
        self.connector_labels = connector_labels or dict()
        self.soma_label = soma_label
        self.delimiter = delimiter
        self.read_meta = read_meta

        int_, float_ = base.parse_precision(precision)
        self._dtypes = {
            "node_id": int_,
            "parent_id": int_,
            "label": "category",
            "x": float_,
            "y": float_,
            "z": float_,
            "radius": float_,
        }

    @base.handle_errors
    def read_buffer(
        self, f: IO, attrs: Optional[Dict[str, Any]] = None
    ) -> "core.TreeNeuron":
        """Read buffer into a TreeNeuron.

        Parameters
        ----------
        f :         IO
                    Readable buffer (if bytes, interpreted as utf-8).
        attrs :     dict | None
                    Arbitrary attributes to include in the TreeNeuron.

        Returns
        -------
        core.TreeNeuron
        """
        if isinstance(f, HTTPResponse):
            f = io.StringIO(f.data.decode())

        if isinstance(f.read(0), bytes):
            f = io.TextIOWrapper(f, encoding="utf-8")

        header_rows = read_header_rows(f)
        try:
            nodes = pd.read_csv(
                f,
                delimiter=self.delimiter,
                skipinitialspace=True,
                skiprows=len(header_rows),
                comment=COMMENT,
                header=None,
                na_values=NA_VALUES,
            )
            if len(nodes.columns) < len(NODE_COLUMNS):
                raise ValueError("Not enough columns in SWC file.")
            elif len(nodes.columns) > len(NODE_COLUMNS):
                logger.warning(
                    f"Found {len(nodes.columns)} instead of the expected 7 "
                    "columns in SWC file. Assuming additional columns are "
                    "custom properties. You can silence this warning by setting "
                    "`navis.set_loggers('ERROR')`."
                )
                nodes.columns = (
                    list(NODE_COLUMNS) + nodes.columns[len(NODE_COLUMNS) :].tolist()
                )
            else:
                nodes.columns = NODE_COLUMNS
        except pd.errors.EmptyDataError:
            # If file is totally empty, return an empty neuron
            # Note that the TreeNeuron will still complain but it's a better
            # error message
            nodes = pd.DataFrame(columns=NODE_COLUMNS)

        # Check for row with JSON-formatted meta data
        # Expected format '# Meta: {"id": "12345"}'
        if self.read_meta:
            meta_row = [r for r in header_rows if r.lower().startswith("# meta:")]
            if meta_row:
                meta_data = json.loads(meta_row[0][7:].strip())
                attrs = base.merge_dicts(meta_data, attrs)

        return self.read_dataframe(
            nodes, base.merge_dicts({"swc_header": "\n".join(header_rows)}, attrs)
        )

    @base.handle_errors
    def read_dataframe(
        self, nodes: pd.DataFrame, attrs: Optional[Dict[str, Any]] = None
    ) -> "core.TreeNeuron":
        """Convert a SWC-like DataFrame into a TreeNeuron.

        Parameters
        ----------
        nodes :     pandas.DataFrame
        attrs :     dict or None
                    Arbitrary attributes to include in the TreeNeuron.

        Returns
        -------
        core.TreeNeuron
        """
        n = core.TreeNeuron(
            sanitise_nodes(nodes.astype(self._dtypes, errors="ignore", copy=False)),
            connectors=self._extract_connectors(nodes),
        )

        if self.soma_label is not None:
            is_soma_node = n.nodes.label.values == self.soma_label
            if any(is_soma_node):
                n.soma = n.nodes.node_id.values[is_soma_node][0]

        attrs = self._make_attributes({"name": "SWC", "origin": "DataFrame"}, attrs)

        # SWC is special - we do not want to register it
        n.swc_header = attrs.pop("swc_header", "")

        # Try adding properties one-by-one. If one fails, we'll keep track of it
        # in the `.meta` attribute
        meta = {}
        for k, v in attrs.items():
            try:
                n._register_attr(k, v)
            except (AttributeError, ValueError, TypeError):
                meta[k] = v

        if meta:
            n.meta = meta

        return n

    def _extract_connectors(self, nodes: pd.DataFrame) -> Optional[pd.DataFrame]:
        """Infer outgoing/incoming connectors from node labels.

        Parameters
        ----------
        nodes :     pd.DataFrame

        Returns
        -------
        Optional[pd.DataFrame]
                    With columns `["node_id", "x", "y", "z", "connector_id", "type"]`
        """
        if not self.connector_labels:
            return None

        to_concat = [
            pd.DataFrame([], columns=["node_id", "connector_id", "type", "x", "y", "z"])
        ]
        for name, val in self.connector_labels.items():
            cn = nodes[nodes.label == val][["node_id", "x", "y", "z"]].copy()
            cn["connector_id"] = None
            cn["type"] = name
            to_concat.append(cn)

        return pd.concat(to_concat, axis=0)


def sanitise_nodes(nodes: pd.DataFrame, allow_empty=True) -> pd.DataFrame:
    """Check that nodes dataframe is non-empty and is not missing any data.

    Parameters
    ----------
    nodes : pandas.DataFrame

    Returns
    -------
    pandas.DataFrame
    """
    if not allow_empty and nodes.empty:
        raise ValueError("No data found in SWC.")

    is_na = nodes[["node_id", "parent_id", "x", "y", "z"]].isna().any(axis=1)

    if is_na.any():
        # Remove nodes with missing data
        nodes = nodes.loc[~is_na.any(axis=1)]

        # Because we removed nodes, we'll have to run a more complicated root
        # detection
        nodes.loc[~nodes.parent_id.isin(nodes.node_id), "parent_id"] = -1

    return nodes


def read_header_rows(f: TextIO):
    f"""Read {COMMENT}-prefixed lines from the start of a buffer,
    then seek back to the start of the buffer.

    Parameters
    ----------
    f : io.TextIO

    Returns
    -------
    list : List of strings
    """
    out = []
    for line in f:
        if not line.startswith(COMMENT):
            break
        out.append(line)

    f.seek(0)
    return out


def read_swc(
    f: Union[str, pd.DataFrame, Iterable],
    connector_labels: Optional[Dict[str, Union[str, int]]] = {},
    soma_label: Union[str, int] = 1,
    include_subdirs: bool = False,
    delimiter: str = " ",
    parallel: Union[bool, int] = "auto",
    precision: int = 32,
    fmt: str = "{name}.swc",
    read_meta: bool = True,
    limit: Optional[int] = None,
    errors: str = "raise",
    **kwargs,
) -> "core.NeuronObject":
    """Create Neuron/List from SWC file.

    This import is following format specified
    [here](http://www.neuronland.org/NLMorphologyConverter/MorphologyFormats/SWC/Spec.html).

    Parameters
    ----------
    f :                 str | pandas.DataFrame | list thereof
                        Filename, folder, SWC string, URL or DataFrame:
                         - if folder, will import all `.swc` files
                         - if a `.zip`, `.tar` or `.tar.gz` archive will read all
                           SWC files from the file
                         - if a URL (http:// or https://), will download the
                           file and import it
                         - FTP address (ftp://) can point to a folder or a single
                           file
                         - DataFrames are interpreted as a SWC tables
                        See also `limit` parameter to read only a subset of files.
    connector_labels :  dict, optional
                        If provided will extract connectors from SWC.
                        Dictionary must map types to labels:
                        `{'presynapse': 7, 'postsynapse': 8}`
    include_subdirs :   bool, optional
                        If True and `f` is a folder, will also search
                        subdirectories for `.swc` files.
    delimiter :         str
                        Delimiter to use. Passed to `pandas.read_csv`.
    parallel :          "auto" | bool | int
                        Whether to use parallel processes for reading:
                         - "auto" (default): will use parallel processing if
                            more than 200 SWCs are imported.
                          - Integers will be interpreted as the number of
                            processes to use. Defaults to `os.cpu_count() // 2`.
                          - False will use a single process.
                        Ignored for tar archives. Please note that spawning
                        processes incurs an overhead and might not be faster
                        for small numbers of files.
    precision :         int [8, 16, 32, 64] | None
                        Precision for data. Defaults to 32 bit integers/floats.
                        If `None` will let pandas infer data types - this
                        typically leads to higher than necessary precision.
    fmt :               str
                        Formatter to specify how filenames are parsed into
                        neuron attributes. Some illustrative examples:

                          - `{name}.swc` (default) uses the filename
                            (minus the suffix) as the neuron's name property
                          - `{id}.swc` uses the filename as the neuron's ID
                            property
                          - `{name,id}.swc` uses the filename as the neuron's
                            name and ID properties
                          - `{name}.{id}.swc` splits the filename at a "."
                            and uses the first part as name and the second as ID
                          - `{name,id:int}.swc` same as above but converts
                            into integer for the ID
                          - `{name}_{myproperty}.swc` splits the filename at
                            "_" and uses the first part as name and as a
                            generic "myproperty" property
                          - `{name}_{}_{id}.swc` splits the filename at
                            "_" and uses the first part as name and the last as
                            ID. The middle part is ignored.

                        Throws a ValueError if pattern can't be found in
                        filename. Ignored for DataFrames.
    read_meta :         bool
                        If True and SWC header contains a line with JSON-encoded
                        meta data e.g. (`# Meta: {'id': 123}`), these data
                        will be read as neuron properties. `fmt` still takes
                        precedence. Will try to assign meta data directly as
                        neuron attribute (e.g. `neuron.id`). Failing that
                        (can happen for properties intrinsic to `TreeNeurons`),
                        will add a `.meta` dictionary to the neuron.
    limit :             int | str | slice | list, optional
                        When reading from a folder or archive you can use this parameter to
                        restrict the which files read:
                         - if an integer, will read only the first `limit` SWC files
                          (useful to get a sample from a large library of skeletons)
                         - if a string, will interpret it as filename (regex) pattern
                           and only read files that match the pattern; e.g. `limit='.*_R.*'`
                           will only read files that contain `_R` in their filename
                         - if a slice (e.g. `slice(10, 20)`) will read only the files in
                           that range
                         - a list is expected to be a list of filenames to read from
                           the folder/archive
    errors :            "raise" | "log" | "ignore"
                        If "log" or "ignore", errors will not be raised and the
                        mesh will be skipped. Can result in empty output.
    **kwargs
                        Keyword arguments passed to the construction of
                        `navis.TreeNeuron`. You can use this to e.g. set
                        meta data.

    Returns
    -------
    navis.TreeNeuron
                        Contains SWC file header as `.swc_header` attribute.
    navis.NeuronList
                        If import of multiple SWCs will return NeuronList of
                        TreeNeurons.

    See Also
    --------
    [`navis.write_swc`][]
                        Export neurons as SWC files.

    Examples
    --------

    Read a single file:

    >>> s = navis.read_swc('skeleton.swc')                      # doctest: +SKIP

    Read all .swc files in a directory:

    >>> s = navis.read_swc('/some/directory/')                  # doctest: +SKIP

    Read all .swc files in a zip archive:

    >>> s = navis.read_swc('skeletons.zip')                     # doctest: +SKIP

    Sample the first 100 SWC files in a zip archive:

    >>> s = navis.read_swc('skeletons.zip', limit=100)          # doctest: +SKIP

    Read first all SWC files an ftp folder:

    >>> s = navis.read_swc('ftp://server:port/path/to/swc/')    # doctest: +SKIP

    """
    # SwcReader will try its best to read whatever you throw at it - with limited
    # sanity checks. For example: if you misspell a filepath, it will assume
    # that it's a SWC string (because anything that's a string but doesn't
    # point to an existing file or a folder MUST be a SWC) which will lead to
    # strange error messages.
    # The easiest fix is to implement a small sanity check here:
    if isinstance(f, str) and "\n" not in f and not utils.is_url(f):
        # If this looks like a path
        p = Path(f).expanduser()
        if not p.is_dir() and not p.is_file():
            raise FileNotFoundError(
                f'"{f}" looks like a directory or filepath '
                "but does not appear to exist."
            )

    reader = SwcReader(
        connector_labels=connector_labels,
        soma_label=soma_label,
        delimiter=delimiter,
        precision=precision,
        read_meta=read_meta,
        fmt=fmt,
        errors=errors,
        attrs=kwargs,
    )
    res = reader.read_any(f, include_subdirs, parallel, limit=limit)

    failed = []
    for n in core.NeuronList(res):
        if not hasattr(n, "meta"):
            continue
        failed += list(n.meta.keys())

    if failed:
        failed = list(set(failed))
        logger.warning(
            "Some meta data could not be directly attached to the "
            "neuron(s) - probably some clash with intrinsic "
            "properties. You can find these data attached as "
            "`.meta` dictionary."
        )

    return res


def write_swc(
    x: "core.NeuronObject",
    filepath: Union[str, Path],
    header: Optional[str] = None,
    write_meta: Union[bool, List[str], dict] = True,
    labels: Union[str, dict, bool] = True,
    export_connectors: bool = False,
    return_node_map: bool = False,
) -> None:
    """Write TreeNeuron(s) to SWC.

    Follows the format specified
    [here](http://www.neuronland.org/NLMorphologyConverter/MorphologyFormats/SWC/Spec.html).

    Parameters
    ----------
    x :                 TreeNeuron | NeuronList
                        If multiple neurons, will generate a single SWC file
                        for each neuron (see also `filepath`).
    filepath :          str | pathlib.Path | list thereof
                        Destination for the SWC files. See examples for options.
                        If `x` is multiple neurons, `filepath` must either
                        be a folder, a "formattable" filename, a filename ending
                        in `.zip` or a list of filenames (one for each neuron
                        in `x`). Existing files will be overwritten!
    header :            str | None, optional
                        Header for SWC file. If not provided, will use generic
                        header.
    write_meta :        bool | list | dict
                        If not False, will add meta data as JSON-formatted
                        string to the header::

                           True: adds neuron `id`, `name` and `units`
                           list: use to set which properties, e.g. ['id', 'units']
                           dict: use to set meta data, e.g. {'template': 'JRC2018F'}

                        This parameter is ignored if custom header is provided.
    labels :            str | dict | bool, optional
                        Node labels. Can be::

                            str : column name in node table
                            dict: must be of format {node_id: 'label', ...}.
                            bool: if True, will generate automatic labels, if False all nodes have label "0".

    export_connectors : bool, optional
                        If True, will label nodes with pre- ("7") and
                        postsynapse ("8"). Because only one label can be given
                        this might drop synapses (i.e. in case of multiple
                        pre- and/or postsynapses on a single node)! `labels`
                        must be `True` for this to have any effect.
    return_node_map :   bool
                        If True, will return a dictionary mapping the old node
                        ID to the new reindexed node IDs in the file.

    Returns
    -------
    node_map :          dict
                        Only if `return_node_map=True`.

    See Also
    --------
    [`navis.read_swc`][]
                        Import skeleton from SWC files.

    Examples
    --------
    Save a single neuron to a specific file:

    >>> import navis
    >>> n = navis.example_neurons(1, kind='skeleton')
    >>> navis.write_swc(n, tmp_dir / 'my_neuron.swc')

    Save two neurons to specific files:

    >>> import navis
    >>> nl = navis.example_neurons(2, kind='skeleton')
    >>> navis.write_swc(nl, [tmp_dir / 'my_neuron1.swc', tmp_dir / 'my_neuron2.swc'])

    Save multiple neurons to a folder (must exist). Filenames will be
    autogenerated as "{neuron.id}.swc":

    >>> import navis
    >>> nl = navis.example_neurons(5, kind='skeleton')
    >>> navis.write_swc(nl, tmp_dir)

    Save multiple neurons to a folder but modify the pattern for the
    autogenerated filenames:

    >>> import navis
    >>> nl = navis.example_neurons(5, kind='skeleton')
    >>> navis.write_swc(nl, tmp_dir / 'skel-{neuron.name}.swc')

    Save multiple neurons to a zip file:

    >>> import navis
    >>> nl = navis.example_neurons(5, kind='skeleton')
    >>> navis.write_swc(nl, tmp_dir / 'neuronlist.zip')

    Save multiple neurons to a zip file but modify the filenames:

    >>> import navis
    >>> nl = navis.example_neurons(5, kind='skeleton')
    >>> navis.write_swc(nl, tmp_dir / 'skel-{neuron.name}.swc@neuronlist.zip')

    """
    # Make sure inputs are only TreeNeurons
    if isinstance(x, core.NeuronList):
        for n in x:
            if not isinstance(n, core.TreeNeuron):
                msg = f'Can only write TreeNeurons to SWC, not "{type(n)}"'
                if isinstance(n, core.Dotprops):
                    msg += (
                        ". For Dotprops, you can use either `navis.write_nrrd`"
                        " or `navis.write_parquet`."
                    )
                raise TypeError(msg)
    elif not isinstance(x, core.TreeNeuron):
        msg = f'Can only write TreeNeurons to SWC, not "{type(n)}"'
        if isinstance(n, core.Dotprops):
            msg += (
                ". For Dotprops, you can use either `navis.write_nrrd`"
                " or `navis.write_parquet`."
            )
        raise TypeError(msg)

    writer = base.Writer(write_func=_write_swc, ext=".swc")

    return writer.write_any(
        x,
        filepath=filepath,
        header=header,
        write_meta=write_meta,
        labels=labels,
        export_connectors=export_connectors,
        return_node_map=return_node_map,
    )


def _write_swc(
    x: Union["core.TreeNeuron", "core.Dotprops"],
    filepath: Union[str, Path],
    header: Optional[str] = None,
    write_meta: Union[bool, List[str], dict] = True,
    labels: Union[str, dict, bool] = True,
    export_connectors: bool = False,
    return_node_map: bool = False,
) -> None:
    """Write single TreeNeuron to file."""
    # Generate SWC table
    res = make_swc_table(
        x,
        labels=labels,
        export_connectors=export_connectors,
        return_node_map=return_node_map,
    )

    if return_node_map:
        swc, node_map = res[0], res[1]
    else:
        swc = res

    # Generate header if not provided
    if not isinstance(header, str):
        header = dedent(f"""\
        # SWC format file
        # based on specifications at http://www.neuronland.org/NLMorphologyConverter/MorphologyFormats/SWC/Spec.html
        # Created on {datetime.date.today()} using navis (https://github.com/navis-org/navis)
        """)
        if write_meta:
            if isinstance(write_meta, str):
                props = {write_meta: str(getattr(x, write_meta, None))}
            elif isinstance(write_meta, dict):
                props = write_meta
            elif isinstance(write_meta, list):
                props = {k: str(getattr(x, k, None)) for k in write_meta}
            else:
                props = {k: str(getattr(x, k, None)) for k in ["id", "name", "units"]}
            header += f"# Meta: {json.dumps(props)}\n"
        header += dedent("""\
        # PointNo Label X Y Z Radius Parent
        # Labels:
        # 0 = undefined, 1 = soma, 5 = fork point, 6 = end point
        """)
        if export_connectors:
            header += dedent("""\
            # 7 = presynapses, 8 = postsynapses
            """)
    elif not header.endswith("\n"):
        header += "\n"

    with open(filepath, "w") as file:
        # Write header
        file.write(header)

        # Write data
        writer = csv.writer(file, delimiter=" ")
        writer.writerows(swc.astype(str).values)

    if return_node_map:
        return node_map


def make_swc_table(
    x: Union["core.TreeNeuron", "core.Dotprops"],
    labels: Union[str, dict, bool] = None,
    export_connectors: bool = False,
    return_node_map: bool = False,
) -> pd.DataFrame:
    """Generate a node table compliant with the SWC format.

    Follows the format specified
    [here](http://www.neuronland.org/NLMorphologyConverter/MorphologyFormats/SWC/Spec.html).

    Parameters
    ----------
    x :                 TreeNeuron | Dotprops
                        Dotprops will be turned from points + vectors to
                        individual segments.
    labels :            str | dict | bool, optional
                        Node labels. Can be::

                        str : column name in node table
                        dict: must be of format {node_id: 'label', ...}.
                        bool: if True, will generate automatic labels, if False all nodes have label "0".

    export_connectors : bool, optional
                        If True, will label nodes with pre- ("7") and
                        postsynapse ("8"). Because only one label can be given
                        this might drop synapses (i.e. in case of multiple
                        pre- or postsynapses on a single node)! `labels`
                        must be `True` for this to have any effect.
    return_node_map :   bool
                        If True, will return a dictionary mapping the old node
                        ID to the new reindexed node IDs in the file.

    Returns
    -------
    SWC table :         pandas.DataFrame
    node map :          dict
                        Only if `return_node_map=True`.

    """
    if isinstance(x, core.Dotprops):
        x = x.to_skeleton()

    # Work on a copy
    swc = x.nodes.copy()

    # Add labels
    swc["label"] = 0
    if isinstance(labels, dict):
        swc["label"] = swc.index.map(labels)
    elif isinstance(labels, str):
        swc["label"] = swc[labels]
    elif labels:
        # Add end/branch labels
        swc.loc[swc.type == "branch", "label"] = 5
        swc.loc[swc.type == "end", "label"] = 6
        # Add soma label
        if not isinstance(x.soma, type(None)):
            soma = utils.make_iterable(x.soma)
            swc.loc[swc.node_id.isin(soma), "label"] = 1
        if export_connectors:
            # Add synapse label
            pre_ids = x.presynapses.node_id.values
            post_ids = x.postsynapses.node_id.values
            swc.loc[swc.node_id.isin(pre_ids), "label"] = 7
            swc.loc[swc.node_id.isin(post_ids), "label"] = 8

    # Sort such that the parent is always before the child
    swc.sort_values("parent_id", ascending=True, inplace=True)

    # Reset index
    swc.reset_index(drop=True, inplace=True)

    # Generate mapping
    new_ids = dict(zip(swc.node_id.values, swc.index.values + 1))

    swc["node_id"] = swc.node_id.map(new_ids)
    # Lambda prevents potential issue with missing parents
    swc["parent_id"] = swc.parent_id.map(lambda x: new_ids.get(x, -1))

    # Get things in order
    swc = swc[["node_id", "label", "x", "y", "z", "radius", "parent_id"]]

    # Make sure radius has no `None`
    swc["radius"] = swc.radius.fillna(0)

    # Adjust column titles
    swc.columns = ["PointNo", "Label", "X", "Y", "Z", "Radius", "Parent"]

    if return_node_map:
        return swc, new_ids

    return swc
