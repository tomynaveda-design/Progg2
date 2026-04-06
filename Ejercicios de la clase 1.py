r=0
h=0

valido=False
while valido==False:
    try:
        r=float(input("ingrese el radio del circulo: "))
        valido=True
    except:
        print("Error solo se permiten numeros")

        
valido=False
while valido==False:
    try:
        h=float(input("ingrese la altura del circulo: "))
        valido=True
    except:
        print("Error solo se permiten numeros")
        
        
area = 2 * 3.14 * r * h + 2 * 3.14 * r**2
volumen = 3.14 * r**2 * h
        
print("El area es: ", area)
print("El volumen es: ", volumen)

