import numpy as np
from sympy import *
import sympy as sp


def def_integ():
    int_function = input("pls provide an equation: ")
    integ_with_respect = Symbol(input("what variable do you want to integrate with respect to? "))
    lower = input("lower bound? ")
    upper = input("upper bound? ")
    integ = sp.integrate(int_function, (integ_with_respect, lower, upper))
    print(integ)

#definite does not care about the symbol anyway, we're good.