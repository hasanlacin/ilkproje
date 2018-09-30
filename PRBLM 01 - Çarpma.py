# sadece toplama işareti kullanarak girilen iki sayıyı çarpacak program
carpan = int(input("1.Sayı giriniz"))

while True:
    sayac = int(input("2.Sayıyı giriniz"))
    if(sayac<100):
        break
    else:
        print(" sayı 100 den küçük olmalı")


toplam = 0

while sayac >0:
    toplam = toplam+carpan
    sayac = sayac-1
    #print('şu anda toplam=%d sayac=%d' %(toplam,sayac))

print("sayıların çarpımı =",toplam)