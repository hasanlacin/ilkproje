liste = []
sayac = 0

sayı = int(input("bir sayı giriniz"))
while True:
    sayac = sayac + 1
    if(sayı%sayac == 0):
        liste.append(sayac)
        if(sayı == sayac):
            break
print("girdiğiniz sayının çarpanları :{}".format(liste))