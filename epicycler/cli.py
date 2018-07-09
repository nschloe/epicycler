# -*- coding: utf-8 -*-
#
from __future__ import print_function

import sys

from .__about__ import __version__
from .main import animate_image


def main(argv=None):
    # Parse command line arguments.
    parser = _get_parser()
    args = parser.parse_args(argv)

    animate_image(args.infile)
    return


def _get_parser():
    import argparse

    parser = argparse.ArgumentParser(
        description=("Create epicycle animation from image.")
    )

    parser.add_argument("infile", type=str, help="input image file")

    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version="%(prog)s {}, Python {}".format(__version__, sys.version),
        help="display version information",
    )

    return parser
