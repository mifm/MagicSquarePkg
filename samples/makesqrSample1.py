#!/usr/bin/env python
"""
Sample script that uses the MagicSquarePkg package created using
MATLAB Compiler SDK.

Refer to the MATLAB Compiler SDK documentation for more information.
"""

from __future__ import print_function
import MagicSquarePkg
import matlab

my_MagicSquarePkg = MagicSquarePkg.initialize()

xIn = matlab.double([5], size=(1, 1))
yOut = my_MagicSquarePkg.makesqr(xIn)
print(yOut, sep='\\n')

my_MagicSquarePkg.terminate()
