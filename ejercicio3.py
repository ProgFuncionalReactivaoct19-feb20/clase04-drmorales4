"""
	ejercicio3 - en clase
	@drmorales4

"""

lista = [(100, 2), (20, 4), (30, 1)]
lista2 = ["b", "a", "c"]

lista2B = map(lambda x: x.upper(), lista2) # transformar a mayusculas

print(list(zip(sorted(lista), sorted(lista2B, reverse = True))))