if 4>5:
    print("verdad")
else:
    print("falso")
    
if 10%2 == 0:
    print("es par")
    
# MOSTRAR EL MAYOR DE 3 NUMEROS

num1,num2,num3 = 4, 3 , 7
if num1 > num2 and num1> num3:
    print(f"{num1} es mayor")
elif num2>num1 and num2>num3:
    print(f"{num2} es mayor")
else:
    print(f"{num3} es mayor")

# MOSTRAR TODOS LOS ELEMENTOS DE UNA LISTA QUE SEAN MULTIPLOS DEL 3 Y 5, DE UNA LISTA DE 100 ELEMENTOS

import random

valores = list(range(1,100))

for valor in valores:
    if valor%3==0 and valor%5==0:
        print(valor)
