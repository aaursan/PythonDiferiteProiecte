class Melodii(object):
    def __init__(self,nume_melodii):
        self.nume_melodii=nume_melodii
    def amestec(self):
        import random
        random.shuffle(self.nume_melodii)
        return self.nume_melodii
lista_melodi=Melodii(['andra','maria','ioana'])
print(lista_melodi.amestec())