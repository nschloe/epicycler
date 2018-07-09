# -*- coding: utf-8 -*-
#
from __future__ import print_function

import argparse
import sys

import numpy

from .__about__ import __version__
from .main import animate_image, animate_poly


def image(argv=None):
    # Parse command line arguments.
    parser = _get_parser_image()
    args = parser.parse_args(argv)

    animate_image(
        args.infile,
        xylim=args.xylim,
        output_filename=args.output_file,
        cutoff_radius=args.cutoff_radius,
    )
    return


def _get_parser_image():
    parser = argparse.ArgumentParser(
        description=("Create epicycle animation from image.")
    )

    parser.add_argument("infile", type=str, help="input image file")

    parser.add_argument(
        "--xylim",
        nargs="+",
        help="xlim, ylim for plot (default: deduce from coordinates)",
        default="polygon",
    )

    parser.add_argument(
        "--cutoff-radius",
        "-c",
        type=float,
        help="epicycles smaller than this radius will be left out (default: 0.0)",
        default=0.0,
    )

    parser.add_argument(
        "--output-file",
        "-o",
        type=str,
        help="output file (default: none, show on screen)",
        default=None,
    )

    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version="%(prog)s {}, Python {}".format(__version__, sys.version),
        help="display version information",
    )

    return parser


def poly(argv=None):
    parser = _get_parser_poly()
    args = parser.parse_args(argv)

    assert len(args.coords) % 2 == 0, "Must specify an even number of values."

    animate_poly(
        numpy.reshape(args.coords, (-1, 2)),
        xylim=args.xylim,
        output_filename=args.output_file,
        show_axes=args.show_axes,
    )
    return


def _get_parser_poly():
    parser = argparse.ArgumentParser(
        description=("Create epicycle animation from a list of points.")
    )

    parser.add_argument(
        "coords", type=float, nargs="+", help="input point coordinates (x0 y0 x1 y1...)"
    )

    parser.add_argument(
        "--xylim",
        nargs="+",
        help="xlim, ylim for plot (default: deduce from coordinates)",
        default="polygon",
    )

    parser.add_argument(
        "--show-axes",
        "-a",
        action="store_true",
        help="show coordinate axes (default: false)",
        default=False,
    )

    parser.add_argument(
        "--output-file",
        "-o",
        type=str,
        help="output file (default: none, show on screen)",
        default=None,
    )

    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version="%(prog)s {}, Python {}".format(__version__, sys.version),
        help="display version information",
    )
    return parser
