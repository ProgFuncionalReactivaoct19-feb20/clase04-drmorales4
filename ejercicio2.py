"""
	ejercicio2 - en clase
	@drmorales4

"""

lista = [(100, 2), (20, 4), (30, 1)]
lista2 = ["b", "a", "c"]

# listaB = sorted(lista, key = lambda x: [1])
# lista2B = sorted(lista2)

print(list(zip(sorted(lista2), sorted(lista, key = lambda x: x[1]))))