class masina:
    def __init__(self,name):
        self.name=name
    def accelercatie(self):
        raise NotImplementedError("Subclasa trebuie sa implemnetzeze metoda abstracta")
    def Franda(self):
        raise NotImplementedError("Subclasa trebuie sa implemnetzeze metoda abstracta")

class masina_sport(masina):
    def acceleratie(self):
        return"masina_sport acceleratie"
    def frana(self):
        return("masina sport frana")
class utilaj(masina):
    def acceleratie(self):
        return"utilaj accelaetaue"
    def frana(self):
        return"utilaj frana"
masini=[utilaj("trabant"),utilaj("aro"),masina_sport("bmw")]

# for i in masini:
#     print (i.name+ ": " +i.acceleratie())# apelez obectele din lista
for masina in masini:
        print(masina.name + ": " + masina.acceleratie())  # apelez obectele din lista