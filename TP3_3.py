nombre: str=input("Por favor, ingrese su nombre: ")
while not nombre.isalpha():
    nombre: str=input("Dato invalido. Ingrese su nombre: ")
nombre=nombre.capitalize()
print(f"Bienvenid@, {nombre}.")

lunes1=""
lunes2=""
lunes3=""
lunes4=""

martes1=""
martes2=""
martes3=""

opcion_5=True
#menu
while opcion_5:
    print("1) Reservar turno. 2) Cancelar turno(por nombre) 3) Ver agenda del dia 4) Ver resumen digital 5) Cerrar sistema ")
    opcion=input("Opcion: ")
    while not opcion.isdigit() or int(opcion)<1 or int(opcion)>5:
        opcion=input("Ingrese una opcion dentro del rango.\nOpcion: ")
    opcion=int(opcion)

    if opcion==1:
        print("Eliga dia (1=Lunes, 2=Martes). ")
        opcion1=input("Opcion: ")
        while not opcion1.isdigit() or int(opcion1)<1 or int(opcion1)>2:
            opcion1=input("Ingrese una opcion dentro del rango.\nOpcion: ")
        opcion1=int(opcion1)

        nombre: str=input("Por favor, ingrese su nombre_completo: ")
        while not nombre.isalpha():
            nombre: str=input("Dato invalido. Ingrese su nombre_completo: ")
        nombre=nombre.capitalize()
        if opcion1==1:
            print("Lunes.")
            if lunes1=="":
                lunes1=nombre
            elif lunes2=="":
                lunes2=nombre
            elif lunes3=="":
                lunes3=nombre
            elif lunes4=="":
                lunes4=nombre
            else:
                print("No hay turnos disponibles para el Lunes.")
        else:
            print("Martes.")
            if martes1=="":
                martes1=nombre
            elif martes2=="":
                martes2=nombre
            elif martes3=="":
                martes3=nombre
            else:
                print("No hay turnos disponibles para el Martes.")

    elif opcion==2:
        print("Elija dia (1=Lunes, 2=Martes). ")
        opcion1=input("Opcion: ")
        while not opcion1.isdigit() or int(opcion1)<1 or int(opcion1)>2:
            opcion1=input("Ingrese una opcion dentro del rango.\nOpcion: ")
        opcion1=int(opcion1)

        nombre_a_cancelar: str=input("Por favor, ingrese su nombre_completo: ")
        while not nombre_a_cancelar.isalpha():
            nombre_a_cancelar: str=input("Dato invalido. Ingrese su nombre_completo: ")
        nombre_a_cancelar=nombre_a_cancelar.capitalize()
        if opcion1==1:
            print("Lunes.")
            if lunes1==nombre_a_cancelar:
                lunes1=""
            elif lunes2==nombre_a_cancelar:
                lunes2=""
            elif lunes3==nombre_a_cancelar:
                lunes3=""
            elif lunes4==nombre_a_cancelar:
                lunes4=""
            else:
                print("No se encontro el paciente en el Lunes.")
        else:
            print("Martes.")
            if martes1==nombre_a_cancelar:
                martes1=""
            elif martes2==nombre_a_cancelar:
                martes2=""
            elif martes3==nombre_a_cancelar:
                martes3=""
            else:
                print("No se encontro el paciente en el Martes.")

    elif opcion==3:
        print("Elija dia (1=Lunes, 2=Martes). ")
        opcion1=input("Opcion: ")
        while not opcion1.isdigit() or int(opcion1)<1 or int(opcion1)>2:
            opcion1=input("Ingrese una opcion dentro del rango.\nOpcion: ")
        opcion1=int(opcion1)
        if opcion1==1:
            if lunes1=="":
                lib_l1="(Libre)"
            else:
                lib_l1=lunes1

            if lunes2=="":
                lib_l2="(Libre)"
            else:
                lib_l2=lunes2

            if lunes3=="":
                lib_l3="(Libre)"
            else:
                lib_l3=lunes3

            if lunes4=="":
                lib_l4="(Libre)"
            else:
                lib_l4=lunes4
            print(f'''
            Turno_1: {lib_l1}
            Turno_2: {lib_l2}
            Turno_3: {lib_l3}
            Turno_4: {lib_l4}
            ''')
        else:
            if martes1=="":
                lib_m1="(Libre)"
            else:
                lib_m1=martes1

            if martes2=="":
                lib_m2="(Libre)"
            else:
                lib_m2=martes2

            if martes3=="":
                lib_m3="(Libre)"
            else:
                lib_m3=martes3
            print(f'''
            Turno_1: {lib_m1}
            Turno_2: {lib_m2}
            Turno_3: {lib_m3}
            ''')

    elif opcion==4:
        ocupados_l=0
        if lunes1 !="":
            ocupados_l=ocupados_l+1
        if lunes2 !="":
            ocupados_l=ocupados_l+1
        if lunes3 !="":
            ocupados_l=ocupados_l+1
        if lunes4 !="":
            ocupados_l=ocupados_l+1

        ocupados_m=0
        if martes1 !="":
            ocupados_m=ocupados_m+1
        if martes2 !="":
            ocupados_m=ocupados_m+1
        if martes3 !="":
            ocupados_m=ocupados_m+1

        disponible_l= 4 - ocupados_l
        disponible_m= 3 - ocupados_m
        print(f'''
        Lunes_ Ocupados: {ocupados_l}, Disponible: {disponible_l}
        Martes_ Ocupados: {ocupados_m}, Disponible: {disponible_m}''')

        if ocupados_l > ocupados_m:
            print("Lunes tiene mas turnos.")
        elif ocupados_l < ocupados_m:
            print("Martes tiene mas turnos.")
        else:
            print("Empate de turnos.")

    else:
        print("Cerrar sistema.")
        opcion_5=False
