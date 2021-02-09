# #exercitiul 1 3 clase 2 metode
# class Vodafone:
#     def __int__(self,nr_ang,salarii):#am pus 2 metode
#         self.nr=nr_ang
#         self.salrii=salarii
#     def show(self):
#         print("nr de angajatii ai firmei:"+ str(self.nr))
#     def calcul(self):#metoda calcul
#         print("banii cheltuiti ptr angajati:" + str(self.nr*self.salrii))
# class Telacad:
#     def __int__(self, nr_ang, salarii):  # am pus 2 metode
#         self.nr = nr_ang
#         self.salrii = salarii
#     def show(self):
#         print("Firma telacad ofera cursuri prin cei:" + str(self.nr)+ "angajati")
#     def calcul(self):  # metoda calcul
#         print("banii cheltuiti ptr angajati:" + str(self.nr * self.salrii))
# class Orange:
#     def __int__(self, nr_ang, salarii):  # am pus 2 metode
#         self.nr = nr_ang
#         self.salrii = salarii
#     def show(self):
#         print("nu oferim internet ptr ca avem:" + str(self.nr) + "angajati")
#     def calcul(self):  # metoda calcul
#         print("banii pe care nu-i chelyuieste firma orangecheltuiti ptr angajati:" + str(self.nr * self.salrii))
#     #creez metoda acu
# def apel_functie(obiect):
#     obiect.show()
#     obiect.calcul()
#     print("------")
# def apel_func(lista):
#     for i in lista:
#         i.show()
#         i.calcul()
#         print("------")
# #lista=[]
# #declarare obiecte
# comp1=Vodafone(500,1500)
# comp2=Telacad(20,1000)
# comp3=Orange(2,3)
# #apelez functie obiecte si calsa
# #metoda 1 de apelare a functiei
# apel_functie(comp1)
# apel_functie(comp2)
# apel_functie(comp3)
# #metoda 2 de apelare a functiei
# lista.append(comp1)
# lista.append(comp2)
# lista.append(comp3)
class Vodafone:
    def __init__(self,nr_ang,salarii):
        self.nr=nr_ang
        self.salarii=salarii
    def show(self):
        print("Numarul de angajati ai firmei: "+str(self.nr))
    def calcul(self):
        print("Banii pe care ii cheltuieste aceasta "
              "firma pe iubitii sai angajati ieie: "
              ""+str(self.nr*self.salarii))

class Telacad:
    def __init__(self,nr_ang,salarii):
        self.nr=nr_ang
        self.salarii=salarii
    def show(self):
        print("Firma Telacad ofera cursuri prin cei "+str(self.nr)+""
        " angajati")
    def calcul(self):
        print("Banii pe care ii cheltuieste firma Telacad pe iubitii sai angajati ieie: "+str(self.nr*self.salarii))

class Orange:
    def __init__(self,nr_ang,salarii):
        self.nr=nr_ang
        self.salarii=salarii
    def show(self):
        print("Nu oferim internet pentru ca avem "+str(self.nr)+" angajati")
    def calcul(self):
        print("Banii pe care nu ii cheltuieste firma Orange pe iubitii sai angajati ieie: "+str(self.nr*self.salarii))


def apel_functie(obiect):
    obiect.show()
    obiect.calcul()
    print("----")

def apel_func(lista):
    for i in lista:
        i.show()
        i.calcul()
        print("----")

lista=[]

comp1=Vodafone(500,15000)
comp2=Telacad(20,1000)
comp3=Orange(2,3)

lista.append(comp1)
lista.append(comp2)
lista.append(comp3)
#
# apel_functie(comp1)
# apel_functie(comp2)
# apel_functie(comp3)

apel_func(lista)

