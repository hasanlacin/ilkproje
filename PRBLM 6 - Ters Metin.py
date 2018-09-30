# Kullanıcıdan bir metin isteyecek ve girilen kelimeyi tersine çevirerek ekrana yazdıracak program
# "Girdiğiniz metnin tersi : ..... "
# str bir metnin tersini veren bir fonksiyon yazılacak ve programda bu fonksiyon kullanılacak
# ipucu : her string değişken aynı zamanda harflerden oluşan bir listedir.
# yaptıktan sonra da şu yönteme bak. print(girilenmetin[::-1])


def Tersecevir(isim):
    ters = ""
    x = len(isim)
    x = x -1
    while True:
        ters =ters + isim[x]
        if(x == 0):
            break
        x = x -1
    return ters

a = input("isim giriniz")

isim = Tersecevir(a)

print(isim)








