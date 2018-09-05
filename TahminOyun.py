# Önce oyuncunun adını ve yaşını alacak.
# yaşı 1-5 arasında ise, oynayamazsın;
# yaşı 5-10 arasında ise tahmin sayısı 1-10 arası olacak,
# yaşı 10 dan büyük ise tahmin sayısı 1-15 arasında olacak
# tahmin edilecek sayı için random kütüphanesini kullan. "from random import randint" (rastgele programında örnek var)
# oyuncunun üç hakkı var. tahmin edilen sayıyı bulmaya çalışacak.
# Bulursa tebrik etsin, bulamazsa tekrar gel desin.

from random import randint


isim = input("isminizi girin")
yas = int(input("yaşınızı girin"))

hak = 3

if(yas<=5):
    print("OYNAYAMAZSIN")
    quit()

if(yas>5 and yas<=10):
    tutulansayi = randint(1,10)
    print("(1 ile 10 arasında tahmin yap)")

if(yas>10):
    tutulansayi = randint(1,15)
    print("(1 ile 15 arasında tahmin yap)")


while True:

    if(hak == 0):
        print("yanlış cevap verdin,oyun bitti tekrar dene")
        quit()

    tahmin = int(input("sayı tahmin et"))

    if(tutulansayi == tahmin):
        print("tebrikler",isim," doğru bildin"),

        quit()
    else:
        print("yanlış bildiniz")
        if(tutulansayi>tahmin):
            print("yüksel")
        if(tutulansayi<tahmin):
            print("biraz in")
        hak =hak-1

        if(hak==0):
           print("cevap:",tutulansayi,"olacaktı")











