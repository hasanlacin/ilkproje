
while True:
    cevap = input("ne haber?")
    print(cevap)

#döngüyü başa çevirelim
    if(cevap=="k"):
        continue

    print("k girilmemiş, başka bişey girilmiş")

#döngüyü bitirme
    if (cevap=="q"):
        break

    print("q da girilmemiş")


#for döngüsü ve range konusu
#değişkendeki her bir harfi ayrı ayrı yazar
bir_isim = "hasan laçin"
for harf in bir_isim:
    print(harf)

#bir kelimede harf kontrolü yapmak
türkçeharfler="çğıİöüş"
parola = input("parolanızı girin")
for karakter in parola:
    if(karakter in türkçeharfler):
        print("parolada türkçe harfler kullanılamaz")


#belli bir sayıda döngü çevirmek
for numara in range(1,5):
    print(numara)

#ikişer ikişer ilerlemek
for numara in range(1,10,2):
    print(numara)

#geriye doğru saydırıp ilerlemek
for numara in range (10,0,-1):
    print(numara)


#iki metni karşılaştır, ilkinde olup ta ikincide olmayanları bul
ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"

print ("ilk metinde olup ta ikincide olmayanlar şunlardır:")
for s in ilk_metin:
    if not s in ikinci_metin:
        print(s)



#karakter sayma
metin= """Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı
tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan,
isminin Python olmasına aldanarak, bu programlama dilinin, adını piton
yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu programlama
dilinin adı piton yılanından gelmez. Guido Van Rossum bu programlama dilini,
The Monty Python adlı bir İngiliz komedi grubunun, Monty Python’s Flying
Circus adlı gösterisinden esinlenerek adlandırmıştır. Ancak her ne kadar
gerçek böyle olsa da, Python programlama dilinin pek çok yerde bir yılan
figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır."""

harf = input("hangi harfi sayayım")

sayı=''

for s in metin:
    if harf==s:
        sayı += harf

#yazdırmanın eski yöntemi
print ("%s karakteri %d adet var" %(harf, len(sayı)))

#yazdırmanın yeni yöntemi
print("{} karakteri {} adet var".format(harf, len(sayı)))

