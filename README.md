# epicycler

[![CircleCI](https://img.shields.io/circleci/project/github/nschloe/epicycler/master.svg)](https://circleci.com/gh/nschloe/epicycler/tree/master)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/epicycler.svg)](https://codecov.io/gh/nschloe/epicycler)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![PyPi Version](https://img.shields.io/pypi/v/epicycler.svg)](https://pypi.org/project/epicycler)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/epicycler.svg?logo=github&label=Stars)](https://github.com/nschloe/epicycler)

![circles](https://nschloe.github.io/epicycler/circles.gif)

[Epicylces](https://en.wikipedia.org/wiki/Deferent_and_epicycle) have been used for
millenia to describe the motion of planets; even
[Copernicus](https://en.wikipedia.org/wiki/Nicolaus_Copernicus) still used them. They
got out of fashion when [Kepler](https://en.wikipedia.org/wiki/Johannes_Kepler)
thought about ellipses, but one can still fool around with epicycles a bit. See
[mathologer's awesome video about it](https://youtu.be/qS4H6PEcCCA) (which in fact
motivated this little package).

### Create animations from polygons

Given a number of 2D polygonal points, epicycler creates nice animations. For example,
the above is created with
```bash
epicycler-poly \
  0.0 0.0 \
  1.0 0.0 \
  1.0 2.0 \
  -0.5 1.1 \
  -0.5 2.1 \
  --xylim -1.5 +2.0 -1.3 3.0
```
See
```bash
epicycler-poly -h
```
for more options.

### Installation

epicycler is [available from the Python Package
Index](https://pypi.org/project/epicycler/), so simply type
```
pip install -U epicycler
```
to install or upgrade.

### Create animations from image files
![seagull](https://nschloe.github.io/epicycler/seagull.png)

Given a (small) linedrawing image file like the above seagull,
epicycler can create an animation from it
```bash
epicycler-image in.png -c 0.5
```
Use the `-c` option for reducing the number of circles by cutting off those smaller than
the given threshold radius; notice then how the polygon points are not followed exactly:

![seagull-gif](https://nschloe.github.io/epicycler/seagull.gif)


### Creating a GIF

```bash
ffmpeg -i out.mp4 -r 10 'frame-%03d.png'
convert -delay 5 -loop 0 frame-*.png out.gif
```

### Testing

To run the epicycler unit tests, check out this repository and type
```
pytest
```

### Distribution

To create a new release

1. bump the `__version__` number,

2. publish to PyPi and GitHub:
    ```
    make publish
    ```

### License

epicycler is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
