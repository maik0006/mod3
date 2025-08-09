#dict
dict()
usuario = dict(nombre="Ana",edad=28,ciudad="Lima")
print(usuario)
items = [("a",1),("b",2),("c",3)]
diccionario = dict(items)
print(diccionario)
#comprencion de diccionarios
cuadrados = {x: x**2 for x in range(1, 6)}
print(cuadrados)
pares = {x: x**2 for x in range(10) if x % 2 == 0}
print(pares)
#fromkeys
claves = ["nombre","edad","ciudad"]
diccionario = dict.fromkeys(claves,"desconicido")
print(diccionario)
congfig = dict.fromkeys("debug","cache","verbose")
print(congfig)