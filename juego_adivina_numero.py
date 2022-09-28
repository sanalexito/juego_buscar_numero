from random import*

print("Pensé en un número. Tienes ocho intentos para adivinarlo...\nLe entras o te da culo?")
aleatorio = randint(1, 100)
intentos = 0
num_usuario = 0
condicion = input("s/n: ")
if condicion=="s":
    intentos = 0
    while intentos < 8:
        num_usuario = input("Dime tu número que debe estar entre 1 y 100: ")
        intentos +=1
        if int(num_usuario) not in range(1, 101):
            print("Seas mamón!!! Pusiste un número fuera de rango y")
        elif int(num_usuario)<aleatorio:
           print("Nel, mi número es más alto")
        elif int(num_usuario)>aleatorio:
           print("Noup! Mi número está por abajo")
        else:
            print(f"Rifadote!!! Le atinaste en {intentos} intentos")
            break
    if int(num_usuario)!=aleatorio:
        print(f"Se te acabó el veinte! El bueno era {aleatorio}")
else:
    print("Abrigo pinche miedoso!!!")
