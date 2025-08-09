#Pop
tareas = ["Estudiar","Comprar","Cocinar","Limpiar"]
tarea_urgente = tareas.pop(1)
print(f"Tarea eliminida:{tarea_urgente}")
print(f"lista despues:{tareas}")
tarea_urgente = tareas.pop()
print(f"Ultima tarea:{tarea_urgente}")
print(f"lista final:{tareas}")
#Insert
numeros = [1, 2, 4, 5]
numeros.insert(2, 3)
print(f"Despues de insert(2, 3): {numeros}")
numeros.insert(0, 0)
print(f"Despues de insert(0, 0): {numeros}")
#Len
elementos = ["a","b","c","d"]
longitud = len(elementos)
#sum
precios = [10.5,20,5.25]
total = sum(precios)
#Max
edades = [25,30,18,45,22]
edad_maxima = max(edades)
letras = ["z","a","k","m"]
letra_maxima = max(letras)
#append
lista_original = [1,2,3,]
lista_original.append([4,5])
print(lista_original)
#extend
lista_original = [1,2,3,]
lista_original.extend([4,5])
print(lista_original)