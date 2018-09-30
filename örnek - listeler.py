t1 = ['kasar', 'tulum', 'orgu', 'tulum']
t2 = ['a', 'b']

#t1 listesini ekrana yazar
print(t1)

#t1 listesinin sonuna elma adlı bir eleman ekler
t1.append("elma")
print (t1)

#t1 listesinin eleman sayısını yazar
elemansayısı = len(t1)
print("listenin eleman sayısı = {} adettir".format(elemansayısı))

#listedeki elemanları tek tek yazdırır
sayac=0
for kelime in range(elemansayısı):
    print(t1[sayac])
    sayac = sayac + 1


#t1 listesinin sıfırıncı elamanını "peynir" olarak değiştirir
t1[0] = "peynir"
print (t1)

#listenin belli bir kısmını alır
print (t1[1:3])

#listede "tulum" elemanı kaç tane var
adet = t1.count("tulum")
print("listede %d adet 'tulum' kelimesi var" %adet)

#t1 listesi ile t2 listesini birleştirir
t1.extend(t2)
print (t1)


#t1 listesi sıralayarak yeni bir diziye at. t1 dizisi eski haliyle kalır.
sıralıDizi = sorted(t1)
print(sıralıDizi)

#t1 listesini küçükten büyüğe sıralar
t1.sort()
print(t1)

#t1 listesini büyükten küçüğe sıralar
t1.sort(reverse=True)
print(t1)

#t1 listesinden 1 numaralı sıradaki elemanı sil (listelerde numara sıfırdan başlar)
t1.pop(1)
print(t1)

#t1 listesinden "orgu" elemanını sil
t1.remove ('orgu')
print(t1)
