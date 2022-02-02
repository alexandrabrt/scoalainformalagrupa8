# print("Mesaj")
# format()
# a = input("Input dat de utilizator")
# def functia_mea():
#     pass

def suma(a: int, b: int = 1, c: int = 0) -> (int, int):
    """
    :param a: first param
    :param b: second param
    :param c: third param
    :return: sum of params, dif of params
    """
    return a + b + c, a - b - c


variabila_1 = 1
variabila_2 = 2
sum, dif = suma(a=variabila_1, c=0, b=variabila_2)
print(sum, type(sum))
print(dif, type(dif))

