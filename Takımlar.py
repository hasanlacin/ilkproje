# program bir menü gösterecek.
# 1 - Bilgi Gir
# 2 - Bilgileri Listele
# 3 - Çıkış
# Seçiminizi giriniz :
# ----------------------------------------------------------
#  Bilgi Gir Kısmı
# İsim Giriniz diyerek ismi alacak, Takımını giriniz diyerek takım bilgisini alacak.
# Ve aldığı bilgiyi bir "dictionary" sözlüğe kaydedecek. Sonra yine ana menüyü gösterecek.
#  Bilgileri Listele Kısmı
# Sözlüğümüzdeki her bir satırı şu şekilde ekrana basacak :
#  KİŞİ ADI ---> TUTTUĞU TAKIM
#  Sonra yine ana menüyü gösterecek
# 3 girilise, bir isim isteyecek ve girilen kişinin takımını bulup ekrana yazdıracak. 
# 4 girilirse program biter.

Takımisim = {}

def bilgigirme():
    isim = input("isminizi girin")
    takım = input("takımınızı girin")
    Takımisim[isim] = takım

def bilgilisteleme():
    print("İSİM         TAKIM")
    print("------------------")
    for sıradaki in Takımisim:
        print("{} ---> {}".format(sıradaki,Takımisim[sıradaki]))

def arama():
    a = input("kimin takımını öğrenmek istersiniz")
    if(a in Takımisim):
        print("{} adlı kişinin tuttuğu takım = {}".format(a,Takımisim[a]))
    else:
        print("Aradığınız kişi bulunamadı")


while True:
    print("\n")
    print("1 - Bilgi Gir")
    print("2 - Bilgileri Listele")
    print("3 - Takım Arama")
    print("4 - Çıkış")
    print("\n")

    seçim = int(input("seçiminizi giriniz"))
    if(seçim == 1):
        bilgigirme()
    elif(seçim == 2):
        bilgilisteleme()
    elif(seçim == 3):
        arama()

    elif(seçim == 4):
        quit()
    else:
        print("Tanımsız numara girdiniz")