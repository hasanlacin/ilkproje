#  Kullanıcıdan isimler isteyecek. "son" kelimesi girilene kadar istemeyi sürdürecek.
# "Bir isim giriniz (sonlandırmak için <son> yazınız)" şeklinde istesin.
# Girilen isimler bir diziye atılacak.
# Her bir  kelimenin tersini bularak ekrana yazacak.
# Terse çevirmek için PRBLM 6 programındaki fonksiyon aynen kullanılabilir.
#
# Her bir kelimeyi ayrı satırlara yazacak. Şu şekilde
#     1.kelimenin tersi=.....
#     2.kelimenin tersi=....
#     ......


def tersyaz(d):
    ters = ""
    x = len(d)
    x = x-1
    while True:
        ters = ters + d[x]
        if(x == 0):
            break
        x = x-1
    return ters


liste = []

while True:
    kelime = input("kelime giriniz")
    if(kelime == "son"):
        break
    print("kelime girmeyi sonlandırmak için(son)yazın")
    d = tersyaz(kelime)
    liste.append(d)

uzunluk = len(liste)

sayac = 0
while True:
    kelimeninTersi = liste[sayac]

    sayac = sayac +1

    print("{}. kelimenin tersi = {}".format(sayac,kelimeninTersi))

    if(sayac >= uzunluk):
        break

#Aynı döngüyü for la yaptık
sayac = 0
for kelimeninTersi in liste:
    sayac = sayac + 1
    print("{}. kelimenin tersi = {}".format(sayac, kelimeninTersi))







