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

from ... import config

__all__ = ['get_viewer', 'clear3d', 'close3d', 'pop3d']


def get_viewer():
    """Grab active 3D viewer.

    Returns
    -------
    [`navis.Viewer`][]

    Examples
    --------
    >>> import navis
    >>> from vispy import scene
    >>> # Get and plot neuron in 3d
    >>> n = navis.example_neurons(1)
    >>> _ = n.plot3d(color='red', backend='vispy')
    >>> # Grab active viewer and add custom text
    >>> viewer = navis.get_viewer()
    >>> text = scene.visuals.Text(text='TEST',
    ...                           pos=(0, 0, 0))
    >>> viewer.add(text)
    >>> # Close viewer
    >>> viewer.close()

    """
    return getattr(config, 'primary_viewer', None)


def clear3d():
    """Clear viewer 3D canvas."""
    viewer = get_viewer()

    if viewer:
        viewer.clear()


def close3d():
    """Close existing 3D viewer (wipes memory)."""
    try:
        viewer = get_viewer()
        viewer.close()
        globals().pop('viewer')
        del viewer
    except BaseException:
        pass


def pop3d():
    """Remove the last item added to the 3D canvas."""
    viewer = get_viewer()
    viewer.pop()
