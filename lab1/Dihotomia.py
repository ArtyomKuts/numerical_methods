#4.1151331093937
#0.524293807692839
#3*x**4-8*x**3-18*x**2+2
#2*math.exp(x)+5*x-6
import math
a=float(input("Введите левую границу отрезка: "))
b=float(input("Введите правую границу отрезка: "))
eps=float(input("Введите точность: "))
def func(x):
    return 3*x**4-8*x**3-18*x**2+2
fa=func(a)
def dihotomia(a,b,eps):
    it=0
    while abs(b-a)>eps:
        it=it+1
        c=(a+b)/2
        if fa*func(c)<0:
            b=c
        else:
            a=c
    return c,func(c),it,abs(c-4.1151331093937)
print(dihotomia(a,b,eps))