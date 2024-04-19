from djitellopy import Tello

"""Escreva um programa que leia quatro bases de missao e imprima todos os
numeros lidos"""

tello = Tello()
tello.connect()
tello.takeoff()

tello.enable_mission_pads()

# distancia entre um missionpad e outro.
DISTANCIA = 78

x = tello.get_mission_pad_id()

for i in range(4):
    x = tello.get_mission_pad_id()
    print(f"num {i+1}: {x}")
    tello.move_forward(DISTANCIA)

print(f"bateria: {tello.get_battery()}")
tello.land()