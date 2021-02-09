#recapitulare polimorfism
class Caine:
    def sunet(self):
        print("ham ham")
class Pisica:
    def sunet(self):
        print("miau")
def asculta_sunet(tipul_animalului):# astapta obiect tipul animalului
    tipul_animalului.sunet()#
CaineObj=Caine()#dau obiect
PisicaObj=Pisica()

asculta_sunet(CaineObj)
asculta_sunet(PisicaObj)



