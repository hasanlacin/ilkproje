#asal sayı olup olmadığını bulan bir fonksiyon yazılacak. Bu fonksiyon kullanılarak iki aralıktaki asal sayılar bulunacak.
# fonksiyonun mümkün olan en hızlı şekilde çalışması sağlanacak.
# örneğin çift sayılar için bölünebilme kontrlüne gerek yok.
# 1 ile 100bin arası sayılar için;
# ilk halinde :106 saniye
# çift sayı atlatınca :57 saniye
# kareköke kadar kontrol de ekleyince:1 saniye
from math import sqrt

def Asalsayımı(z):
    asalmı = True

# çift sayıysa asal değildir
    if(z%2== 0):
        return False

    karekök = int(sqrt(z))

#o sayıya kadar her bir sayı için bölünebilme kontrolü yapalım
    for sayac in range(2,karekök + 1):
        if(z%sayac == 0):
            asalmı = False
            break


    return asalmı

sayac =0



sayı = int(input("başlangış sayısını giriniz"))
sayı1 = int(input("bitiş sayısını giriniz"))
asallar=[]

for w in range(sayı,sayı1 + 1):

    if(Asalsayımı(w) == True):
        sayac = sayac + 1
        asallar.append(w)

print("toplam {} adet asal sayı vardır".format(sayac))

cevap = input("Yazdırmamı ister misin? E/H : ")
if(cevap.upper()=='E'):
    for x in asallar:
        print (x)


