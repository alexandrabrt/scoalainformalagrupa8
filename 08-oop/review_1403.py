class ClasaMea:

    gamma = 0  # variabila de clasa

    def __init__(self):  # constructor
        self.alpha = 1  # variabila de instance
        self.__delta = 3  # variabila de instance privata


obj = ClasaMea()  # instantiere a clase ClasaMew
obj.beta = 2  # variabila de instanta si poate exista doar in interiorul obj
print(obj.__dict__)
print(obj.alpha)
print(obj.gamma) # sau
print(ClasaMea.gamma)
print(obj._ClasaMea__delta)
