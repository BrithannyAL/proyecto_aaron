estado = True

while estado == True:
    Num = int(input("Ingresar numero:"))
    
    if Num > 5:
        print(Num - 5)
        estado = False
    elif Num < 5:
        print(Num + 5)
        estado = False