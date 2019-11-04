
def asalsayımı(ilksayı):
    carpanlar = []

    for sıradaki in range(2,ilksayı):
        if(ilksayı % sıradaki==0):
            carpanlar.append(sıradaki)



    return carpanlar



sayı = int(input("bir sayı giriniz"))

sonuclar = asalsayımı(sayı)

if(len(sonuclar)== 0):
    print("girilen sayı asaldır")

else:
    print("girilen sayı asal değildir, çarpanları şunlardır:")
    for x in sonuclar:
        print(x)