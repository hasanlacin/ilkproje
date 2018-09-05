isim=input("adınız ne")
gun = "perşembe"

print("merhaba %s hosgeldin, bugün %s" %(isim, gun))


for i in range(3):

    soru=input("beni seviyor musun %s?" %isim)

    if(soru=="evet"):
        print("mutlu oldum")
    elif(soru=="hayır"):
        print("üzüldüm")
    else:
        print("ne diyorsun")


