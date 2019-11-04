sozluk = {
    'elma':'kırmızı ve yeşil olan bir meyve',
    'masa':'üzerine eşya konan üç veya dört ayaklı alet',
    'bilgisayar':'bilgileri sayan cihaz',
    'telefon': 'uzaktan sesleri ileten cihaz',
    'kalem': 'yazmaya yarayan alet',
    'araba':'bir yerden bir yere gitmeye yarayan dört tekerlekli araç',
    'kitap': 'okunan sayfalar',
    'lamba': 'aydınlatan cihaz',
    'pena': 'bir tür çalgı',
    'kapı': 'dışarı çıkmak veya içeri girmek için açılan şey',
    'Kaplan' : 'bir yayınevi adı',
    'TBMM': 'Türkiyenin meclisi'
}

import json

from difflib import get_close_matches

sozluk = json.load(open("yenisozluk.txt"))


def kelimebulucu(kelime):

    kelime = kelime.lower()

    if(kelime in sozluk):
        return sozluk[kelime]

    elif(kelime.title() in sozluk):
        return sozluk[kelime.title()]

    elif(kelime.upper()in sozluk):
        return sozluk[kelime.upper()]

    else:
        enyakınlar = get_close_matches(kelime,sozluk.keys())
        if(len(enyakınlar)> 0):
            tahmin = enyakınlar[0]
            soru = input(" Bunu mu demek istediniz : {} (e/h)".format(tahmin))
            if(soru == "e"):
                return sozluk[tahmin]
            elif(soru == "h"):
                return "**işlem iptal edildi**"
            else:
                return "**ne dediğiniz anlaşılamadı**"
        else:
            return "**kelime bulunamadı**"
print("çıkmak isterseniz 'q' ya basın")
while True:
    kelime =input("aramak istediğiniz kelimeyi girin")
    if(kelime  == "q"):
        quit()

    d = kelimebulucu(kelime)

    if(type(d)== list):

        for anlam in d:
            print("-", anlam)

    else:
        print(d)




