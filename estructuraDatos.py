#lista(list)
frutas=["Tunas","Guayabas","Maracuya"]
numerosPrimos=[3,5,7,11]
print(type(frutas))
print(type(numerosPrimos))
print(frutas[0])
print(numerosPrimos[2])
frutas[0]="Mango"
print(frutas)
frutas.append("Lichi")
print(frutas)
# Buscar la posición de un elemento en la lista de frutas
elemento = "Guayabas"
if elemento in frutas:
    posicion = frutas.index(elemento)
    print(f"La posición de '{elemento}' en la lista de frutas es: {posicion}")
else:
    print(f"'{elemento}' no se encuentra en la lista de frutas.")
# Contar la cantidad de de caracteres de un elemento en la lista de frutas
