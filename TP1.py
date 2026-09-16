#1
print("Hola Mundo!")
#2
nombre=input("Ingrese su nombre: ")
print(f"Hola {nombre}!")
#3
nombre=input("Ingrse su nombre: ")
apellido=input("Ingrse su apellido: ")
edad=int(input("Ingrse su edad: "))
lugar_de_residencia=input("Ingrse su lugar de residencia: ")
print(f"Soy {nombre} {apellido},tengo {edad} años y vivo en {lugar_de_residencia}")
#4
radio=int(input("Ingrese radio de un circulo: "))
area=float(3.14*radio**2)
perimetro=float(2*3.14*radio)
print(f"Su radio es: {radio}")
print(f"Su area es: {area}")
print(f"Su perimetro es: {perimetro}")
#5
seg=int(input("Ingrese una cantidad de segundos: "))
horas=float(seg*0.000277778)
print(f"Es equivalente a {horas} hs.")
#6
numero=int(input("Ingrese un número entero: "))
tabla_0=numero*0
tabla_1=numero*1
tabla_2=numero*2
tabla_3=numero*3
tabla_4=numero*4
tabla_5=numero*5
tabla_6=numero*6
tabla_7=numero*7
tabla_8=numero*8
tabla_9=numero*9
print(f"""Su tabla de multiplicar es: 
      {numero}x0={tabla_0}
      {numero}x1={tabla_1}
      {numero}x2={tabla_2}
      {numero}x3={tabla_3}
      {numero}x4={tabla_4}
      {numero}x5={tabla_5}
      {numero}x6={tabla_6}
      {numero}x7={tabla_7}
      {numero}x8={tabla_8}
      {numero}x9={tabla_9}""")
#7
num_a=int(input(f"Ingrese un numero distinto de 0: "))
num_b=int(input(f"Ingrese un otro numero distinto de 0: "))
suma=num_a+num_b
divicion=num_a/num_b
mutiplicacion=num_a*num_b
resta=num_a-num_b
print(f"""
      Resultado de sumar: {suma}
      Resultado de dividir: {divicion}
      Resultado de multiplicar: {mutiplicacion}
      Reultado de restar: {resta}""")
#8
alt=float(input(f"Ingrese su altura(m): "))
peso=float(input(f"Ingrese su peso(kg): "))
imc=peso/alt**2
print(f"Su IMC es: {imc}")
#9
temperatura=int(input(f"Ingrese temperatura en grados celsius: "))
fahrenheit=temperatura*9/5+32
print(f"Su temperatura en fahrenheit es de: {fahrenheit}")
#10
num_C=int(input(f"Ingrese el 1° número: "))
num_D=int(input(f"Ingrese el 2° número: "))
num_E=int(input(f"Ingrese el 3° número: "))
promedio=(num_C+num_D+num_E)/3
print(f"Su promedio es de: {promedio}")
