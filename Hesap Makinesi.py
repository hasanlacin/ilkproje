# HESAP MAKİNESİ
# Açılışta bir menü çıkacak
# 1 - TOPLAMA
# 2 - ÇARPMA
# 3 - BÖLME
# 4 - ÇIKARMA
# 5 - KARE ALMA
# 0 - ÇIKMAK İÇİN SIFIR GİRİNİZ
#
# Kullanıcı geçerli bir seçim girerse, ard arda iki sayı isteyecek . (Birinci sayı: ? ) (İkinci sayı:?)
# Ardından girilen sayılarla istenen işlemi yapıp sonucu gösterecek.
#
# Sıfır girilince program bitecek. (Biterken kapanış mesajı versin)
# Geçersiz bir seçenek girilirse de hata mesajı versin.
#

while True:
    print(" 1 - TOPLAMA \n 2 - ÇARPMA \n 3 - BÖLME \n 4 - ÇIKARMA \n 5 - KARE ALMA \n 0 - ÇIKMAK İÇİN")
    secim = int(input("Bir işlem seçiniz"))

    if(secim >5 or secim <0):
        print("Hatalı sayı girdiniz")
        continue

    if(secim== 0):
        print("By By Tekrar Bekleriz :)")
        quit()

    if(secim == 1 or secim == 2 or secim ==3 or secim == 4 ):
        a = int(input("1.Sayınızı girin"))
        b = int(input("2.Sayınızı girin"))

    if(secim== 1):
        cevap = a + b
        print("sonucunuz = {}".format(cevap))
    if(secim== 2):
        cevap = a*b
        print("sonucunuz = {}".format(cevap))
    if(secim== 3):
        cevap = a/b
        print("sonucunuz = {}".format(cevap))
    if(secim== 4):
        cevap = a-b
        print("sonucunuz = {}".format(cevap))
    if(secim== 5):
        ab = int(input("Bir sayı giriniz"))
        cevap = ab*ab
        print("sonucunuz = {}".format(cevap))


