numero = int(input('Escriba un numero del 1 hasta el 100: '))

if numero > 50:
    print('El número está más cerca del 100')
elif numero < 50:
    print('El numero está más cerca del 1')
elif numero == 50:
    print('El número es la mitad')