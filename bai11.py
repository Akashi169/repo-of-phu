n = int(input("Nhập bảng cửu chương cần tìm: "))
print("Bảng cửu chương của ", n, " là:")

tich = 1

for i in range(1, 11):
    tich = n * i
    print(n, "x", i, "=", tich)