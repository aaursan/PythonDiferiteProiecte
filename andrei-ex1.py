class Caine:
    def __init__(self,nume,varsta):
        self.nume=nume
        self.varsta=varsta
    def Prezentare(self):
        print("Cainele are " , self.nume, self.varsta)
    def Sunet(self,latra):
        self.latra=latra
        print("cainele face " , self.nume,self.latra)


class Ciobanesc(Caine):
    def Viteza(self,viteza):
        self.viteza=viteza
        print(" Cainele Ciobanesc alearga cu o viteza de ", self.nume, self.viteza)

class ChowChow(Caine):
    def Viteza(self,viteza):
        self.viteza=viteza
        print("Cainele chowchow alearga cu o viteza de " ,self.nume, self.viteza)

a=Caine("ion" , 3)
a.Prezentare()
a.Sunet("ham")
b=Ciobanesc("Dora", "10")
b=ChowChow("Kube","3")
b.Viteza("8")