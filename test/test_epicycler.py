# -*- coding: utf-8 -*-
#
import numpy

import epicycler

from helpers import download_image


def test_plot():
    polygon = numpy.array([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.1]])
    epicycler.plot(polygon)
    return


def test_cli_poly():
    epicycler.cli.poly(
        [
            "0.0",
            "0.0",
            "1.0",
            "0.0",
            "1.0",
            "2.0",
            "-0.5",
            "1.1",
            "-0.5",
            "2.1",
            "--xylim",
            "-1.5",
            "+2.0",
            "-1.3",
            "3.0",
        ]
    )
    return


def test_cli_image():
    filename = download_image(
        "seagull.png", "79ab5c6a3ce01135009fcdc1a555c692eb35fe0cb0b3eddbe9d58251"
    )
    epicycler.cli.image(
        [
            filename,
            "-c",
            "0.5",
            # "-o", "seagull.mp4"
        ]
    )
    return


if __name__ == "__main__":
    test_cli_poly()
    # test_cli_image()
