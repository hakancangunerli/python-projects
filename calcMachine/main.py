from derive import derive # you can call otra files using from et import
from indefinite import indef_integ
from definite import def_integ

#l'main est l' logique d'l' systeme. it does not do anything itself it just calls diger .py dosyalari.   

which = input("do you want to integrate or derive? ")

if which == "derive":
    derive()
elif which == "integrate":
    how = input('integrate def or indef? ')
    if how == "def":
        def_integ()
    elif how == "indef":
        indef_integ()

else:
    print("quoi the fuck") # c'est ne pas le 'best' systeme pour exception-handling. 

# TODO: this application is not idiot-proof, it can graph indefinite and derivative.

