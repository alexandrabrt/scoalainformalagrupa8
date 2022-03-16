# 1. Vehicul
# 1.1. Vehicul de apa
# 1.2. Vehicul de aer
# 1.3. Vehicul de spatiu
# 1.4. Vehicul terestru
# 1.4.1. Vehicul de teren
# 1.4.2. Vehicul de curs
# 1. este super clasa pentru 1.1 -> 1.4.
# 1.1. -> 1.4. este subclasa pentru 1

# 2. Animale
# 2.1. Mamifere
# 2.1.1. Animale salbatice
# 2.1.2. Animale domestice
# 2.2. Reptile
# 2. pentru 2.1. si 2.2. este superclasa
# 2.1. si 2.2. pentru 2. sunt subclase
# 2.1.1. si 2.1.2 pentru 2.1. sunt subclase
# 2.1.1 si 2.1.2 pentru 2 sunt subclase

# Max este un caine mare care doarme toata ziua.
# obiectul -> Max (substantiv)
# clasa -> caine (substantiv)
# proprietatea -> mare (ajectiv)
# activitatea -> doarme toata ziua (verb) -> metoda

# Un Logan verde care merge incet.
# obiect -> Logan
# clasa -> masina
# proprietate -> verde
# activitate -> merge incet


# Lenovo-ul gri se poate cumpara la un pret mai mic de pe un magazin online.
# obiect -> Lenovo
# clasa -> calculator / laptop
# proprietate -> gri
# activate -> se poate cumpara

# Sa se realizeze jocul X&0 intre doi jucatori in care:
# primul jucator este mereu calculatorul
# exista reguli de joc pentru mutari
# obiecte -> calculator / omul
# clasa -> Jocul
# proprietate -> primul jucator este mereu calculatorul
# activitatea -> mutarile / calculul de scor al jocului


# class MyFirstClass:
#     pass
#
#
# my_object = MyFirstClass()
#
# stack = []
#
#
# def push(val):
#     stack.append(val)
#     return stack
#
#
# def pop():
#     val = stack[-1]
#     del stack[-1]
#     return val


# print(push(3))
# print(push(2))
# print(push(1))

# print(pop())
# print(pop())
# print(pop())


# class Stack:
#
#     def __init__(self):
#         self.__stack_list = []
#
#     def push(self, val):
#         self.__stack_list.append(val)
#
#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val
#
#     def __str__(self):
#         return f"{self.__stack_list}"


# obiect_stiva = Stack()
# obiect_stiva.push(3)
# print(obiect_stiva)
# obiect_stiva.push(2)
# print(obiect_stiva)
# obiect_stiva.push(1)
# print(obiect_stiva)
# print(obiect_stiva.pop())
# print(obiect_stiva.pop())
# print(obiect_stiva.pop())

# class ClasaExemplu:
#
#     def __init__(self, val=1):
#         self.first = val
#         self.second = 0
#
#     def set_second(self, val=2):
#         self.second = val
#
#     def __str__(self):
#         return f"{self.first} {self.second}"
#
#
# obiect_1 = ClasaExemplu()
# obiect_2 = ClasaExemplu(2)
# obiect_3 = ClasaExemplu(3)

# print(obiect_1)
# print(obiect_2)
# print(obiect_3.set_second(3))
# print(obiect_3.second)

# class Caine:
#     nr_picioare = 4  # atribut
#
#     def __init__(self, name, vaccin, age=3):
#         self.__nume = name
#         self.__varsta = age
#         self.__vaccinuri = vaccin
#         self.stare = 'tanar'
#         self.cumpara = 'mancare'
#         if self.__varsta == 4:
#             self.stare = 'batran'
#         if self.__varsta != '4':
#             self.cumpara = 'jucarie'
#         # Caine.nr_picioare = 3
#
#     def __str__(self):
#         return f"{self.__nume} - {self.__varsta}"
#
#     def change_name(self, name):
#         self.__nume = name
#         return 'Ceva'
#
#
# obiect_1 = Caine('Rex', age=4, vaccin=10)
# print(type(obiect_1).__name__)
# print(obiect_1.__dict__)
# print(Caine.__dict__)
# print(obiect_1.cumpara)
# print(hasattr(Caine, 'nr_picioare'))
# var2 = obiect_1.__dict__
# print(obiect_1._Caine__nume)
# print(obiect_1.nr_picioare, 'nr picioare')
# print(obiect_1.varsta, 'varsta')
# print(obiect_1.nume, 'nume')
# print(obiect_1.vaccinuri, 'vaccin')

# class Star:
#
#     def __init__(self, nume, galaxie):
#         self.name = nume
#         self.galaxy = galaxie
#
#     def __str__(self):
#         return f"{self.name} este in {self.galaxy}"
#
#
# soare = Star("Soarele", "Calea Lacteei")
# print(soare)

# vehicul
# vehiculdeteren
# vehiculdetractare


class Vehicul:
    pass


class VehiculTeren(Vehicul):
    pass


class VehiculTractare(VehiculTeren):
    pass

# parintii sunt Vehicul pentru VehiculTeren si VehiculTractare (indirect)
# parintii sunt VehiculTeren pentru VehiculTractare
# parintii sunt superclase pentru copii (superclass)
# copiii sunt VehiculTeren si VehiculTractare(indirect) pentru Vehicul
# copilul este VehiculTractare pentru VehiculTeren
# copiii se numesc subclase
# print("Vehicul VehiculTeren VehiculTractare")
# for cls1 in [Vehicul, VehiculTeren, VehiculTractare]:
#     for cls2 in [Vehicul, VehiculTeren, VehiculTractare]:
#         print(issubclass(cls1, cls2), end='\t')
#     print()


# vehicul1 = Vehicul()
# vehicul_teren = VehiculTeren()
# vehicul_tractare = VehiculTractare()
# print(isinstance(vehicul1, VehiculTractare))

# for obj in [vehicul1, vehicul_teren, vehicul_tractare]:
#     for cls in [Vehicul, VehiculTeren, VehiculTractare]:
#         print(isinstance(obj, cls), end='\t')
#     print()

# class Exemplu:
#
#     def __init__(self, val):
#         self.value = val
#
#     def __str__(self):
#         return f"{self.value}"
#
#
# obiect_1 = Exemplu(0)
# print(obiect_1.value, '223')
# obiect_2 = Exemplu(2)
# print(obiect_2.value, '225')
# obiect_3 = obiect_1
# obiect_1.value = 7
# print(obiect_3.value, obiect_1.value, '227')
# obiect_3.value += 1
# a = obiect_1.value
# b = obiect_2.value
# c = obiect_3.value
# print('ddd')



# print(obiect_1 is obiect_2)
# print(obiect_2 is obiect_3)
# print(obiect_3 is obiect_1)
# print(obiect_1.value, obiect_2.value, obiect_3.value)
# string_1 = "Maria are mere "

# string_2 = "www"
# string_2 = string_1

# string_2 = "Maria are mere mari"
# string_1 += "mari"

# print(string_1 == string_2, string_1 is string_2, string_1, string_2)


# class SuperClass:
#
#     supVar = 1
#     variabila_clasa = 6
#
#     def __init__(self, nume):
#         self.name = nume
#         # self.var_1 = 101
#
#     def __str__(self):
#         return f"Numele meu este {self.name}"


# class Clasa3(SuperClass):
#
#     variabila_clasa = 5
#
#     def __init__(self, nume):
#         super().__init__(nume)
#         self.name = nume
#         self.var_2 = 201
#         # self.var_1 = 101
#
#     def prima_metoda(self):
#         return 4

# class SubClass(Clasa3):
#
#     subVar = 2
#     supVar = 3
#
#     def __init__(self, nume):
#         # self.var_1 = 202
#         # print(self.var_1)
#         super().__init__(nume)
#         self.var_3 = 301
#         self.var_1 = 203
#         # self.name = nume
#         # Super.__init__(self, nume)
#
#     def __str__(self):
#         return f"Nume"

# obiect = SubClass("Alexandra")
# print(obiect.subVar)
# print(obiect.supVar)
# print(obiect.variabila_clasa)
# print(obiect.var_3, obiect.var_2, obiect.var_1)
# print(obiect.prima_metoda())
# print(obiect.var_1)


class A:

    def info(self):
        return "Clasa A"


class F:

    def info(self):
        return "Clasa F"


class B(A):

    pass

    # def info(self):
    #     return "Clasa B"


class C(B):

    pass

    # def info(self):
    #     return "Clasa C"


class D(A, C):
    pass


print(D().info())
