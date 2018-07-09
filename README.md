# epicycler

[![CircleCI](https://img.shields.io/circleci/project/github/nschloe/epicycler/master.svg)](https://circleci.com/gh/nschloe/epicycler/tree/master)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/epicycler.svg)](https://codecov.io/gh/nschloe/epicycler)
[![Codacy grade](https://img.shields.io/codacy/grade/7b33b6a288804ab4b4edd74c896be82a.svg)](https://app.codacy.com/app/nschloe/epicycler/dashboard)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![PyPi Version](https://img.shields.io/pypi/v/epicycler.svg)](https://pypi.org/project/epicycler)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/epicycler.svg?logo=github&label=Stars)](https://github.com/nschloe/epicycler)

![circles](https://nschloe.github.io/epicycler/circles.gif)


### Creating a GIF

```
ffmpeg -i out.mp4 -r 10 'frame-%03d.png'
convert -delay 5 -loop 0 frame-*.png out.gif
```

### Installation

epicycler is [available from the Python Package
Index](https://pypi.org/project/epicycler/), so simply type
```
pip install -U epicycler
```
to install or upgrade.

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
