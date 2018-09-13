# Kullanıcıdan isimler istesin. Her seferinde "1.ismi girin, 2.ismi girin" şeklinde istesin.
# Kullanıcı "bitti" yazdığı zaman sormayı bıraksın.
# Girilen isimleri bir listeye atacağız.
# Girişler bitince aşağıdakileri sırayla yapsın
# 1 - Önce listede kaç isim olduğunu yazacak. "Toplam, XX adet isim girdiniz"
# 2 - Sonra isimleri sıralayacak. Sıralı haliyle ekrana yazacak. "Girdiğiniz isimlerin sıralı hali şu şekilde:" desin
#     ve ardından her satıra bir isim yazsın
# 3 - Her bir ismin ilk harfini alarak bir kelime oluştursun ve bunu da ekrana yazsın.
#     "Baş harflerden oluşan kelime : XXXXX"
# 4 - Listedeki en uzun  kelimeyi yazsın.
#     "Listedeki en uzun kelime XXXX dir."
#     Bunu yapmak için, önce ilk elemana en uzun diyeceğiz ve en uzun kelime değişkenimiz bu kelime olacak.
#     sonra, listedeki her bir elemanın uzunluğu ile karşılaştırıp, birinciden büyükse en büyük yenisi olacak.
# 5 - Listedeki en kısa kelimeyi de aynı şekilde bulsun ve yazsın
#     "Listedeki en kısa kelime XXXX dir."
# Başarılar dilerim
liste = []
a = 0

while True:
    a = a +1
    isim = input("{}.ismi girin".format(a))
    if(isim =="bitti"):
        break
    liste.append(isim)

isimsayısı = len(liste)
print("listedeki isim sayısı şu kadardır: {}".format(isimsayısı))


print("listedeki isimlerin sıralı hali şu şekildedir :")

liste.sort()

başharfler = ""

for i in range(isimsayısı):
    print(liste[i])

 #   sıradaki = liste[i]
 #   harf = sıradaki[0]
    harf = liste[i][0]
    başharfler = başharfler + harf

print("listedeki isimlerin baş harfleri şu şekildedir {}".format(başharfler))

enuzun = liste[0]
for isim in liste:
    isimuzunluğu = len(isim)
    isimuzunluğu1 = len(enuzun)
    if(isimuzunluğu1<isimuzunluğu):
        enuzun = isim
print("listedeki en uzun isim: {}".format(enuzun))



enkucuk = liste[0]
for isim in liste:
    isimuzunluğu3 = len(isim)
    isimuzunluğu4 = len(enkucuk)
    if(isimuzunluğu3<isimuzunluğu4):
        enkucuk = isim

print("listedeki en kısa isim: {}".format(enkucuk))