#innerclasses cu identare

# class Human:
#     def __init__(self,name):
#         self.name=name#self.name e enclosing
#         self.head=self.Head()#intro clasa crrez o clasa sub forma unui obiect declarat mai jos Head, unde head e prametrul iar Head e parametru de tip clasa care aicea e oboect
#     class Head:# Head este de tip clasa ce este o clasa definita in interiorul clasei Human
#        def talk(self):
#           return("zii ceva baaaa ...")#asta emetoda
#
# a=Human("alfred")
# print(a.name)
#
# print(a.head.talk())#prin a obiect pot apela clasa head din clasa Human si obiectul din clasa Head
# if __name__=='__main__'
#     ana=Human()
# print ana.name
# print ana.head.talk()


class Human:


    def __init__(self):
        self.name = 'Guido'
        self.head = self.Head()


class Head:
        def talk(self):
            return 'talking...'


if __name__ == '__main__':
    guido = Human()
print( guido.name)
print (guido.head.talk())
