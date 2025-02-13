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

"""This module contains functions for intersections."""

import pandas as pd
import numpy as np

from typing import Union, List, Dict, Sequence, Optional, overload, Any
from typing_extensions import Literal

from .. import config, core, utils, morpho

from .ray import *
from .convex import *

# Set up logging -> has to be before try statement!
logger = config.get_logger(__name__)

try:
    from pyoctree import pyoctree
except ModuleNotFoundError:
    pyoctree = None
    logger.debug("Package pyoctree not found.")

try:
    import ncollpyde
except ModuleNotFoundError:
    ncollpyde = None
    logger.debug("Package ncollpyde not found.")


__all__ = sorted(['in_volume', 'intersection_matrix'])

Modes = Union[Literal['IN'], Literal['OUT']]

Backends = Union[Literal['ncollpyde'],
                 Literal['pyoctree'],
                 Literal['scipy'],
                 Sequence[Union[Literal['ncollpyde'],
                                Literal['pyoctree'],
                                Literal['scipy']]]
                 ]

@overload
def in_volume(x: 'core.TreeNeuron',
              volume: core.Volume,
              inplace: bool = False,
              mode: Modes = 'IN',
              backend: Backends = ('ncollpyde', 'pyoctree'),
              n_rays: Optional[int] = None,
              prevent_fragments: bool = False) -> 'core.TreeNeuron': ...


@overload
def in_volume(x: 'core.NeuronList',
              volume: core.Volume,
              inplace: bool = False,
              mode: Modes = 'IN',
              backend: Backends = ('ncollpyde', 'pyoctree'),
              n_rays: Optional[int] = None,
              prevent_fragments: bool = False) -> 'core.NeuronList': ...


@overload
def in_volume(x: Union[Sequence, pd.DataFrame],
              volume: core.Volume,
              inplace: bool = False,
              mode: Modes = 'IN',
              backend: Backends = ('ncollpyde', 'pyoctree'),
              n_rays: Optional[int] = None,
              prevent_fragments: bool = False) -> Sequence[bool]: ...


@overload
def in_volume(x: Union['core.NeuronObject', Sequence, pd.DataFrame],
              volume: Union[Dict[str, core.Volume],
                            Sequence[core.Volume]],
              inplace: bool = False,
              mode: Modes = 'IN',
              backend: Backends = ('ncollpyde', 'pyoctree'),
              n_rays: Optional[int] = None,
              prevent_fragments: bool = False) -> Dict[str,
                                                       Union[Sequence[bool],
                                                             'core.NeuronObject']]: ...


# We do need the full signature b/c we're recursively calling in_volume
# which means that there is uncertainty
@overload
def in_volume(x: Union['core.NeuronObject', Sequence, pd.DataFrame],
              volume: Union[core.Volume,
                            Dict[str, core.Volume],
                            Sequence[core.Volume]],
              inplace: bool = False,
              mode: Modes = 'IN',
              backend: Backends = ('ncollpyde', 'pyoctree'),
              n_rays: Optional[int] = None,
              prevent_fragments: bool = False) -> Optional[Union['core.NeuronObject',
                                                                 Sequence[bool],
                                                                 Dict[str, Union[Sequence[bool],
                                                                                 'core.NeuronObject']]
                                                                 ]]: ...


def in_volume(x: Union['core.NeuronObject', Sequence, pd.DataFrame],
              volume: Union[core.Volume,
                            Dict[str, core.Volume],
                            Sequence[core.Volume]],
              mode: Modes = 'IN',
              backend: Backends = ('ncollpyde', 'pyoctree'),
              n_rays: Optional[int] = None,
              prevent_fragments: bool = False,
              validate: bool = False,
              inplace: bool = False,) -> Optional[Union['core.NeuronObject',
                                                        Sequence[bool],
                                                        Dict[str, Union[Sequence[bool],
                                                                        'core.NeuronObject']]
                                                        ]]:
    """Test if points/neurons are within a given volume.

    Notes
    -----
    This function requires [ncollpyde](https://github.com/clbarnes/ncollpyde)
    (recommended and installed with `navis`) or
    [pyoctree](https://github.com/mhogg/pyoctree) as backends for raycasting.
    If neither is installed, we can fall back to using scipy's ConvexHull
    instead. This is, however, slower and will give wrong positives for concave
    meshes!

    Parameters
    ----------
    x :                 (N, 3) array-like | pandas.DataFrame | Neuron/List
                        Object(s) to intersect with the volume.
                         - Neuron(s) will be subset to parts within the volume
                         - Array-like is treated as list of x/y/z coordinates;
                           has to be of shape `(N, 3)`
                         - `pandas.DataFrame` needs to have `x, y, z`
                           columns

    volume :            Volume | mesh-like | dict or list thereof
                        Multiple volumes can be given as list
                        (`[volume1, volume2, ...]`) or dict
                        (`{'label1': volume1, ...}`).
    mode :              'IN' | 'OUT', optional
                        If 'IN', parts of the neuron that are within the volume
                        are kept.
    backend :           'ncollpyde' | 'pyoctree' | 'scipy' | iterable thereof
                        Which backend so be used (see Notes). If multiple
                        backends are given, will use the first backend that is
                        available.
    n_rays :            int | None, optional
                        Number of rays used to determine if a point is inside
                        a volume. More rays give more reliable results but are
                        slower (especially with pyoctree backend). If `None`
                        will use default number of rays (3 for ncollpyde, 1 for
                        pyoctree).
    prevent_fragments : bool, optional
                        Only relevant if input is TreeNeuron(s). If True, will
                        attempt to keep neuron from fragmenting.
    validate :          bool, optional
                        If True, validate `volume` and try to fix issues using
                        trimesh. Will raise ValueError if issue could not be
                        fixed.
    inplace :           bool, optional
                        Only relevant if input is Neuron/List. Ignored
                        if multiple volumes are provided.

    Returns
    -------
    Neuron
                      If input is a single neuron or NeuronList, will return
                      subset of the neuron(s) (nodes and connectors) that are
                      within given volume.
    list of bools
                      If input is `(N, 3)` array of coordinates, returns a `(N, )`
                      boolean array: `True` if in volume, `False` if not in
                      order.
    dict
                      If multiple volumes are provided, results will be
                      returned in dictionary with volumes as keys::

                        {'volume1': in_volume(x, volume1),
                         'volume2': in_volume(x, volume2),
                         ... }

    Examples
    --------
    Prune neuron to volume

    >>> import navis
    >>> n = navis.example_neurons(1)
    >>> lh = navis.example_volume('LH')
    >>> n_lh = navis.in_volume(n, lh, inplace=False)
    >>> n_lh                                                    # doctest: +SKIP
    type            navis.TreeNeuron
    name                  1734350788
    id                    1734350788
    n_nodes                      344
    n_connectors                None
    n_branches                    49
    n_leafs                       50
    cable_length             32313.5
    soma                        None
    units                8 nanometer
    dtype: object

    Find out which points are inside a volume

    >>> in_v = navis.in_volume(n.nodes[['x', 'y', 'z']].values, lh)
    >>> in_v
    array([False, False, False, ..., False, False, False])
    >>> in_v.sum()
    344

    """
    allowed_backends = ('ncollpyde', 'pyoctree', 'scipy')

    if not utils.is_iterable(backend):
        backend = [backend]

    if any(set(backend) - set(allowed_backends)):
        raise ValueError(f'Unknown backend in "{backend}". Allowed backends: '
                         f'{allowed_backends}')

    if mode not in ('IN', 'OUT'):
        raise ValueError(f'`mode` must be "IN" or "OUT", not "{mode}"')

    # If we are given multiple volumes
    if isinstance(volume, (list, dict, np.ndarray)):
        # Force into dict
        if not isinstance(volume, dict):
            # Make sure all Volumes can be uniquely indexed
            vnames = [getattr(v, 'name', i) for i, v in enumerate(volume)]
            dupli = [str(v) for v in set(vnames) if vnames.count(v) > 1]
            if dupli:
                raise ValueError('Duplicate Volume names detected: '
                                 f'{", ".join(dupli)}. Volume.name must be '
                                 'unique.')

            volume = {getattr(v, 'name', i): v for i, v in enumerate(volume)}

        # Make sure everything is a volume
        volume = {k: utils.make_volume(v) for k, v in volume.items()}

        # Validate now - this might safe us troubles later
        if validate:
            for v in volume.values():
                msg = 'Mesh is not a volume ' \
                      '(e.g. not watertight, incorrect ' \
                      'winding) and could not be fixed. ' \
                      'Use `validate=False` to skip validation and ' \
                      'perform intersection regardless.'
                try:
                    v.validate()
                except utils.VolumeError as e:
                    raise utils.VolumeError(f'{v}: {msg}') from e
                except BaseException:
                    raise

        data: Dict[str, Any] = dict()
        for v in config.tqdm(volume, desc='Volumes', disable=config.pbar_hide,
                             leave=config.pbar_leave):
            data[v] = in_volume(x,
                                volume=volume[v],
                                inplace=False,
                                n_rays=n_rays,
                                mode=mode,
                                validate=False,
                                backend=backend)
        return data

    # Coerce volume into navis.Volume
    volume = utils.make_volume(volume)

    if not isinstance(volume, core.Volume):
        raise TypeError(f'Expected navis.Volume, got "{type(volume)}"')

    # From here on out volume is a single core.Volume
    vol: 'core.Volume' = volume  # type: ignore

    if validate:
        msg = 'Mesh is not a volume ' \
              '(e.g. not watertight, incorrect ' \
              'winding) and could not be fixed. ' \
              'Use `validate=False` to skip validation and ' \
              'perform intersection regardless.'
        try:
            vol.validate()
        except utils.VolumeError as e:
            raise utils.VolumeError(f'{vol}: {msg}') from e
        except BaseException:
            raise

    # Make copy if necessary
    if isinstance(x, (core.NeuronList, core.BaseNeuron)):
        if inplace is False:
            x = x.copy()

    if isinstance(x, (core.BaseNeuron)):
        if isinstance(x, core.TreeNeuron):
            data = x.nodes[['x', 'y', 'z']].values
        elif isinstance(x, core.Dotprops):
            data = x.points
        elif isinstance(x, core.MeshNeuron):
            data = x.vertices
        elif isinstance(x, core.VoxelNeuron):
            data = x.voxels * x.units_xyz.magnitude + x.units_xyz.magnitude / 2
            data += x.offset

        in_v = in_volume(data,
                         vol,
                         mode='IN',
                         n_rays=n_rays,
                         validate=False,
                         backend=backend)

        # If mode is OUT, invert selection
        if mode == 'OUT':
            in_v = ~np.array(in_v)

        # Only subset if there are actually nodes to remove
        if not all(in_v):
            if isinstance(x, core.TreeNeuron):
                _ = morpho.subset_neuron(x,
                                         subset=x.nodes[in_v].node_id.values,
                                         inplace=True,
                                         prevent_fragments=prevent_fragments)
            elif isinstance(x, (core.MeshNeuron, core.Dotprops)):
                _ = morpho.subset_neuron(x,
                                         subset=in_v,
                                         inplace=True,
                                         prevent_fragments=prevent_fragments)
            elif isinstance(x, core.VoxelNeuron):
                values = x.values[in_v]
                x._data = x.voxels[in_v]
                x.values = values
                x._clear_temp_attr()

        return x
    elif isinstance(x, core.NeuronList):
        for n in config.tqdm(x, desc='Subsetting',
                             leave=config.pbar_leave,
                             disable=config.pbar_hide):
            in_volume(n, vol, inplace=True, mode=mode, backend=backend,
                      validate=False, n_rays=n_rays,
                      prevent_fragments=prevent_fragments)

        return x
    elif isinstance(x, pd.DataFrame):
        points = x[['x', 'y', 'z']].values
    elif isinstance(x, np.ndarray):
        points = x
    elif isinstance(x, (list, tuple)):
        points = np.array(x)

    if points.ndim != 2 or points.shape[1] != 3:  # type: ignore  # does not know about numpy
        raise ValueError('Points must be array of shape (N,3).')

    for b in backend:
        if b == 'ncollpyde' and ncollpyde:
            return in_volume_ncoll(points, vol,
                                   n_rays=n_rays)
        elif b == 'pyoctree' and pyoctree:
            return in_volume_pyoc(points, vol,
                                  n_rays=n_rays)
        elif b == 'scipy':
            return in_volume_convex(points, vol, approximate=False)

    raise ValueError(f'None of the specified backends were available: {backend}')


def intersection_matrix(x: 'core.NeuronObject',
                        volumes: Union[List[core.Volume],
                                       Dict[str, core.Volume]],
                        attr: Optional[str] = None,
                        **kwargs
                        ) -> pd.DataFrame:
    """Compute intersection matrix between a set of neurons and volumes.

    Parameters
    ----------
    x :               NeuronList | single neuron
                      Neuron(s) to intersect.
    volume :          list or dict of navis.Volume
    attr :            str | None, optional
                      Attribute to return for intersected neurons (e.g.
                      'cable_length' for TreeNeurons). If None, will return
                      the neuron subset to the volumes.
    **kwargs
                      Keyword arguments passed to [`navis.in_volume`][].

    Returns
    -------
    pandas DataFrame

    Examples
    --------
    >>> import navis
    >>> # Grab neurons
    >>> nl = navis.example_neurons(3)
    >>> # Grab a single volume
    >>> lh = navis.example_volume("LH")
    >>> # Re-use for testing
    >>> vols = {'lh1': lh, 'lh2': lh}
    >>> # Generate intersection matrix with cable length
    >>> m = navis.intersection_matrix(nl, vols, attr='cable_length')

    """
    # Volumes should be a dict at some point
    volumes_dict: Dict[str, core.Volume]

    if isinstance(x, core.BaseNeuron):
        x = core.NeuronList(x)

    if not isinstance(x, core.NeuronList):
        raise TypeError(f'x must be Neuron/List, not "{type(x)}"')

    if not isinstance(volumes, (list, dict)):
        raise TypeError('Volumes must be given as list or dict, not '
                        f'"{type(volumes)}"')

    if isinstance(volumes, list):
        volumes_dict = {v.name: v for v in volumes}
    else:
        volumes_dict = volumes

    for v in volumes_dict.values():
        if not isinstance(v, core.Volume):
            raise TypeError(f'Wrong data type found in volumes: "{type(v)}"')

    data = in_volume(x, volumes_dict, inplace=False, **kwargs)

    if not attr:
        df = pd.DataFrame([[n for n in data[v]] for v in data],
                          index=list(data.keys()),
                          columns=x.id)
    else:
        df = pd.DataFrame([[getattr(n, attr) for n in data[v]] for v in data],
                          index=list(data.keys()),
                          columns=x.id)

    return df
