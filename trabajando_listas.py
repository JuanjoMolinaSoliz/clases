#lista de equipos de futbol

equipos = ['Aurora', 'Bolivar', 'U de vinto', 'Wilsterman', 'Oriente Petrolero', 'The Strongers', 'Blooming']
print(equipos)

for equipo in equipos:
    print(f"Nombre de equipo: {equipo}")

for valor in range(10):
    print(valor)

for i in range(1,20):
    print(i)

for i in range(1,100,3):
    print(i)
    
# slicing

print(equipos[1:4])

# Extraer la sub lista desde la posicion 0 hasta la 4
print(equipos[:5])
print(equipos[-5:])

# TODOS LOS VALORES MENOS LOS 5 ULTIMOS
print(equipos[:-5])

# IMPRIME EN PANTALLA LOS VALORES DE LA LISTA DESDE LA POSICION 5 HASTA EL FINAL
# IMPRIME TODOS LOS VALORES MENOS LOS 5 PRIMEROS
print(equipos[5:])


