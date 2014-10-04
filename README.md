pycompat [![Build Status](https://travis-ci.org/alexandrevicenzi/pycompat.svg?branch=master)](https://travis-ci.org/alexandrevicenzi/pycompat) [![Version](https://pypip.in/version/pycompat/badge.png)](https://pypi.python.org/pypi/pycompat)
========

Library to check Python and System version in a easy way

### Compatibility

Works with all major versions of Python.

Tested on Python 1.5, 2.2, 2.3, 2.4, 2.6, 2.7, 3.0, 3.2, 3.3, 3.4 and PyPy.

### Install

`pip install pycompat`

or

`python setup.py install`

### How to use?

```python
from pycompat import python as py
```

```python
py.is2xx
>>> True
```

```python
py.is27x
>>> True
```

```python
py.is3xx
>>> False
```

```python
py.is_gt(2, 5)
>>> True
```

```python
py.is_lt(3)
>>> True
```

```python
py.is_eq(2, 7, 5)
>>> True
```

```python
py.is_cpython
>>> True
```

```python
py.is_pypy
>>> False
```

```python
from pycompat import system as sys
```

```python
sys.is_64bits
>>> True
```

```python
sys.is_linux
>>> True
```

```python
sys.is_linux2
>>> True
```

```python
sys.is_linux3
>>> False
```

### List of all attributes/methods

```python
# Constants
pycompat.WIN_32
pycompat.CYGWIN
pycompat.LINUX
pycompat.LINUX2
pycompat.LINUX3
pycompat.MAC_OS_X
pycompat.OS2
pycompat.OS2_EMX
pycompat.CPYTHON
pycompat.IRONPYTHON
pycompat.JYTHON
pycompat.PYPY
pycompat.MAX_SIZE

# Python version
pycompat.major
pycompat.minor
pycompat.micro
pycompat.release

# Python info
python.is1xx
python.is10x
python.is15x
python.is16x
python.is2xx
python.is20x
python.is21x
python.is22x
python.is23x
python.is24x
python.is25x
python.is26x
python.is27x
python.is3xx
python.is30x
python.is31x
python.is32x
python.is33x
python.is34x
python.is35x

python.is_pypy
python.is_ironpython
python.is_jython
python.is_cpython

python.is_32bits
python.is_64bits

python.is_gt(2, 7, 5)
python.is_lt(2, 7, 5)
python.is_eq(2, 7, 5)

python.is_alpha
python.is_beta
python.is_candidate
python.is_final

# System info
system.is_windows
system.is_cygwin
system.is_linux
system.is_linux2
system.is_linux3
system.is_mac_os

system.is_32bits
system.is_64bits
```

### Want more?

Feel free to request more functions or contribute in this project.
