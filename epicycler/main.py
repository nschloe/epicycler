# -*- coding: utf-8 -*-
#
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy
import tspsolve


def plot(polygon):
    n = polygon.shape[0]
    a = numpy.fft.fft(polygon[:, 0] + 1j * polygon[:, 1])
    freqs = numpy.fft.fftfreq(n)

    t = numpy.linspace(0.0, 2 * numpy.pi, 1000)
    # In principle, this is the inverse transform with a higher sampling rate.
    vals = numpy.sum(a / n * numpy.exp(1j * numpy.multiply.outer(t, n * freqs)), axis=1)

    plt.plot(vals.real, vals.imag, "-")
    plt.plot(polygon[:, 0], polygon[:, 1], ".")
    plt.axis("equal")
    plt.show()
    return


def animate_image(
    filename,
    xylim="polygon",
    output_filename=None,
    cutoff_radius=0.0,
    pixel_opacity_threshold=0.9,
):
    img = plt.imread(filename)

    # Find all pixel positions where the alpha value is greater than a threshold
    yx = numpy.array(numpy.where(img[:, :, 3] > pixel_opacity_threshold))
    xy = yx[[1, 0]]

    # prepare matrix of distances
    dx = numpy.subtract.outer(xy[0], xy[0])
    dy = numpy.subtract.outer(xy[1], xy[1])
    d = numpy.sqrt(dx ** 2 + dy ** 2)
    # solve tsp
    path = tspsolve.nearest_neighbor(d)
    path = tspsolve.two_opt(d, path).tolist()

    # plt.plot(xy[0, path + [path[0]]], xy[1, path + [path[0]]], "-")
    # plt.axis("square")
    # plt.gca().invert_yaxis()
    # plt.show()

    # r = list(range(xy.shape[1]))
    # dist = {(i, j): d[i][j] for i in r for j in r}
    # path = tsp.tsp(r, dist)
    # print(path)
    # exit(1)

    animate_poly(
        xy[:, path].T,
        xylim=xylim,
        output_filename=output_filename,
        cutoff_radius=cutoff_radius,
        invert_yaxis=True,
        show_axes=False,
    )
    return


def animate_poly(
    polygon,
    xylim="polygon",
    show_axes=True,
    output_filename=None,
    cutoff_radius=0.0,
    invert_yaxis=False,
):
    n = polygon.shape[0]
    a = numpy.fft.fft(polygon[:, 0] + 1j * polygon[:, 1])
    freqs = numpy.fft.fftfreq(n)

    fig, ax = plt.subplots()

    # Make the plot tighter, <https://stackoverflow.com/a/15883620/353337>
    fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)

    ax.axis("square")

    radii = numpy.abs(a / n)

    cut = radii > cutoff_radius
    a = a[cut]
    radii = radii[cut]
    freqs = freqs[cut]

    new_red = "#d62728"
    dot = plt.plot([], [], ".", color=new_red)[0]
    circles = [
        plt.Circle((0.0, 0.0), radius, color="k", fill=False) for radius in radii[1:]
    ]
    for circle in circles:
        ax.add_artist(circle)

    if xylim == "polygon":
        xlim = [numpy.min(polygon[:, 0]), numpy.max(polygon[:, 0])]
        ylim = [numpy.min(polygon[:, 1]), numpy.max(polygon[:, 1])]
        width = xlim[1] - xlim[0]
        height = ylim[1] - ylim[0]
        xlim = [xlim[0] - 0.1 * width, xlim[1] + 0.1 * width]
        ylim = [ylim[0] - 0.1 * height, ylim[1] + 0.1 * height]
    elif xylim == "circles":
        sum_radii = numpy.sum(radii[1:])
        center0 = [a[0].real / n, a[0].imag / n]
        xlim = [center0[0] - 1.1 * sum_radii, center0[0] + 1.1 * sum_radii]
        ylim = [center0[1] - 1.1 * sum_radii, center0[1] + 1.1 * sum_radii]
    else:
        assert len(xylim) == 4
        xylim = [float(x) for x in xylim]
        xlim = xylim[:2]
        ylim = xylim[2::]

    ax.set_xlim([xlim[0], xlim[1]])
    ax.set_ylim([ylim[0], ylim[1]])

    if invert_yaxis:
        ax.invert_yaxis()

    if not show_axes:
        ax.axis("off")

    plt.plot(polygon[:, 0], polygon[:, 1], ".", color="0.7")

    def init():
        return circles + [dot]

    def animate(t):
        vals = a / n * numpy.exp(1j * numpy.multiply.outer(t, n * freqs))
        cs = numpy.cumsum(vals)
        centers = cs[:-1]
        for circle, center in zip(circles, centers):
            circle.center = [center.real, center.imag]
        dot.set_data(cs[-1].real, cs[-1].imag)
        return circles + [dot]

    num_frames = 1000

    anim = FuncAnimation(
        fig,
        animate,
        init_func=init,
        frames=numpy.linspace(0.0, 2 * numpy.pi, num_frames),
        interval=10,
        blit=True,
    )

    if output_filename:
        anim.save(
            output_filename,
            fps=60,
            # writer="imagemagick",
            # extra_args=['-vcodec', 'libx264']
        )
    else:
        plt.show()
    return
