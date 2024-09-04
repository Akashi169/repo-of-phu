TAX = 0.1

don_gia = int(input("Nhap don gia: "))
so_luong = int(input("Nhap soLuong: "))

Tien_truoc_thue = don_gia * so_luong
Tien_thue = TAX * Tien_truoc_thue
Tong_tien_sau_thue = Tien_truoc_thue + Tien_thue
#,'*','=',
print('{0:>28}{1:>2} * {2} = {3:>4}'.format('Tong tien truoc thue: ',don_gia,so_luong,Tien_truoc_thue))
print('{0:>28}{1:>16}'.format('Tien thue: ',Tien_thue)) 
print('{0:>28}{1:>17}'.format('Tong tien sau thue: ',Tong_tien_sau_thue))
