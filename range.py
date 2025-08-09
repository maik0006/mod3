print("Ejemplo 1: range (5)")
for i in range (5):
    print(i)
print("Ejemplo 2: range (1, 10, 2)")
for i in range (1, 10, 2):
    print(i)
print("Ejemplo 3: range (2, 7)")
for i in range (2, 7):
    print(i)
print("Ejemplo 4: range (10, 0, -1)")
for i in range (10, 0, -1):
    print(i)
for i in range (5):
    print(f"Iteracion{i+1}")
nombres=["Ana","Carlos","Elena"]
for i in range(len(nombres)):
    print(f"posicion {i}: {nombres [i]}")
multiplos = [x*5 for x in range (1, 11)]
print(multiplos )