class masina:
    def __init__(self, name):

        self.name = name


def acceleratie(self):
    raise NotImplementedError("Subclasa trebuie sa-si implementeze metoda abstracta")


def frana(self):
    raise NotImplementedError(" Subclasa trebuie sa-si implementeze metoda abstracta")


class masina_sport(masina):
    def acceleratie(self):

        return 'Masina_sport acceleratie'


def frana(self):
    return 'Masina_sport frana'


class utilaj(masina):
    def acceleratie(self):

        return 'Utilajul acceleratie'

    def frana(self):
        return 'Utilaj frana'

    masini =[utilaj("Trabant”), utilaj('ARO'), masina_sport('R8")]

    for i in masini:
        print( i.name + ': ' + i.acceleratie())