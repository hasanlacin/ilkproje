

def Asalsayımı(hedefsayı):
    asalmı = True

    for sayac in range(2,hedefsayı):
        if(hedefsayı%sayac == 0):
            asalmı = False
            break


    return asalmı


sayı = int(input("bir sayı giriniz"))


#sayı asal değil ise : "sayı asal değildir, çarpanları = ...... " desin
if(sayı == 1):
    print("girilen sayı asal değil")
    quit()
if(Asalsayımı(sayı) == True):
    print("girilen sayı asal")

else:
    print("girilen sayı asal değil")
