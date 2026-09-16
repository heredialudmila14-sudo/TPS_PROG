nombre=input("Ingrese su nombre: ")
while not nombre.isalpha():
    nombre=input("El dato es invalido, intente nuevamente: ")
nombre=nombre.capitalize()
print(f"Bienvenid@ al kiosko, {nombre}.")

cant_prod=input("Ingrese la cantidad de productos que va a llevar: ")
while not cant_prod.isdigit() or cant_prod=="0":
    cant_prod=input("El dato es invalido, intente nuevamente con un numero mayor a 0 (cero): ")
cant_prod=int(cant_prod)

total_con_descuento=0
total_sin_descuento=0

for i in range (cant_prod):
    precio=input(f"Ingrese precio del Producto_{i+1}: ")
    while not precio.isdigit():
        precio=input(f"El dato es invalido, intente nuevamente. Producto_{i+1}: ")
    precio=int(precio)
    desc=input("Tiene descuento? S/N: ")
    while desc.lower() !="s" and desc.lower() !="n":
     desc =input("Opcion invalida, intente nuevamente S/N: ")
     desc =str(desc)
    if desc.lower() =="s":
        precio_final=(precio-0.10*precio)
    else:
        precio_final=(precio)
    precio_final=float(precio_final)
    total_sin_descuento= (total_sin_descuento+precio)
    total_con_descuento= (total_con_descuento+precio_final)

print(f"""
Cliente:{nombre}
Cantidad de productos: {cant_prod}
Total sin descuento: $ {total_sin_descuento:.2f}
Total con descuento: $ {total_con_descuento:.2f}
Ahorro: $ {total_sin_descuento-total_con_descuento:.2f}
Promedio por producto: $ {total_con_descuento/cant_prod:.2f}

Gracias por su compra!!""")