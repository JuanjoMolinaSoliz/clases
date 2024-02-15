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

#eliminar un valor utilizando la funcion "remove"
#remove elimina por valor 

print(paises)
paises.remove('Alemania')
print(paises)

copy_paises = paises
print(paises)
print(copy_paises)
paises.remove('Francia')
print(paises)
print(copy_paises)

copy_motos = motocicletas.copy()
print(copy_motos)
motocicletas.remove('Kawasaki')
print(motocicletas)
print(copy_motos)

#eliminar valores con 'delete'

del motocicletas[0]
print(motocicletas)

motocicletas.reverse()
print(motocicletas)
