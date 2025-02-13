#    This script is part of navis (http://www.github.com/navis-org/navis).
#    Copyright (C) 2017 Philipp Schlegel
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
#
#    You should have received a copy of the GNU General Public License
#    along

"""Functions to generate vispy visuals."""

import uuid
import warnings

import pandas as pd
import numpy as np

import matplotlib.colors as mcl

from ... import core, config, utils, conversion
from ..colors import prepare_colormap, vertex_colors, eval_color

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    import vispy
    from vispy import scene
    from vispy.geometry import create_sphere

__all__ = [
    "volume2vispy",
    "neuron2vispy",
    "dotprop2vispy",
    "voxel2vispy",
    "points2vispy",
    "combine_visuals",
]

logger = config.get_logger(__name__)


def volume2vispy(x, settings):
    """Convert Volume(s) to vispy visuals."""
    # Must not use make_iterable here as this will turn into list of keys!
    if not isinstance(x, (list, np.ndarray)):
        x = [x]

    # List to fill with vispy visuals
    visuals = []
    for i, v in enumerate(x):
        if not isinstance(v, core.Volume):
            raise TypeError(f'Expected navis.Volume, got "{type(v)}"')

        object_id = uuid.uuid4()

        if settings.color is not None:
            color = settings.color
        else:
            color = getattr(v, "color", (0.95, 0.95, 0.95, 0.1))

        # Colors might be list, need to pick the correct color for this volume
        if isinstance(color, list):
            if all([isinstance(c, (tuple, list, np.ndarray)) for c in color]):
                color = color[i]

        if isinstance(color, str):
            color = mcl.to_rgb(color)

        color = np.array(color, dtype=float)

        # Add alpha
        if len(color) < 4:
            color = np.append(color, [0.1])

        if max(color) > 1:
            color[:3] = color[:3] / 255

        s = scene.visuals.Mesh(
            vertices=v.vertices,
            faces=v.faces,
            color=color,
            shading=settings.shading,
        )

        # Set some aesthetic parameters
        # Note that for larger meshes adjusting the shading filter actually
        # surprisingly slow (e.g. ~4s @ 400k faces). Since volumes typically
        # don't have too many faces, we will keep setting the shininess.
        if int(vispy.__version__.split(".")[1]) >= 7:
            s.shading_filter.shininess = 0
        else:
            s.shininess = 0

        # Possible presets are "additive", "translucent", "opaque"
        s.set_gl_state("additive", cull_face=True, depth_test=False)
        # s.set_gl_state('additive' if color[3] < 1 else 'opaque',
        #               cull_face=True,
        #               depth_test=False if color[3] < 1 else True)

        # Make sure volumes are always drawn after neurons
        s.order = 10

        # Add custom attributes
        s.unfreeze()
        s._object_type = "volume"
        s._volume_name = getattr(v, "name", None)
        s._object = v
        s._object_id = object_id
        s.freeze()

        visuals.append(s)

    return visuals


def neuron2vispy(x, settings):
    """Convert a Neuron/List to vispy visuals.

    Parameters
    ----------
    x :               TreeNeuron | MeshNeuron | Dotprops | VoxelNeuron | NeuronList
                      Neuron(s) to plot.
    color :           list | tuple | array | str
                      Color to use for plotting.
    colormap :        tuple | dict | array
                      Color to use for plotting. Dictionaries should be mapped
                      by ID. Overrides `color`.
    connectors :      bool, optional
                      If True, plot connectors.
    connectors_only : bool, optional
                      If True, only connectors are plotted.
    by_strahler :     bool, optional
                      If True, shade neurites by strahler order.
    by_confidence :   bool, optional
                      If True, shade neurites by confidence.
    linewidth :       int, optional
                      Set linewidth. Might not work depending on your backend.
    cn_mesh_colors :  bool, optional
                      If True, connectors will have same color as the neuron.
    cn_layout :       dict, optional
                      Sets connector (e.g. synapse) layout. For example::

                        {
                            0: {
                                'name': 'Presynapses',
                                'color': (255, 0, 0)
                                },
                            1: {
                                'name': 'Postsynapses',
                                'color': (0, 0, 255)
                                },
                            2: {
                                'name': 'Gap junctions',
                                'color': (0, 255, 0)
                                },
                            'display': 'lines'  # can also be 'circles'
                        }

    Returns
    -------
    list
                    Contains vispy visuals for each neuron.

    """
    if isinstance(x, core.BaseNeuron):
        x = core.NeuronList(x)
    elif isinstance(x, core.NeuronList):
        pass
    else:
        raise TypeError(f'Unable to process data of type "{type(x)}"')

    # colors = kwargs.get('color',
    #                     kwargs.get('c',
    #                                kwargs.get('colors', None)))
    # palette = kwargs.get('palette', None)
    # color_by = kwargs.get('color_by', None)
    # shade_by = kwargs.get('shade_by', None)

    # Color_by can be a per-node/vertex color, or a per-neuron color
    # such as property of the neuron
    color_neurons_by = None
    if settings.color_by is not None and x:
        # Check if this is a neuron property
        if isinstance(settings.color_by, str):
            if hasattr(x[0], settings.color_by):
                # If it is, use it to color neurons
                color_neurons_by = [getattr(neuron, settings.color_by) for neuron in x]
                settings.color_by = None
        elif isinstance(settings.color_by, (list, np.ndarray)):
            if len(settings.color_by) == len(x):
                color_neurons_by = settings.color_by
                settings.color_by = None

    if not isinstance(settings.color_by, type(None)):
        if not settings.palette:
            raise ValueError(
                'Must provide `palette` (e.g. "viridis") argument '
                "if using `color_by`"
            )

        colormap = vertex_colors(
            x,
            by=settings.color_by,
            alpha=settings.alpha,
            palette=settings.palette,
            vmin=settings.vmin,
            vmax=settings.vmax,
            na="raise",
            color_range=1,
        )
    else:
        colormap, _ = prepare_colormap(
            settings.color,
            neurons=x,
            palette=settings.palette,
            alpha=settings.alpha,
            color_by=color_neurons_by,
            color_range=1,
        )

    if not isinstance(settings.shade_by, type(None)):
        alphamap = vertex_colors(
            x,
            by=settings.shade_by,
            use_alpha=True,
            palette="viridis",  # palette is irrelevant here
            vmin=settings.smin,
            vmax=settings.smax,
            na="raise",
            color_range=1,
        )

        new_colormap = []
        for c, a in zip(colormap, alphamap):
            if not (isinstance(c, np.ndarray) and c.ndim == 2):
                c = np.tile(c, (a.shape[0], 1))

            if c.shape[1] == 4:
                c[:, 3] = a[:, 3]
            else:
                c = np.insert(c, 3, a[:, 3], axis=1)

            new_colormap.append(c)
        colormap = new_colormap

    # List to fill with vispy visuals
    visuals = []
    _radius_warned = False
    for i, neuron in enumerate(x):
        # Generate random ID -> we need this in case we have duplicate IDs
        object_id = uuid.uuid4()

        if isinstance(neuron, core.TreeNeuron) and settings.radius == "auto":
            # Number of nodes with radii
            n_radii = (neuron.nodes.get("radius", pd.Series([])).fillna(0) > 0).sum()
            # If less than 30% of nodes have a radius, we will fall back to lines
            if n_radii / neuron.nodes.shape[0] < 0.3:
                settings.radius = False

        if isinstance(neuron, core.TreeNeuron) and settings.radius:
            # Warn once if more than 5% of nodes have missing radii
            if not _radius_warned:
                if (
                    (neuron.nodes.radius.fillna(0).values <= 0).sum() / neuron.n_nodes
                ) > 0.05:
                    logger.warning(
                        "Some skeleton nodes have radius <= 0. This may lead to "
                        "rendering artifacts. Set `radius=False` to plot skeletons "
                        "as single-width lines instead."
                    )
                    _radius_warned = True

            _neuron = conversion.tree2meshneuron(
                neuron,
                warn_missing_radii=False,
                radius_scale_factor=settings.get("linewidth", 1),
            )
            _neuron.connectors = neuron.connectors
            neuron = _neuron

            # See if we need to map colors to vertices
            if isinstance(colormap[i], np.ndarray) and colormap[i].ndim == 2:
                colormap[i] = colormap[i][neuron.vertex_map]

        neuron_color = colormap[i]
        if not settings.connectors_only:
            if isinstance(neuron, core.TreeNeuron):
                visuals += skeleton2vispy(neuron, neuron_color, object_id, settings)
            elif isinstance(neuron, core.MeshNeuron):
                visuals += mesh2vispy(neuron, neuron_color, object_id, settings)
            elif isinstance(neuron, core.Dotprops):
                visuals += dotprop2vispy(neuron, neuron_color, object_id, settings)
            elif isinstance(neuron, core.VoxelNeuron):
                visuals += voxel2vispy(neuron, neuron_color, object_id, settings)
            else:
                logger.warning(
                    f"Don't know how to plot neuron of type '{type(neuron)}'"
                )

        if settings.connectors or settings.connectors_only and neuron.has_connectors:
            visuals += connectors2vispy(neuron, neuron_color, object_id, settings)

    return visuals


def connectors2vispy(neuron, neuron_color, object_id, settings):
    """Convert connectors to vispy visuals."""
    cn_lay = config.default_connector_colors.copy()
    cn_lay.update(settings.cn_layout)

    if isinstance(settings.connectors, (list, np.ndarray, tuple)):
        connectors = neuron.connectors[neuron.connectors.type.isin(settings.connectors)]
    elif settings.connectors == "pre":
        connectors = neuron.presynapses
    elif settings.connectors == "post":
        connectors = neuron.postsynapses
    elif isinstance(settings.connectors, str):
        connectors = neuron.connectors[neuron.connectors.type == settings.connectors]
    else:
        connectors = neuron.connectors

    visuals = []
    for j, this_cn in connectors.groupby("type"):
        if isinstance(settings.cn_colors, dict):
            color = settings.cn_colors.get(
                j, cn_lay.get(j, {}).get("color", (0.1, 0.1, 0.1))
            )
        elif settings.cn_colors == "neuron":
            color = neuron_color
        elif settings.cn_colors is not None:
            color = settings.cn_colors
        else:
            color = cn_lay.get(j, {}).get("color", (0.1, 0.1, 0.1))

        color = eval_color(color, color_range=1)

        pos = this_cn[["x", "y", "z"]].apply(pd.to_numeric).values

        mode = cn_lay["display"]
        if mode == "circles" or isinstance(neuron, core.MeshNeuron):
            con = scene.visuals.Markers(
                spherical=cn_lay.get("spherical", True),
                scaling=cn_lay.get("scale", False),
            )

            con.set_data(
                pos=np.array(pos),
                face_color=color,
                edge_color=color,
                size=settings.cn_size if settings.cn_size else cn_lay["size"],
            )

        elif mode == "lines":
            tn_coords = (
                neuron.nodes.set_index("node_id")
                .loc[this_cn.node_id.values][["x", "y", "z"]]
                .apply(pd.to_numeric)
                .values
            )

            segments = [item for sublist in zip(pos, tn_coords) for item in sublist]

            con = scene.visuals.Line(
                pos=np.array(segments),
                color=color,
                # Can only be used with method 'agg'
                width=settings.linewidth,
                connect="segments",
                antialias=False,
                method="gl",
            )
            # method can also be 'agg' -> has to use connect='strip'
        else:
            raise ValueError(f'Unknown connector display mode "{mode}"')

        # Add custom attributes
        con.unfreeze()
        con._object_type = "neuron"
        con._neuron_part = "connectors"
        con._id = neuron.id
        con._name = str(getattr(neuron, "name", neuron.id))
        con._object_id = object_id
        con._object = neuron
        con.freeze()

        visuals.append(con)
    return visuals


def mesh2vispy(neuron, neuron_color, object_id, settings):
    """Convert mesh (i.e. MeshNeuron) to vispy visuals."""
    # Skip empty neurons
    if not len(neuron.faces):
        return []

    color_kwargs = dict(color=neuron_color)
    if isinstance(neuron_color, np.ndarray) and neuron_color.ndim == 2:
        if len(neuron_color) == len(neuron.vertices):
            color_kwargs = dict(vertex_colors=neuron_color)
        elif len(neuron_color) == len(neuron.faces):
            color_kwargs = dict(face_colors=neuron_color)
        else:
            color_kwargs = dict(color=neuron_color)

    # There is a bug in pickling/unpickling numpy arrays where an internal flag
    # is set from 1 to 0 -> this then in turn upsets vispy. See also:
    # https://github.com/vispy/vispy/issues/1741#issuecomment-574425662
    # Pickling happens when meshneurons have been multi-processed. To fix this
    # the best way is to use astype (.copy() doesn't cut it)
    if neuron.vertices.dtype.isbuiltin == 0:
        neuron.vertices = neuron.vertices.astype(neuron.vertices.dtype.str)
    if neuron.faces.dtype.isbuiltin == 0:
        neuron.faces = neuron.faces.astype(neuron.faces.dtype.str)

    m = scene.visuals.Mesh(
        vertices=neuron.vertices,
        faces=neuron.faces,
        shading=settings.shading,
        **color_kwargs,
    )

    # Set some aesthetic parameters
    # Vispy 0.7.0 uses a new shading filter
    # Note that for larger meshes adjusting the shading filter is actually
    # surprisingly slow (e.g. ~4s @ 400k faces)
    if isinstance(settings.shininess, (int, float)):
        if int(vispy.__version__.split(".")[1]) >= 7:
            m.shading_filter.shininess = settings.shininess
        else:
            m.shininess = settings.shininess

    # Possible presets are "additive", "translucent", "opaque"
    if len(neuron_color) == 4 and neuron_color[3] < 1:
        m.set_gl_state("additive", cull_face=True, depth_test=False)

    # Add custom attributes
    m.unfreeze()
    m._object_type = "neuron"
    m._neuron_part = "neurites"
    m._id = neuron.id
    m._name = str(getattr(neuron, "name", neuron.id))
    m._object_id = object_id
    m._object = neuron
    m.freeze()
    return [m]


def to_vispy_cmap(color, fade=True):
    """Convert a given colour to a vispy colormap."""
    # First force RGB
    stop = mcl.to_rgba(color)
    start = mcl.to_rgba(color, alpha=0)

    # Convert to vispy cmap
    colors = vispy.color.ColorArray([start, stop])
    cmap = vispy.color.colormap.Colormap(colors=colors)

    # cmap consists of two colors
    # We will set first color to black and transparent
    if fade:
        col_arr = cmap.colors.rgba
        col_arr[1][:] = 0
        cmap.colors.rgba = col_arr

    return cmap


def voxel2vispy(neuron, neuron_color, object_id, settings):
    """Convert voxels (i.e. VoxelNeuron) to vispy visuals."""
    # Note the transpose: currently, vispy expects zyx for volumes but this
    # might change in the future
    grid = neuron.grid.T
    # Vispy doesn't like boolean matrices here
    if grid.dtype == bool:
        grid = grid.astype(int)
    vx = scene.visuals.Volume(vol=grid, cmap=to_vispy_cmap(neuron_color))

    # Add transforms
    vx.set_transform("st", scale=neuron.units_xyz.magnitude, translate=neuron.offset)

    # Add custom attributes
    vx.unfreeze()
    vx._object_type = "neuron"
    vx._neuron_part = "neurites"
    vx._id = neuron.id
    vx._name = str(getattr(neuron, "name", neuron.id))
    vx._object_id = object_id
    vx._object = neuron
    vx.freeze()
    return [vx]


def skeleton2vispy(neuron, neuron_color, object_id, settings):
    """Convert skeleton (i.e. TreeNeuron) into vispy visuals."""
    if neuron.nodes.empty:
        logger.warning(f"Skipping TreeNeuron w/o nodes: {neuron.id}")
        return []
    elif neuron.nodes.shape[0] == 1:
        logger.warning(f"Skipping single-node TreeNeuron: {neuron.label}")
        return []

    visuals = []
    if not settings.connectors_only:
        # Make sure we have one color for each node
        neuron_color = np.asarray(neuron_color)
        if neuron_color.ndim == 1:
            neuron_color = np.tile(neuron_color, (neuron.nodes.shape[0], 1))

        # Get nodes
        non_roots = neuron.nodes[neuron.nodes.parent_id >= 0]
        connect = np.zeros((non_roots.shape[0], 2), dtype=int)
        node_ix = pd.Series(
            np.arange(neuron.nodes.shape[0]), index=neuron.nodes.node_id.values
        )
        connect[:, 0] = node_ix.loc[non_roots.node_id].values
        connect[:, 1] = node_ix.loc[non_roots.parent_id].values

        # Create line plot from segments.
        t = scene.visuals.Line(
            pos=neuron.nodes[["x", "y", "z"]].values,
            color=neuron_color,
            # Can only be used with method 'agg'
            width=settings.linewidth,
            connect=connect,
            antialias=True,
            method="gl",
        )
        # method can also be 'agg' -> has to use connect='strip'
        # Make visual discoverable
        t.interactive = True

        # Add custom attributes
        t.unfreeze()
        t._object_type = "neuron"
        t._neuron_part = "neurites"
        t._id = neuron.id
        t._name = str(getattr(neuron, "name", neuron.id))
        t._object = neuron
        t._object_id = object_id
        t.freeze()

        visuals.append(t)

        # Extract and plot soma
        soma = utils.make_iterable(neuron.soma)
        if settings.soma:
            # If soma detection is messed up we might end up producing
            # hundrets of soma which will freeze the session
            if len(soma) >= 10:
                logger.warning(
                    f"Neuron {neuron.id} appears to have {len(soma)}"
                    " somas. That does not look right - will ignore "
                    "them for plotting."
                )
            else:
                for s in soma:
                    # Skip `None` somas
                    if isinstance(s, type(None)):
                        continue

                    # If we have colors for every vertex, we need to find the
                    # color that corresponds to this root (or it's parent to be
                    # precise)
                    if isinstance(neuron_color, np.ndarray) and neuron_color.ndim > 1:
                        s_ix = np.where(neuron.nodes.node_id == s)[0][0]
                        soma_color = neuron_color[s_ix]
                    else:
                        soma_color = neuron_color

                    n = neuron.nodes.set_index("node_id").loc[s]
                    r = (
                        getattr(n, neuron.soma_radius)
                        if isinstance(neuron.soma_radius, str)
                        else neuron.soma_radius
                    )
                    sp = create_sphere(7, 7, radius=r)
                    verts = sp.get_vertices() + n[["x", "y", "z"]].values.astype(
                        np.float32
                    )
                    s = scene.visuals.Mesh(
                        vertices=verts,
                        shading="smooth",
                        faces=sp.get_faces(),
                        color=soma_color,
                    )
                    # Vispy 0.7.0 uses a new shading filter
                    if int(vispy.__version__.split(".")[1]) >= 7:
                        s.shading_filter.ambient_light = vispy.color.Color("white")
                        s.shading_filter.shininess = 0
                    else:
                        s.ambient_light_color = vispy.color.Color("white")
                        s.shininess = 0

                    # Make visual discoverable
                    s.interactive = True

                    # Add custom attributes
                    s.unfreeze()
                    s._object_type = "neuron"
                    s._neuron_part = "soma"
                    s._id = neuron.id
                    s._name = str(getattr(neuron, "name", neuron.id))
                    s._object = neuron
                    s._object_id = object_id
                    s.freeze()

                    visuals.append(s)

    return visuals


def dotprop2vispy(x, neuron_color, object_id, settings):
    """Convert dotprops(s) to vispy visuals.

    Parameters
    ----------
    x :             navis.Dotprops | pd.DataFrame
                    Dotprop(s) to plot.

    Returns
    -------
    list
                    Contains vispy visuals for each dotprop.

    """
    # Skip empty neurons
    if not len(x.points):
        return []

    # Generate TreeNeuron
    tn = x.to_skeleton(scale_vec=settings.dps_scale_vec)
    return skeleton2vispy(tn, neuron_color, object_id, settings)


def points2vispy(x, **kwargs):
    """Convert points to vispy visuals.

    Parameters
    ----------
    x :             list of arrays
                    Points to plot.
    color :         tuple | array
                    Color to use for plotting.
    size :          int, optional
                    Marker size.

    Returns
    -------
    list
                    Contains vispy visuals for points.

    """
    colors = kwargs.get(
        "color",
        kwargs.get("c", kwargs.get("colors", eval_color(config.default_color, 1))),
    )

    visuals = []
    for p in x:
        object_id = uuid.uuid4()
        if not isinstance(p, np.ndarray):
            p = np.array(p)

        con = scene.visuals.Markers(
            spherical=kwargs.get("spherical", True), scaling=kwargs.get("scale", False)
        )
        con.set_data(
            pos=p,
            face_color=colors,
            edge_color=colors,
            size=kwargs.get("size", kwargs.get("s", 2)),
        )

        # Add custom attributes
        con.unfreeze()
        con._object_type = "points"
        con._object_id = object_id
        con.freeze()

        visuals.append(con)

    return visuals


def combine_visuals(visuals, name=None):
    """Attempt to combine multiple visuals of similar type into one.

    Parameters
    ----------
    visuals :   List
                List of visuals.
    name :      str, optional
                Legend name for the combined visual.

    Returns
    -------
    list
                List of visuals some of which where combined.

    """
    if any([not isinstance(v, scene.visuals.VisualNode) for v in visuals]):
        raise TypeError("Visuals must all be instances of VisualNode")

    # Combining visuals (i.e. adding pos AND changing colors) fails if
    # they are already on a canvas
    if any([v.parent for v in visuals]):
        raise ValueError("Visuals must not have parents when combined.")

    # Sort into types
    types = set([type(v) for v in visuals])

    by_type = {ty: [v for v in visuals if type(v) is ty] for ty in types}

    combined = []

    # Now go over types and combine when possible
    for ty in types:
        # Skip if nothing to combine
        if len(by_type[ty]) <= 1:
            combined += by_type[ty]
            continue

        if ty == scene.visuals.Line:
            # Collate data
            pos = np.concatenate([vis._pos for vis in by_type[ty]])

            # We need to produce one color/vertex and offset the connections
            colors = []
            connect = []
            offset = 0
            for vis in by_type[ty]:
                if vis.color.ndim == 2:
                    colors.append(vis.color)
                else:
                    colors.append(np.repeat([vis.color], vis.pos.shape[0], axis=0))
                connect.append(vis._connect + offset)
                offset += vis._pos.shape[0]

            connect = np.concatenate(connect)
            colors = np.concatenate(colors)

            t = scene.visuals.Line(
                pos=pos,
                color=colors,
                # Can only be used with method 'agg'
                connect=connect,
                antialias=True,
                method="gl",
            )
            # method can also be 'agg' -> has to use connect='strip'
            # Make visual discoverable
            t.interactive = True

            # Add custom attributes
            t.unfreeze()
            t._object_type = "neuron"
            t._neuron_part = "neurites"
            t._id = "NA"
            t._object_id = uuid.uuid4()
            t._name = name if name else "NeuronCollection"
            t.freeze()

            combined.append(t)
        elif ty == scene.visuals.Mesh:
            vertices = []
            faces = []
            color = []
            for vis in by_type[ty]:
                verts_offset = sum([v.shape[0] for v in vertices])
                faces.append(vis.mesh_data.get_faces() + verts_offset)
                vertices.append(vis.mesh_data.get_vertices())

                vc = vis.mesh_data.get_vertex_colors()
                if not isinstance(vc, type(None)):
                    color.append(vc)
                else:
                    color.append(
                        np.tile(vis.color.rgba, len(vertices[-1])).reshape(-1, 4)
                    )

            faces = np.vstack(faces)
            vertices = np.vstack(vertices)
            color = np.concatenate(color)

            if np.unique(color, axis=0).shape[0] == 1:
                base_color = color[0]
            else:
                base_color = (1, 1, 1, 1)

            t = scene.visuals.Mesh(
                vertices,
                faces=faces,
                color=base_color,
                vertex_colors=color,
                shading=by_type[ty][0].shading,
                mode=by_type[ty][0].mode,
            )

            # Add custom attributes
            t.unfreeze()
            t._object_type = "neuron"
            t._neuron_part = "neurites"
            t._id = "NA"
            t._name = name if name else "MeshNeuronCollection"
            t._object_id = uuid.uuid4()
            t.freeze()

            combined.append(t)
        else:
            combined += by_type[ty]

    return combined
