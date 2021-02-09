#mai intai construim o calsa
#MAI INTAI CREEZ FISER TEXT PLUS SCRIERE IN Ellipsis
#METODA DE CITIRE DIN FISIER
#ARHVARE FISIER
#DEARHIVARE FISIER
import gzip
class arhivare:
    def __init__(self,name):
        self.name=name
        self.nume_arhiv=name+'.gz'
        self.a=''
    def scrierefisier(self,content):
        with open(self.name,'w') as file:
            file.write(content)

    def citirefisier(self):
        with open(self.name, 'rt') as file:
            print(file.readline())
            a=file.readline()

    def arhivarefisier(self):
        with gzip.open(self.name, nume_arhiv, 'wt') as file:
            file.write(self.a)

    def dezarhivarefisier(self):
        with gzip.open(self.name, nume_arhiv, 'rt') as file:
            print(file.readline())
nume='fisier1.txt'
obje=arhivare(nume)
content="am scris o linie"
obj.scrierefisier(content)
obj.citirefisier()
obj.arhivarefisier()
obj.dezarhivarefisier()
