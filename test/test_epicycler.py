# -*- coding: utf-8 -*-
#
import numpy

import epicycler


def test():
    polygon = numpy.array([
        [0.0, 0.0],
        [1.0, 0.0],
        [1.0, 1.0],
        [0.0, 1.1],
    ])
    epicycler.plot(polygon)
    return


if __name__ == "__main__":
    test()
