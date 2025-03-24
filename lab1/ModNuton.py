#4.115133124
#0.524293807692839
#3*x**4-8*x**3-18*x**2+2
#2*math.exp(x)+5*x-6
import math
a=float(input("Введите левую границу отрезка: "))
b=float(input("Введите правую границу отрезка: "))
eps=float(input("Введите точность: "))
h=0.01
def func(x):
    return 2*math.exp(x)+5*x-6
def diff(x,h):
    return (func(x+h)-func(x))/h
def double_diff(x,h):
    return (diff(x+h,h)-diff(x,h))/h

def Nuton(a,b,eps):
    it=0
    c=0
    e=b
    if func(a)*double_diff(a,h)<0:
        c=a
    elif func(b)*double_diff(b,h)<0:
        c=b
    while 0.5*double_diff(e,h)/diff(e,h)*abs(b-a)>eps:
        it=it+1
        a=c
        c=c-func(c)/diff(e,h)
        b=c
    return c, func(c), it, abs(0.524293807692839-c)
print(Nuton(a,b,eps))



