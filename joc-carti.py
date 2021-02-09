import random
class Carte:
    def __init__(self,valoare,suita):
        self.suita=suita
        self.valoare=valoare
    def show(self):
        print("{} de {}".format(self.valoare,self.suita))
#a=carte(7,"inima rosie")
#a.show

class Pachet:
    def __init__(self):
        self.carti=[]# se pune o lista goala in init ptr a se construii imediat
        self.build()
    def build(self):
         for i in ["inima rosie","inima neagra", "romb","trefla"]:#i=suita
             for j in range(2,15):#j=valoare
                 self.carti.append(Carte(j,i))
                # in lista carti fac append de obiecte Carte

    def show(self):
        for i in self.carti:
            i.show()
            #print(i) ----metoda gresita si ar fi aratat obiectul
#a=Pachet()-metoda cu print(i) si e gresita
#a.show()-metoda cu print(i) si e gresita
    def shuffle(self):
        #r=random.shuffle(0,15)# aicea e gresit ptr ca random.shuffle nu s eface inainte de for
        for i in range(len(self.carti)-1,0,-1):
            r = random.randint(0,i)
            #print(r)
            self.carti[i],self.carti[r]=self.carti[r],self.carti[i]

    def draw(self):
        return self.carti.pop()# fcatia pop pe o lista va scote ultima variabila in cazu nostru ultima carte

class Jucator:
     def __init__(self,nume):
         self.nume=nume
         self.mana=[]

     def TrageCarte(self,pachet):
         self.mana.append(pachet.draw())

     def ShowHand(self):
         for i in self.mana:
             i.show()
     def discard(self):
         if len(self.mana)!=0:
             x=len(self.mana)
             a=self.mana[x-1]
             self.mana.pop()
             return self.mana.pop()
         else:
             pass
     # def amesteca(self,val):
     #     self.mana.append(val)
     #     for i in range(len(self.mana) - 1, 0, -1):
     #         r = random.randint(0, i)
     #         # print(r)
     #         self.mana[i], self.mana[r] = self.mana[r], self.mana[i]





a=Pachet()
#a.show()
a.shuffle()
#print("-----")
#a.show()
#print("-------")
juc1=Jucator("Aurel")
juc2=Jucator("Jiji")
for i in range(0,26):
    juc1.TrageCarte(a)
#juc1.ShowHand()
print("-----")
for i in range(0,26):
    juc2.TrageCarte(a)
# print(juc1.discard())
# print(juc2.discard())
#juc2.ShowHand()
#juc1.TrageCarte(a)
#juc1.ShowHand()
# #print(len(a.carti))
# a.show()
# lista1=[]
# for i in range(0,52):
#     lista1.append(a.draw())#draw e metoda
# print(a.draw())
k=0#contori de monitrizare
l=0#contori de monitorizare
juc1.ShowHand()
print("-----")
juc2.ShowHand()
print("------")
lista1=[]
lista2=[]
while len(juc1.mana)!=0 and len(juc2.mana)!=0: #for i in range(0,26):
    d=juc1.discard()
    e=juc2.discard()
    if d==e:
        juc1.amesteca(d)
        juc2.amesteca(e)

    # if juc1.discard()==juc2.discard():
    #     continue

    if d>e:
        k+=1
    else:
        l+=1


    # if juc1.discard()>=juc2.discard():
    #     k+=1
    # else:
    #     l+=1
#random.shuffle(lista1)
#random.shuflle(lista2)
print(k)
print(l)

