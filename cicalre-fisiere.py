#problema asta inta la examen, va trebuie sa deschidem fieserele tesxt, facem verifiacre pe fisiere text, le vom adauga in dictionare,,,,with open ptr deschide
import sys
import os

def ciclare(numeDirector):#am creat fctia
    for i in os.listdir(numeDirector):# metoda os imi perimte sa fac listari
        if os.path.isdir(numeDirector+ "/" +i):#daac 2 e deirector
            ciclare(numeDirector+ "/"+i)#reapelez cicalrea
        else: # daca nu ma aflu in directorul respectiv
            print(numeDirector,i)
ciclare(sys.argv[1])# se pune argv1 ptr ca primul fisier cfeeat incepe cu 1 .....si trebuie pus 1 ca sa se numeste primul folder ptr ca asa va afoisa list index out of range
# laedit configuration se va pune la prametrii valoarea 1 pentru a aputea afisa fisierul text si din ce subfisiere vine
#si de aceea vom fi creat fisierele 1 2 7 9 cu text intre fiecare

import sys
import os

def ciclarfe(numedirector):
    for i in os.listdir(numedirector):
        if os.path.isdir(numedirector: "/" +i)
        ciclare(numedirector: "/" +i)
    else:
        print(numedirect)