
class Nokta():
    x = 0
    y = 0

    def __init__(self,a,b):
        self.x=a
        self.y=b

    def yukariOtele(self,otelemeMiktar):
        self.y = self.y + otelemeMiktar

    def sagaOtele(self,otelemeMiktar):
        self.x = self.x + otelemeMiktar

    def asagıOtele(self,otelemeMiktar):
        self.y = self.y - otelemeMiktar

    def solaOtele(self,otelemeMiktar):
        self.x = self.x - otelemeMiktar

    def Yaz(self):
        print("x = {}, y = {}".format(self.x,self.y))

birinciNokta = Nokta(5,8)



print("mevcut hali")
birinciNokta.Yaz()

print("aşağı 5 öteleyince")
birinciNokta.asagıOtele(5)
birinciNokta.Yaz()

print("sola 9 öteleyince")
birinciNokta.solaOtele(9)
birinciNokta.Yaz()

