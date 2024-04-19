from djitellopy import Tello

"""Escreva um programa que leia quatro bases de missao, ao encontrar o ID
de numero 2, faca o drone subir 65 centimetros."""

tello = Tello()
tello.connect()
tello.takeoff()

# distancia entre um missionpad e outro.
DISTANCIA = 78

tello.enable_mission_pads()

for i in range(4):
    x = tello.get_mission_pad_id()
    if x == 2:
        tello.move_up(20)
    tello.move_forward(DISTANCIA)

print(f"bateria: {tello.get_battery()}")
tello.land()