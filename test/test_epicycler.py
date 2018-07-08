# -*- coding: utf-8 -*-
#
import numpy

import epicycler


def test_plot():
    polygon = numpy.array([
        [0.0, 0.0],
        [1.0, 0.0],
        [1.0, 1.0],
        [0.0, 1.1],
    ])
    epicycler.plot(polygon)
    return


def test_animate():
    polygon = numpy.array([
        [0.0, 0.0],
        [1.0, 0.0],
        [1.0, 2.0],
        [-0.5, 1.1],
        [-0.5, 2.1],
    ])
    epicycler.animate(polygon)
    return


if __name__ == "__main__":
    test_animate()
