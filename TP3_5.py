nombre=input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre=input(f"Nombre del Gladiador: ")
nombre=nombre.capitalize()

vida_jug=100
vida_enem=100
pociones=3
dano_pesado_base=15
dano_enemigo_base=12
juego_activo=True

print("\n=== INICIO DEL COMBATE ===")

while vida_jug>0 and vida_enem>0:
    print(f"\n{nombre} (HP: {vida_jug}) vs Enemigo (HP: {vida_enem}) | Pociones: {pociones}")
    print("Elige acción:\n1. Ataque Pesado\n2. Ráfaga Veloz\n3. Curar")

    opcion=input("Opción: ")
    while not opcion.isdigit() or int(opcion)<1 or int(opcion)>3:
        print("Error: Ingrese un número válido.")
        opcion=input("Opción: ")
    opcion=int(opcion)

    if opcion ==1:
        if vida_enem<20:
            dano =dano_pesado_base*1.5  
            print(f"GOLPE CRÍTICO. Atacaste al enemigo por {dano} puntos de daño.")
        else:
            dano=dano_pesado_base
            print(f"Atacaste al enemigo por {dano} puntos de daño!")
        vida_enem= vida_enem-dano
    elif opcion==2:
        print(">> Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enem =vida_enem-5
            print("> Golpe conectado por 5 de daño")
    elif opcion ==3:
        if pociones>0:
            vida_jug=vida_jug+30
            pociones =pociones-1
            print(f"Te has curado. Vida actual: {vida_jug}")
        else:
            print("No quedan pociones.")
    if vida_enem>0:
        vida_jug=vida_jug - dano_enemigo_base
        print(f">> El enemigo te atacó por {dano_enemigo_base} puntos de daño!")

if vida_jug>0:
    print(f"\nVICTORIA! {nombre} ha ganado la batalla.")
else:
    print("\nDERROTA! Has caído en combate.")
