all: clean build install test

build:
	python setup.py build

dist:
	python setup.py bdist

install:
	python setup.py install -f

test:
	python -m unittest -v tests.test

pypi: clean build dist

clean:
	rm -rf build dist pycompat.egg-info