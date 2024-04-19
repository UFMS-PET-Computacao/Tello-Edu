from djitellopy import Tello

""" Escreva um programa que verifique a altitude atual do drone, se ela for
maior que 1 metro faca o drone girar 360 graus em sentido horario, caso
contrario, faca-o pousar imediatamente"""

tello = Tello()
tello.connect()
tello.takeoff()

tello.move_up(50)

x = tello.get_height()

if x > 100:
    tello.rotate_clockwise(360)
    print(f"altura: {tello.get_battery()}")
    print(f"bateria: {tello.get_battery()}")
    tello.land()
else:
    print(f"bateria: {tello.get_battery()}")
    tello.land()