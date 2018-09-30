#  Sayılardan oluşan bir listeyi kontrol ederek, kaç tanesinin tek sayı olduğunu bulan program
# sayının tek olup olmadığını bulan bir fonksiyon yazılarak, programda bu fonksiyon kullanılacak.
# Sayılar kullanıcıdan istenecek. 0 girdiği zaman istemeyi durduracak.
# En sonunda da "girdiğiniz sayılardan XX tanesi tek sayıdır" diyecek.
# ipucu : bir sayının tek olup olmadığını anlamak için 2'ye bölümünün 0 olup olmadığına bakılabilir.

def TekOlanıBul(sayılar):
    tekler = 0

    for sayı in sayılar:
        if(sayı%2 == 0):
            pass
        else:
            tekler = tekler + 1
    return tekler

liste = []

while True:
    sayı = int(input("sayı girin"))
    if(sayı == 0):
        break
    liste.append(sayı)

#print(liste)


tekler = TekOlanıBul(liste)
print("girdiğiniz sayıların {} tanesi tektir".format(tekler))








