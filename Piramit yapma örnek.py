"""
 bir sayı isteyecek (2 ile 20 arasında)
birden o sayıya kadar ekrana şu şekilde yazacak

ipucu : print yapıldığında sonraki satıra geçmemesi için şu şekilde kullanılır
print(yazılacakşey, end=" ")

önce değişkeni oluştur. bitince satırı yaz.


1
22
333
4444
55555
......
"""

sayı = int(input("Bir sayı girin"))

for i in range(0,sayı):
    kelime = ""
    for a in range(0,i + 1):
        kelime = kelime + str(i + 1)
    print(kelime)
