from djitellopy import Tello

""" Escreva um programa que leia duas bases de missao, caso a multiplicacao
entre esses dois numeros seja menor que 4, de o comando para o drone
dar uma cambalhota para frente."""

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

if x*y < 4:
    # da uma cambalhota para tras
    tello.flip_forward()

print(f"bateria: {tello.get_battery()}")

tello.land()