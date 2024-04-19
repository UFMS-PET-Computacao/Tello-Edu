from djitellopy import Tello

""" Escreva um programa que verifique o nivel de bateria do drone. Se o nivel
da bateria for menor que 26%, pouse-o imediatamente, caso contraio,
faca-o subir 50 centimetros e, em seguida, pousar."""

tello = Tello()
tello.connect()
tello.takeoff()

bateria = tello.query_battery()

if bateria < 26:
    tello.land()
else:
    print(f"bateria: {tello.get_battery()}")
    tello.move_up(50)
    tello.land()

