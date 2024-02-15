#Crear una lista vacia

lista_vacia = []
print(len(lista_vacia))

#crear una lista como array

motocicletas = ['Zeus','Pegasus','kyngo','Susuki','BMW', 'Honda']

#crear una lista usando list

paises = list(('España','Portugal','Italia','Francia','Suiza','Alemania'))

#crear lista con rage

numeros = list(range(1,100))

#Modificar una lista

print(paises)
print(paises[2])

paises[2] = 'Italy'
print(paises)
print(paises[2])

#Agregar valores append --> agrega items al final de la lista

paises.append('Ucrania')
paises.append('Rusia')

print(paises)

#agregar valores N posicion

print(motocicletas)
motocicletas.insert(1,'Kawasaki')
print(motocicletas)

#eliminar ultimos valores

print(len(paises))
ultimo = paises.pop()
print(f"Elemento eliminado:{ultimo}")
print(len(paises))

#eliminar un valor de la posicion n de una lista

print(paises)
eliminado = paises.pop(2)
print(f"eliminado:{eliminado}")
print(paises)