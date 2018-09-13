# Kullanıcıdan bir kelime istesin
# Bir de yasaklı harfler listesi olsun.
# Girilen kelimede yasaklı bir harf varsa, kullanıcıyı uyarıp yeni kelime istesin.
# "çıkış" girilirse program bitsin.
# Girilen kelimenin harf uzunluğunu ölçüp söylesin. Fonksiyon = len()
# Sonra da, girilen kelilmeyi şu şkeilde ekrana yazsın.
# K * E * L * İ * M * E

yasakli_harfler = "d_t_g_p_s_z_b"

while True:
    kelime = input("bir kelime girin")

    if (kelime == "çıkış"):
        quit()

    for harf in kelime:
        if(harf in yasakli_harfler):
            print("yasaklı harf girdiniz,yasaklı harfler şunlar: {}".format(yasakli_harfler))
            kelime =""
            break

    if (kelime != ""):
        break

harf_sayısı = len(kelime)

print("{} kelimesi {}  harf uzunluğunda".format(kelime, harf_sayısı))


sayac = 0
yenikelime = ""

for harf in kelime:
    sayac = sayac +1
    yenikelime = yenikelime + harf

#harf sayısı sayaça eşitse yıldız eklesin
    if(sayac!= harf_sayısı):
        yenikelime = yenikelime + " * "

print(yenikelime)














