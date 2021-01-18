import numpy as np
from sympy import *
import sympy as sp
import matplotlib.pyplot as plt

def indef_integ(): # l'code principalement follows l'code fonction d'dérivée
    int_function = input("pls provide an equation: ")
    integ_with_respect = Symbol(input("what variable do you want to integrate with respect to? "))
    integ = sp.integrate(int_function, integ_with_respect) #sympy already has l'integration in it
    stringed = str(integ)
    lower_bound = float(input("graph lower bound of the graph: "))
    upper_bound = float(input("graph upper bound of the graph: "))

    x = np.linspace(lower_bound, upper_bound, 100)
    why = eval(stringed)
    plt.plot(x, why)
    plt.show()
    print("∫ f(",str(integ_with_respect),")"+ "d" +str(integ_with_respect) + "=" ,stringed, "+C"  )

    #TODO: cannot do multivariate, for now only can do with respect to due to numpy.