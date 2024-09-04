from math import*

a,b,c = map(int,input("nhập a,b,c là: ").split())

tu = -b + sqrt(b*b - 4*a*c)
mau = 2*a

print("Đáp án của biểu thức là: ",tu/mau)