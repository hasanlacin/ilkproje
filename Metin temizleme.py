# girilen bir metinden şu simgeleri temizleyerek, ekrana temiz metni yazacak.
# simgeler :  "{}\-!+%&()?;"
def Temizleyeci(x):
    YeniMetin = ""
    yasaklı_harfler = "{}\-!+%&()?;"

    for harf in x:
        if(harf not in yasaklı_harfler):

            YeniMetin = YeniMetin + harf
    return YeniMetin


metin = input("bir metin giriniz")
a = Temizleyeci(metin)
print(a)