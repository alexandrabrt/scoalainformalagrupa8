# Tema4 -staticmethod si mosteniri

class EroarePersonala(Exception):
    def __init__(self, cod, mesaj):
        super(EroarePersonala, self).__init__(str(cod) + "=>" + str(mesaj))


class util():
    total = []

    def __init__(self):
        utilizatori.total.append(self)


class izatori:
    def __init__(self, user, passw):
        self.user = user
        self.passw = passw


class utilizatori(util, izatori):
    def __init__(self, user, passw):
        util.__init__(self)
        izatori.__init__(self, user, passw)

    def __useri(self):
        return set([e.user for e in self.total])

    def __parole(self):
        return set([e.passw for e in self.total])

    @staticmethod
    def __len__():
        raise EroarePersonala(101, "Ai gresit apelarea!")


o1 = utilizatori("cata", "pass")
o2 = utilizatori("ana", "pass")
o3 = utilizatori("stefan", "pass")

print(o1._utilizatori__useri())
print(o1._utilizatori__parole())

try:
    len(o1)
except(Exception) as e:
    print(e)

