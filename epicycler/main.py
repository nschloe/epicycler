# -*- coding: utf-8 -*-
#
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy
from tsp_solver.greedy import solve_tsp


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


def animate_image(filename):
    img = plt.imread(filename)

    # Find all pixel positions where the alpha value is greater than a threshold
    threshold = 0.9999
    xy = numpy.array(numpy.where(img[:, :, 3] > threshold))

    # Solve the traveling salesman problem for a reasonable path traversing the pixels.
    # prepare matrix of distances
    dx = numpy.subtract.outer(xy[0], xy[0])
    dy = numpy.subtract.outer(xy[1], xy[1])
    d = numpy.sqrt(dx ** 2 + dy ** 2)
    path = solve_tsp(d)

    animate(xy[:, path].T)
    return


def animate(polygon, xylim="polygon"):
    n = polygon.shape[0]
    a = numpy.fft.fft(polygon[:, 0] + 1j * polygon[:, 1])
    freqs = numpy.fft.fftfreq(n)

    fig, ax = plt.subplots()
    ax.axis("square")

    radii = numpy.abs(a / n)

    center = numpy.array([0.0, 0.0])
    dot = plt.plot([], [], ".r")[0]
    circles = [
        plt.Circle(center, radius, color="k", fill=False) for radius in radii[1:]
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
        assert len(xylim) == 2
        xlim, ylim = xylim

    ax.set_xlim([xlim[0], xlim[1]])
    ax.set_ylim([ylim[0], ylim[1]])

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

    plt.show()
    # anim.save(
    #     'out.mp4',
    #     # 'out.gif',
    #     fps=30,
    #     # writer='imagemagick',
    #     # extra_args=['-vcodec', 'libx264']
    #     )

    # plt.axis("equal")
    # plt.show()
    return
