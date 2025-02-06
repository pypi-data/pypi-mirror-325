import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def plot_grid(grid, filename, cuts=[]):
    plt.rcParams.update({"text.usetex": True, "font.family": "Helvetica"})
    tilesize = 1
    xs = np.linspace(0, grid.len_x * tilesize, grid.len_x + 1)
    ys = np.linspace(0, grid.len_y * tilesize, grid.len_y + 1)

    fig, ax = plt.subplots()

    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    w, h = xs[1] - xs[0], ys[1] - ys[0]
    for i, x in enumerate(xs[:-1]):
        for j, y in enumerate(ys[:-1]):
            if grid.map[j, i] == '*':
                ax.add_patch(
                    Rectangle((x, y), w, h, fill=True, color='black', alpha=.5)
                )
            elif (j, i) in grid.colors:
                ax.add_patch(
                    Rectangle((x, y), w, h, fill=True, color=grid.colors[(j, i)], alpha=.3)  # noqa: E501
                )
            else:
                ax.add_patch(Rectangle((x, y), w, h, fill=True, color='#ffffff'))
            if (j, i) in grid.labels:
                ax.text(
                    x + tilesize * 0.5,
                    y + tilesize * 0.5,
                    r'$' + grid.labels[(j, i)][0] + '$',
                    fontsize=25, rotation=0,
                    horizontalalignment='center', verticalalignment='center',
                    rotation_mode='anchor'
                )

    # grid lines
    for x in xs:
        ax.plot([x, x], [ys[0], ys[-1]], color='black', alpha=.33)
    for y in ys:
        ax.plot([xs[0], xs[-1]], [y, y], color='black', alpha=.33)

    width = tilesize / 20
    for cut in cuts:
        startxy = cut[0]
        endxy = cut[1]
        delx = startxy[0] - endxy[0]
        dely = startxy[1] - endxy[1]
        if delx == 0:
            if dely < 0:
                ax.add_patch(
                    Rectangle(
                        (startxy[1] - width / 2 - dely*tilesize,
                        startxy[0] - width / 2), width,  # noqa: E128
                        tilesize + width, fill=True,
                        color='black', alpha=1.0
                    )
                )
            else:
                ax.add_patch(
                    Rectangle((startxy[1] - width / 2,
                    startxy[0] - width/2), width,  # noqa: E128
                    tilesize + width, fill=True,  # noqa: E122
                    color='black', alpha=1.0)  # noqa: E122
                )
        elif dely == 0:
            if delx < 0:
                ax.add_patch(
                    Rectangle((startxy[1] - width / 2,
                    startxy[0] - width/2 - delx * tilesize),  # noqa: E128
                    tilesize + width, width, fill=True,  # noqa: E122
                    color='black', alpha=1.0)  # noqa: E122
                )
            else:
                ax.add_patch(
                    Rectangle((startxy[1] - width / 2,
                    startxy[0] - width/2), tilesize + width,  # noqa: E128
                    width, fill=True, color='black', alpha=1.0)  # noqa: E122
                )

    ax.invert_yaxis()
    ax.axis('equal')
    fig.savefig(filename + '.pdf')
