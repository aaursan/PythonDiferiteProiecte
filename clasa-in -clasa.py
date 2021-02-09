class Human:
    def __init__(self, name):
        self.name = name  # self.name e enclosing
        self.head = self.Head()  # intro clasa crrez o clasa sub forma unui obiect declarat mai jos Head, unde head e prametrul iar Head e parametru de tip clasa care aicea e oboect
        self.brain=self.Brain()

    class Head:  # Head este de tip clasa ce este o clasa definita in interiorul clasei Human
        def talk(self):
            return ("zii ceva baaaa ...")  # asta emetoda
    class  Brain:
        def think(self):
            return("gandeste-yt bre la ceva")


a = Human("alfred")
print(a.name)

print(a.head.talk())  # prin a obiect pot apela clasa head din clasa Human si obiectul din clasa Head
print(a.brain.think())