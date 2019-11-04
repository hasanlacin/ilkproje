liste = ['pazartesi','salı','çarşamba','perşembe','cuma','cumartesi','pazar']

def günübul(sayı):
    return liste[sayı -1]

sayı = int(input("1 den 7 ye kadar sayı girin"))

gün = günübul(sayı)
print(gün)