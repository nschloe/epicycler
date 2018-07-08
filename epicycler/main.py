# -*- coding: utf-8 -*-
#
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy


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


def animate(polygon):
    n = polygon.shape[0]
    a = numpy.fft.fft(polygon[:, 0] + 1j * polygon[:, 1])
    freqs = numpy.fft.fftfreq(n)

    fig, ax = plt.subplots()
    radii = numpy.abs(a / n)

    center = numpy.array([0.0, 0.0])
    dot = plt.plot([], [], '.k')[0]
    circles = [
        plt.Circle(center, radius, color='k', fill=False)
        for radius in radii[1:]
    ]
    for circle in circles:
        ax.add_artist(circle)
    sum_radii = numpy.sum(radii[1:])
    center0 = [a[0].real / n, a[0].imag / n]
    xlim = [center0[0] - 1.1 * sum_radii, center0[0] + 1.1 * sum_radii]
    ylim = [center0[1] - 1.1 * sum_radii, center0[1] + 1.1 * sum_radii]
    ax.axis('square')
    ax.set_xlim([xlim[0], xlim[1]])
    ax.set_ylim([ylim[0], ylim[1]])

    plt.plot(polygon[:, 0], polygon[:, 1], ".")

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
        fig, animate, init_func=init,
        frames=numpy.linspace(0.0, 2 * numpy.pi, num_frames),
        interval=10,
        blit=True
    )

    plt.show()
    # anim.save(
    #     'out.mp4', fps=30,
    #     # extra_args=['-vcodec', 'libx264']
    #     )

    # plt.axis("equal")
    # plt.show()
    return
