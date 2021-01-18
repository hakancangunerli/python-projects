import numpy as np
from sympy import *
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np



def derive():
    der_function = input("pls provide an equation: ")
    with_respect = input("what variable do you want to differentiate with respect to? ")
    derive = sp.diff(der_function, with_respect)
    stringed= str(derive)
    lower_bound = float(input("graph lower bound of the graph: "))
    upper_bound = float(input("graph lower bound of the graph: "))

    # x = np.linspace(lower_bound, upper_bound, 100)
    # y= eval(stringed)
    # plt.plot(x, y)
    # plt.show()
    print("d/d"+with_respect + "=", stringed)

#TODO we can derive with respect to whatever, but the issue is that NUMPY cannot graph according to ANY variable. if you comment out line 14-20 code works flawlessly.