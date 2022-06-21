lista=[1,2,3,4,5,6,7,8,9,10,10,5,5,4,7,8,6,14,15,15,14,5,5]
print("Eliminacion de numero repetidos")
print(lista)
Numeros = set(lista)
lista = list(Numeros)
print("Numero que no se repiten")
print(lista)