import math
'''

vf = vi + a*t
Δx = ((vi + vf)/2)*t
Δx = vi*t + 1/2 * a* t
vf^2 = vi^2 + 2*a* Δx
'''
missing = input('which information are you missing? (dx, vf, vi, or t) ')
 # vf^2 = vi^2 + 2*a* Δx
if (missing == 't'):
    calculating = input('are you calculating vf, vi, dx or a : ')
    if calculating == 'vf':
        a = int(input('a: '))
        dx = int(input('dx: '))
        vi = int(input('vi: '))
        vf = math.sqrt(vi ^ 2 + 2 * a * dx)
        print((vf))
    elif calculating == 'vi':
        a = int(input('a: '))
        dx = int(input('dx: '))
        vf = int(input('vf: '))
        vi = int()
        vf = math.sqrt(vi ^ 2 + 2 * a * dx)
        print((vi))
    elif calculating == 'dx':
        a = int(input('a: '))
        vi = int(input('vi: '))
        vf = int(input('vf: '))
        dx = ((vf * vf) / (2 * a)) - ((vi * vi) / (2 * a))
        print((dx))
    elif calculating == 'a':
        dx = int(input('dx: '))
        vi = int(input('vi: '))
        vf = int(input('vf: '))
        a = (vf * vf) / (2 * dx) + (vi * vi) / (2 * dx)
        print((a))

# vf = vi + a*t

elif (missing == 'dx'):
    calculating = input('are you calculating vf, vi,a or ,t : ')
    if(calculating == 'vf'):
        vi = int(input('vi: '))
        a = int(input("a: "))
        t = int(input('t: '))
        vf = (vi + (a * t))
        print((vf,2))
    elif calculating == 'vi':
        vi = int(input('vi: '))
        a = int(input("a: "))
        t = int(input('t: '))
        vi = vf - a * t
        print((vi,2))
    elif(calculating == 't'):
        vi = int(input('vi: '))
        vf = int(input("vf: "))
        t = int(input('t: '))
        t = ((vf) / (a)) - ((vi) / (a))
        print((t,2))
    elif(calculating == 'a'):
        vi = int(input('vi: '))
        vf = int(input("vf: "))
        t = int(input('t: '))
        a = ((vf) / t) - ((vi) / t)
        print((a,2))

# Δx = vi*t + 1/2 * a* t *t  
elif (missing == 'vf'):
    calculating = input('are you calculating dx, vi,a or ,t : ')
    if (calculating =="dx"):
            a = int(input('a: '))
            vi = int(input("vi: "))
            t = int(input('t: '))
            dx = (vi * t) + (1 / 2 * a * t)
            print((dx,2))
    elif(calculating == "vi"):
            a = int(input('vi: '))
            dx = int(input("dx: "))
            t = int(input('t: '))
            vi= (dx/t) - ((a*t)/2)  # merci Mssr Preetham d'avoir signalé l'erreur! 
            print((vi,2)) 
    elif calculating == "a":
            vi = int(input('vi: '))
            dx = int(input("dx: "))
            t = int(input('t: '))
            a= (2*dx)/(t*t) - ((2*vi)/t)
            print((a,2)) 
    elif calculating == "t":
        vi = int(input('vi: '))
        dx = int(input("dx: "))
        a = int(input('a: '))
        t= -(vi - math.sqrt(vi*vi + 2* a * x)/a) # I recommend pas ça fonction pour calculating çünkü c'est problematique especially due to «racine carrée»  . 
        print((t,2)) 
            

# Δx = ((vi + vf)/2)*t
elif(missing == 'a'):
    
    calculating = input('are you calculating dx, vi,vf or ,t : ')
    if (calculating == "dx"):
            a = int(input('a: '))
            vi = int(input("vi: "))
            t = int(input('t: '))
            dx= ((vi + vf)/2)*t
            print((dx,2)) 
    elif (calculating == "vi"):
            a = int(input('a: '))
            dx = int(input("dx: "))
            t = int(input('t: '))
            vi= (2*dx)/ (t - vf)
            print((vi)) 
    elif calculating == "vf":
            vi = int(input('vi: '))
            dx = int(input("dx: "))
            t = int(input('t: '))
            vf= (2*dx)/t - vi 
            print((vf,2))
    elif calculating == "t":
            vi = int(input('vi: '))
            dx = int(input("dx: "))
            t = int(input('t: '))
            t= (2*dx) / (vi+vf)
            print((t,2)) 
