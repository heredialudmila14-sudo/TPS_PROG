intento=0
usuario_correcto="alumno"
clave_correcta="python123"
mensaje="neuroplasticidad"
acceso=False
opcion_4=True

while intento<3:
    usuario=input(f"Intento{intento+1}/3 - Usuario: ")
    clave=input(f"Clave: ")
    if usuario==usuario_correcto and clave==clave_correcta:
        acceso=True
        print("Acceso concedido.")
        break  
    else:
        print("Error: credenciales invalidas.")
        intento=intento+1
if not acceso:
    print("Cuenta bloqueada.")
else: 
    while opcion_4:
        print('''1) Estado 2) Cambiar clave 3) Mensaje 4) Salir''')
        opcion=input("Opcion: ")
        while not opcion.isdigit() or int(opcion) <1 or int(opcion)>4:
            opcion=input("Error: ingrese un numero valido. \nOpcion: ")
        opcion=int(opcion)

        if opcion == 1:   
            print("Estado: Inscripto.")
        elif opcion== 2:
            nueva_clave=input("Cambiar clave: ")
            while len(nueva_clave)<6:
                nueva_clave=input("Error: minimo 6 caracteres. \nCambiar clave: ")
            confirmacion=input("Confirmar clave: ")
            if nueva_clave==confirmacion:
                print("Se cambio de clave con exito.")
            else:
                print("Error: las claves no coinciden.")
        elif opcion== 3:
            print(F"{mensaje}")
        else:
            print("Salir")
            opcion_4=False
            