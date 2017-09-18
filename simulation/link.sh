#!/usr/bin/env bash
swig -c++ -python simulation.i
python3 build.py build_ext --inplace