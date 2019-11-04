# Dikdortgen adında bir sınıf oluşturulacak.
# Sınıfın iki değişken var . en ve boy.
# Sınıfın metodları şunlar :
# AlanBul : dikdörtgenin alanını bulur.
# ÇevreBul : çevresini bulur
# KosegenBul : Köşegeninin uzunluğunu bulur.
#
# Program akışı
# Kullanıcıdan en ve boy isteyecek. Sonra bu en ve boyu kullanarak Dikdortgen sınıfı oluşturacak
# d = Dikdortgen(50,20)
# Ardından dikdörtgenin alanını, çevresini ve köşegenini bulup ekrana yazacak
#
class Dikdörtgen():
    en = 0
    boy = 0

    def __init__(self,a,b):
        self.en = a
        self.boy = b

    def AlanBul(self):
        alan = self.en * self.boy
        return alan

    def ÇevreBul(self):
        çevre = 2*self.en + 2.*self.boy
        return  int(çevre)

    def KöşegenBul(self):
        köşegen = (self.en**2 + self.boy**2)**0.5
        return köşegen

en1 = int(input("Dikdörtgenin enini girin"))
boy1 = int(input("Dikdörtgenin boyunu girin"))

dik1 = Dikdörtgen(en1,boy1)

print("Alanı = {}".format(dik1.AlanBul()))

print("Çevresi = {}".format(dik1.ÇevreBul()))

print("Köşegeni = {}".format(dik1.KöşegenBul()))












