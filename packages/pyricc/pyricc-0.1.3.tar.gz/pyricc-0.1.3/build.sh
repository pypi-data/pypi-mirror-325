#!/bin/bash

#. .venv/bin/activate

# yellow "1. git taggin with current VERSION.."
# echodo git tag "v$(cat VERSION)"
# git push --tags

#pip install --upgrade build twine
pip install --upgrade pip setuptools setuptools_scm[toml] build twine # upgrade essential tools and install build and twine
#pip install --upgrade build twine setuptools-scm
#python -m build
yellow "2. build with Mad the Twine.."

python -m build -v
#python -m build --wheel
#python -m build --sdist

# Successfully built pyric-0.1.0.tar.gz and pyric-0.1.0-py3-none-any.whl
