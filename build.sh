#!/usr/bin/env bash
echo "Building Python package"
cd package
python3 -m build
cd dist
pip install --force-reinstall *.whl
echo "Package built and installed"