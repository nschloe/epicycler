# -*- coding: utf-8 -*-
#
import numpy

import epicycler


def test_plot():
    polygon = numpy.array([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.1]])
    epicycler.plot(polygon)
    return


def test_animate():
    polygon = numpy.array(
        [[0.0, 0.0], [1.0, 0.0], [1.0, 2.0], [-0.5, 1.1], [-0.5, 2.1]]
    )
    epicycler.animate_poly(polygon, xylim=[-1.5, +2.0, -1.3, 3.0], show_axes=False)
    return


if __name__ == "__main__":
    test_animate()
