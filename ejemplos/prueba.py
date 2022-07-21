try:
    edad = int(input('Ingrese su edad: '))
    anio_actual = 2022
    anio_nacimiento = anio_actual - edad
    print('Usted nació en el año', anio_nacimiento)
except (ValueError, error):
    if ValueError:
        print('El sistema espera un valor numerico')
    elif error:
        print('Hubo un error en el sistema')
   
#TAREA     
"""Diseñe un sistema que pida un numero. si el numero es mayor a 5, el sistema resta con 5, si
es menor a 5, el sistema suma con 5, y si el numero es 5, el sistema vuelve a empezar."""