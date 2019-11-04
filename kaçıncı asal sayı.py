#kullanıcıdan bir sayı isteyecek. "Kaçıncı asal sayıyı bulmak istiyorsun? (çıkış için 1 giriniz)"
# Daha sonra bu sayı kadar asal sayı bulup döngüden çıkacak.
# "... nci asal sayı = ..." şeklinde mesaj verecek.
# işi bitince tekrar başa dönüp sayı istesin.


from math import sqrt

def Asalsayımı(z):
    asalmı = True

# çift sayıysa asal değildir
    if(z%2== 0):
        return False

    karekök = int(sqrt(z))

#o sayıya kadar her bir sayı için bölünebilme kontrolü yapalım
    for sayac in range(2,karekök + 1):
        if(z%sayac == 0):
            asalmı = False
            break


    return asalmı

sayı = int(input("bir sayı giriniz(çıkmak için 1 e basın)"))

if(sayı == '1'):
    quit()
sayac1 = 0
sayac = 0
while True:
    sayac = sayac + 1

    if(Asalsayımı(sayac)== True):
        sayac1 = sayac1 + 1

    if(sayac1 > sayı or sayac1 == sayı):
        break

print(sayac)

