
#birinci yöntem, olabilecek hatalara karşı tek tek önlem almak

ilk_sayı = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")
try:
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
except ZeroDivisionError:
    print("Bir sayıyı 0'a bölemezsiniz!")
except ValueError:
    print("Lütfen sadece sayı girin!")


#ikinci yöntem hatalara topluca bir mesaj vermek

ilk_sayı = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")
try:
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
except (ValueError, ZeroDivisionError):
    print("Bir hata oluştu!")

#pythonun verdiği orijinal hata mesajını da göstermek istersek
ilk_sayı = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")
try:
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
except (ValueError, ZeroDivisionError) as hata:
    print("Bir hata oluştu!")
    print("orijinal hata mesajı: ", hata)


#hata olsa da olmasa da mutlaka yapmamız gereken satırlar için finally

ilk_sayı = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")
try:
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
except (ValueError, ZeroDivisionError) as hata:
    print("Bir hata oluştu!")
    print("orijinal hata mesajı: ", hata)
finally:
    print("devam edelim")




