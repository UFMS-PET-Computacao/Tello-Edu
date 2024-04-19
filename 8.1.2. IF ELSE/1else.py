from djitellopy import Tello

""" Escreva um programa que leia duas bases de missao, se algum desses dois
numeros for igual a 1: imprima “:)”. Caso contrario: imprima “:(“."""

tello = Tello()
tello.connect()
tello.takeoff()

# habilita o drone para reconhecer bases de missão
tello.enable_mission_pads()

x = tello.get_mission_pad_id()

# andando 60cm para frente para ler o proximo mission pad,
# experimente com diferentes distancias
tello.move_forward(60)
y = tello.get_mission_pad_id()

if x == 1 or y == 1:
    print(":)")
else:
    print(":(")

print(f"bateria: {tello.get_battery()}")

tello.land()