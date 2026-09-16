energia=100
tiempo=12
cerraduras_abiertas=0
alarma=False
bloqueado=False
codigo_parcial=""
forcejeo=0

nombre: str=input("Por favor, ingrese su nombre de agente: ")
while not nombre.isalpha():
    nombre: str=input("Error. Ingrese su nombre de agente: ")
nombre=nombre.capitalize()
print(f"Bienvenid@, agente {nombre}.")

while energia>0 and tiempo>0 and cerraduras_abiertas<3 and not bloqueado:
    print(f"Energía: {energia}| Tiempo: {tiempo}| Cerraduras abiertas: {cerraduras_abiertas}|")
    print('''
    1. Forzar cerradura (costo: -20 energia, -2 tiempo) 
    2. Hackear panel    (costo: -10 energia, -3 tiempo)
    3. Descansar        (Costo: +15 energia, -1 tiempo)''')

    opcion=input("Elija acción: ")
    while not opcion.isdigit() or int(opcion)<1 or int(opcion)>3:
        opcion=input("Ingrese una opción dentro del rango.\nElija acción: ")
    opcion=int(opcion)
    
    if opcion==1:
        energia= energia-20
        tiempo= tiempo-2
        forcejeo= forcejeo+1

        if forcejeo==3:
            alarma=True
            forcejeo=0
            print("La cerradura se trabó (forzaste demasiadas veces seguidas).")
        else:
            if energia <40:
                print("Riesgo de alarma.")
                op_1=input("Eliga un numero del 1 al 3: ")
                while not op_1.isdigit() or int(op_1)<1 or int(op_1)>3:
                    op_1=input("Error, dato invalido.\nEliga un numero del 1 al 3: ")
                op_1=int(op_1)

                if int(op_1)==3:
                    alarma=True
                    print("Error. \nBloqueando cerraduras...")
            if not alarma:
                cerraduras_abiertas=cerraduras_abiertas+1
                print("Forcejeo exitoso! Abriste una cerradura.")
    elif opcion==2:
        energia= energia-10
        tiempo= tiempo-3
        forcejeo= 0

        for i in range(4):
            codigo_parcial+="Abc"
            print(f"Hackeando... \nClave actual: {codigo_parcial}")
        if len(codigo_parcial)>=8 and cerraduras_abiertas<3:
            cerraduras_abiertas=cerraduras_abiertas+1
            print("Hackeo exitoso! Abriste una cerradura.")
    elif opcion==3:
        energia= energia+15
        tiempo= tiempo-1
        forcejeo=0
        if energia>100:
            energia=100
        if alarma:
            energia=energia-10
            print("Alarma ON.\n-10 de enegia.")
    if alarma and tiempo<=3:
            bloqueado=True       
if cerraduras_abiertas==3:
    print("VICTORIA \nAbriste las tres cerraduras.")
elif bloqueado:
    print("DERROTA. \nBLOQUEO por alarma.")
else:
    energia<=0 or tiempo<=0
    print("DERROTA.\nTe quedate sin energia o tiempo.")
