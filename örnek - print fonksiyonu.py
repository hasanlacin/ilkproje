

isim = input("Adınızı girin ")
yil = int(input("Dogum yılı"))

yas= 2018 - yil

buyil = 2018

print("merhaba %s, sen %d yaşındasın" %(isim,  yas))

print("merhaba {}, sen {} yaşındasın".format(isim,yas))

print("merhaba {0}, yıl olmuş {2}, sen {1} yaşındasın. "
      "{1} yaşına gelene kadar çok uğraştın mı? ".format(isim, yas, buyil))

print("merhaba {:s}, sen {:d} yaşındasın".format(isim,yas))



#bir metnin içinde değişkenler yapmak
metin = """Arada kullanacağım {ornek} isimli bir değişken yaptım. Bu {ornek} adlı değişkeni 
metnin içinde isteğiğim kadar kullanıyorum. Her yerde {ornek} olarak geçecek.
"""
print(metin.format(ornek="BERAT"))

