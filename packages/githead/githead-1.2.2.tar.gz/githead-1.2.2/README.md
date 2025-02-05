# githead

[![PyPI - Python Version](https://shields.monicz.dev/pypi/pyversions/githead)](https://pypi.org/project/githead)
[![Liberapay Patrons](https://shields.monicz.dev/liberapay/patrons/Zaczero?logo=liberapay&label=Patrons)](https://liberapay.com/Zaczero/)
[![GitHub Sponsors](https://shields.monicz.dev/github/sponsors/Zaczero?logo=github&label=Sponsors&color=%23db61a2)](https://github.com/sponsors/Zaczero)

Simple utility for getting the current git commit hash (HEAD).

## Installation

```sh
pip install githead
```

## Basic usage

```py
from githead import githead

githead() # -> 'bca663418428d603eea8243d08a5ded19eb19a34'

# defaults to '.git' directory but can be changed:
githead('path/to/.git')
```
