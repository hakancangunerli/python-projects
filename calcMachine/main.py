from derive import derive
from indefinite import indef_integ
from definite import def_integ


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
    print("what the fuck")

# this application is not idiot-proof, it can graph indefinite and derivative.