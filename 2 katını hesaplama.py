#iki katını alma fonksiyonu
def x2(sayı):
    çarpım = sayı*2
    return çarpım

#çarpma işlemi yapan fonksiyon

def çarpıcı(s1,s2):
    çarpma = s1*s2
    return çarpma


#iki katını alma fonksiyonu kullanımı
sayı = int(input("bir sayı girin"))

a = x2(sayı)
print(a)

#çarpma fonksiyonu kullanımı
sayı = int(input("bir sayı girin"))
sayı1 = int(input("bir sayı daha girin"))

f = çarpıcı(sayı, sayı1)
print(f)
