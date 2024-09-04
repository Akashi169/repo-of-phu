from math import*

x1 = pi
x2 = pi/2
x3 = 4*pi/3

def check(x):
    return sin(x)** 2 + cos(x)**2 == 1

if (check(x1)):
    print("với x = π thì biểu thức sin(x)**2 + cos(x)**2 == 1 là đúng")
else:
    print("với x = π thì biểu thức sin(x)**2 + cos(x)**2 == 1 là sai")

if(check(x2)):
    print("với x = π/2 thì biểu thức sin(x)**2 + cos(x)**2 == 1 là đúng")
else:
    print("với x = π/2 thì biểu thức sin(x)**2 + cos(x)**2 == 1 là sai")

if(check(x3)):
    print("với x = 4π/3 thì biểu thức sin(x)**2 + cos(x)**2 == 1 là đúng")
else:
    print("với x = 4π/3 thì biểu thức sin(x)**2 + cos(x)**2 == 1 là sai")

