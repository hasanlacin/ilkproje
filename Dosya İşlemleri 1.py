#sadece okuma kipinde açmak

def DosyayıOku():
    dosya = open("deneme1.txt", "r")
    icindekiler = dosya.read()
    print(icindekiler)
    dosya.close()

#yazma kipinde açmak
dosya = open("deneme1.txt", "w")
dosya.write("baştan yazdım")
dosya.close()

#ekleme kipinde açmak
dosya = open("deneme1.txt", "a")
dosya.write("\nbu da ikinci satır olsun")
dosya.close()


DosyayıOku()

#dosyayı satır satır okumak.
dosya = open("deneme1.txt", "r")
satır = dosya.readline()
print(satır)
satır = dosya.readline()
print(satır)






