n = int(input("Nhập số n có 3 chữ số là: "))
cnt = 0
sum = 0

while (n > 0):
    sum += n % 10
    cnt = cnt + 1
    n //= 10
    
print("Trung bình cộng 3 chữ số là: ",sum/cnt)
    
