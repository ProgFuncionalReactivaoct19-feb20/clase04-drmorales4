"""
	ejercicio5
	@drmorales4
Manejo de colecciones y tuplas

Encontrar la siguiente estructura


[(16.333333333333332, 'Ángel'), (16.666666666666668, 'José'), (13.0, 'Ana')]
(16.666666666666668, 'José')
[(13.0, 'Ana'), (16.666666666666668, 'José'), (16.333333333333332, 'Ángel')]


Dadas las siguientes estructuras

paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]
nombres = ["Ángel", "José", "Ana"]

"""

paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]
nombres = ["Ángel", "José", "Ana"]

sacar_promedios = list(map(lambda x: (x[0]+x[1]+x[2])/3, paraleloA)) # sumar y sacar promedio

print(list(zip(sacar_promedios, nombres))) # presentar datos
print(max(zip(sacar_promedios, nombres))) # presentar el dato con el promedio mayor
print(list(zip(sacar_promedios, sorted(nombres)))) # presentar de manera ordenada los nombres