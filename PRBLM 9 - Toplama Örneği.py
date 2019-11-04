# bir fonksiyon yazılacak. Kendisine gelen parametreyi alarak, bu sayıya kadar olan tüm sayıların
# toplamını bulacak ve geri gönderecek.
# Bu fonksiyonu kullanarak, kullanıcının girdiği sayıya kadar tüm sayıların toplamını veren program yazılacak
# 2 ye kadar olan sayıların toplamı = ..
# 3 e kadar olan sayıların toplamı = ..
# ....



def toplambul(hedef):
    toplam = 0
    sayac = 0
    while True:
        if(sayac == hedef):
            break
        sayac = sayac +1
        toplam = toplam +sayac
    return toplam


sayı = int(input("istediğiniz bir sayı girin"))
for sıradaki in range(1,sayı + 1):
    sonuc = toplambul(sıradaki)
    print("{} sayısına kadar olan sayıların toplamı = {}".format(sıradaki,sonuc))

