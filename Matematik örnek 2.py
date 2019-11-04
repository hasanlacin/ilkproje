# 1 ile X arasında , Y ile tam bölünebilen kaç sayı vardır?
# kullanıcıdan iki sayı alacak. birincisi X olsun, ikincisi Y olsun. (Kaça bölünenleri istiyorsun x, kaça kadar sayayım y)
# Sonucu da şöyle yazsın : "1 ile X arasında, Y ile tam bölünebilen ... adet sayı vardır. Listesini görmek ister misiniz? (E/H)."
# E derse bulduğu sayıları yazsın, H derse program bitsin.
# ipucu : bulunan sayılar bir önceden boş olan bir listeye atılacak

liste = []
bölen = int(input("kaça bölünenleri istiyorsun"))
hedefsayı = int(input("kaça kadar sayayım"))

sayac = 0
for sıradaki in range(1,hedefsayı + 1):
    if(sıradaki%bölen==0):
        sayac = sayac +1
        liste.append(sıradaki)

print("1 ile {} arasında {} ile bölünebilen {} sayı vardır".format(hedefsayı,bölen,sayac))

if(sayac > 0):

    x = input("listesini görmek ister misiniz(E/H)")
    if(x.upper() == 'E'):
        for eleman in liste:
            print(eleman)

    elif(x.upper() == 'H'):
        quit()
    else:
        print("ne diyorsun")