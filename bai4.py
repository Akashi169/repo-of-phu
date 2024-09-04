soXe = int(input("Nhập vào số xe của bạn (gồm 5 chữ số): "))
sum = 0

while (soXe > 0):
    sum += soXe % 10
    soXe //= 10
    
print("nút xe của bạn là:", sum % 10) 
    
