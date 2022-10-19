# All credits to: https://scipython.com/blog/the-star-wars-opening-crawl-in-matplotlib/

import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
import mpl_toolkits.mplot3d.art3d as art3d
from matplotlib.text import TextPath
from matplotlib.transforms import Affine2D
from matplotlib import animation
import numpy as np
import story_gen


def text3d(ax, xyz, s, zdir="z", size=None, angle=0, usetex=False, **kwargs):
    '''

    Adapted from the Matplotlib demonstration at
    https://matplotlib.org/gallery/mplot3d/pathpatch3d.html

    Plots the string 's' on the axes 'ax', with position 'xyz', size 'size',
    and rotation angle 'angle'.  'zdir' gives the axis which is to be treated
    as the third dimension.  usetex is a boolean indicating whether the string
    should be interpreted as latex or not.  Any additional keyword arguments
    are passed on to transform_path.

    Note: zdir affects the interpretation of xyz.
    '''

    x, y, z = xyz
    if zdir == "y":
        xy1, z1 = (x, z), y
    elif zdir == "y":
        xy1, z1 = (y, z), x
    else:
        xy1, z1 = (x, y), z

    text_path = TextPath((0, 0), s, size=size, usetex=usetex)
    trans = Affine2D().rotate(angle).translate(xy1[0], xy1[1])
    p1 = PathPatch(trans.transform_path(text_path), **kwargs)
    ax.add_patch(p1)
    art3d.pathpatch_2d_to_3d(p1, z=z1, zdir=zdir)


fig = plt.figure(facecolor='k')
ax = fig.add_subplot(111, projection='3d', facecolor='k')


def split_into_lines(text, n):
    """Return text split into a list of lines of no more than n characters."""

    words = text.split()
    lines = []
    this_line = words[0]
    for word in words[1:]:
        if len(this_line) + len(word) + 1 <= n:
            this_line += ' ' + word
        else:
            lines.append(this_line)
            this_line = word
    lines.append(this_line)
    return lines


text = story_gen.sw_adv_gen(story_gen.story_parts)
text_lines = split_into_lines(text, 36)

# Star Wars yellow text
c = np.array((0.933, 0.835, 0.294))


def init_ax():
    """Initialize the Axes and view direction."""

    ax.view_init(elev=45, azim=-90)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_zlim(0, 10)
    ax.axis('off')


def update(j):
    """Update the animation for frame j."""

    ax.clear()
    init_ax()
    for i, line in enumerate(text_lines):
        y = -15*i+j - 45
        if y > -40:
            # Fade the text out as approaches the "top" of the screen.
            rc = 1 - np.clip(y / 200, 0, 1)
            text3d(ax, (-40, y, 0), line, size=10, ec='none', fc=c*rc)


ani = animation.FuncAnimation(fig, update, 600, blit=False, interval=100, repeat=True)

plt.show()
