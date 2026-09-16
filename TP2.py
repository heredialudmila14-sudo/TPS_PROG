#1
edad=int(input("Ingrese su edad: "))
if(edad<18):
    print("Es menor de edad. ")
else:
    ("edad>18")
    print("Es mayor de edad. ")
#2
nota=float(input("Ingrese su nota: "))
if(nota<=6):
    print("Desaprobado.")
else:
    (nota>=6)
    print("Aprobado")
#3
numero=int(input("Ingrese un numero par: "))
if(numero%2==0):
    print("Ha ingresado un numero par.")
else:
    (numero%2!=0)
    print("Por favor, ingrese un numero par.")
#4
edad=int(input("Por favor, ingrese su edad en años: "))
if(12>=edad):
    print("Pertenece a categoria de niño/a.")
elif(12<=edad<18):
    print("Pertenece a la categoria de adolecente.")
elif(18<=edad<30):
    print("Pertenece a la categoria de adulto/a joven.")
else:
    print("Pertenece a la categoria de adulto.")
#5
contraseña=input("Por favor, ingrese una contraseña de entre 8 y 14 caracteres: ")
if 8<= len (contraseña) <14:
    print("Ha ingresado una contraseña corecta.")
else:
    print("Por favor, ingrese una contaseña de entre 8 y 14 caracteres.")
#6
consumo=float(input("Por favor, ingrese su consumo electrico mensual (en kWh): "))
if consumo<150:
    print("Consumo bajo.")
elif 150<=consumo <=300:
    print("Consumo medio.")
else:
    print("Consumo alto.")
    if consumo>500:
        print("Considere medidas de ahorro energetico.")
#7
frase=input("Por favor, ingrese una frase o palabra: ")
if frase[-1] in ("AEIOUaeiou"):
    print(f"{frase}!")
else:
    print(frase)
#8
nombre=input("Por favor, ingrese su nombre: ")
print("""
      Lea las siguientes opciones:
      1.Si quiere su nombre en Mayusculas.(PEZ)
      2.Si quiere su nombre en Minusculas.(pez)
      3.Si quiere su nombre con la primera letra mayuscula.(Pez)""")
opcion=int(input("Por favor, eliga una opcion: "))
if opcion==1:
    mayus=nombre.upper()
    print(f"{mayus}")
elif opcion==2:
    minus=nombre.lower()
    print(f"{minus}")
else:
    opcion==3
    titulo=nombre.title()
    print(f"{titulo}")
#9
magnitud=float(input("Por favor, ingrese la mangnitud del terremoto: "))
if magnitud<3:
    print("Muy leve(imperceptible).")
elif 3<= magnitud <4:
    print("Leve(ligeramente perceptible).")
elif 4<= magnitud <5:
    print("Moderado(sentido por personas, pero generalmete no causa daños)")
elif 5<= magnitud <6:
    print("Fuerte(puede causar daños en estructuras débiles).")
elif 6<= magnitud<7:
    print("Muy fuerte(puede causar daños significativos).")
else:
    ("Extremo(puede causar graves daños a gran escala).")
#10
hem=input("Por favor, ingrese su hemisferio (N/S): ")
hem=hem.lower()
mes=int(input("Por favor, ingrese el MES del año en números: "))
dia=int(input("Por favor, ingrese que DÍA del mes en números: "))
if (mes==12 and dia>21) or (mes in (1,2)) or (mes==3 and dia<20):
    if hem=="n":
        print("Verano.")
    elif hem=="n":
        print("Invierno")

if (mes==3 and dia>21) or (mes in (4,5)) or (mes==6 and dia<20):
    if hem=="s":
        print("Otoño.")
    elif hem=="n":
        print("Primavera.")

if (mes==6 and dia>21) or (mes in (7,8)) or (mes==9 and dia<20):
    if hem=="s":
        print("Invierno.")
    elif hem=="n":
        print("Verano")

if (mes==9 and dia>21) or (mes in (10,11)) or (mes==12 and dia<21):
    if hem=="s":
        print("Primavera.")
    elif hem=="n":
        print("Otoño.")
