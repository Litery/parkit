#!/usr/bin/env python

"""
setup.py file for SWIG example
"""

from distutils.core import setup, Extension

simulation_module = Extension('_simulation',
                           sources=['simulation_wrap.cxx', 'simulation.cpp'],
                           )

setup(name='simulation',
      version='0.1',
      author="Szymon Litera",
      description="""Simple swig example from docs""",
      ext_modules=[simulation_module],
      py_modules=["simulation"],
      )
