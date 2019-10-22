"""
	ejercicio4
	@drmorales4
# Encontrar la siguiente estructura
#

[(16.333333333333332, 'Ángel'), (16.666666666666668, 'José'), (13.0, 'Ana')]

Dadas las siguientes estructuras:

"""

paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]
nombres = ["Ángel", "José", "Ana"]

funcion1 = lambda x: x[0]
funcion2 = lambda x: x[1]
funcion3 = lambda x: x[2]

funciones = lambda x: ((funcion1(x) + funcion2(x) + funcion3(x))/3) # sumar y sacar promedio

resultado = (list(map(funciones, paraleloA)))

print(list(zip(resultado, nombres)))