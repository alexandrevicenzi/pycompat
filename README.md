pycompat [![Build Status](https://travis-ci.org/alexandrevicenzi/pycompat.svg?branch=master)](https://travis-ci.org/alexandrevicenzi/pycompat)
========

Library to check Python and System version in a easy way

### Requirement

- Python 2.3 or above

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
