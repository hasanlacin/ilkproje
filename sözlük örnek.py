rehber = {
    'hasan':'5339532404',
    'zeynep':'5053779383',
    'berat':'5053779382',
    'bayram': '4125522751',
    'fırın': '4125524880'
}

for ad in rehber:
    print("isim = {},telefon = {}".format(ad,rehber[ad]))

while True:
    a = input("isim girin")
    if(a in rehber):
        print("{} isimli kişinin telefon nunarası = {}".format(a,rehber[a]))
 #       quit()
    else:
        print("listede olmayan bir isim girdiniz")

    cevap = input("programdan çıkılsın mı? (çıkmak için E)")
    if(cevap.upper() == "E"):
        break
