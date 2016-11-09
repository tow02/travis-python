#!/bin/bash

for py_file in $(find tests/ -name *.py)
do
  pytest $py_file
done
