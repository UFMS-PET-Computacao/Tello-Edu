from djitellopy import Tello

""" Escreva um programa que leia quatro bases de missao, armazene em uma
variavel a soma dos numeros lidos e imprima na tela o valor dessa variavel
quando a soma for maior ou igual a 7"""

# distancia entre um missionpad e outro.
DISTANCIA = 78

tello = Tello()
tello.connect()
tello.takeoff()

# habilita o drone para reconhecer bases de missão
tello.enable_mission_pads()

soma = tello.get_mission_pad_id()

# andando 60cm para frente para ler o proximo mission pad,
# experimente com diferentes distancias
tello.move_forward(DISTANCIA)
soma = soma + tello.get_mission_pad_id()

tello.move_forward(DISTANCIA)
soma = soma + tello.get_mission_pad_id()

tello.move_forward(DISTANCIA)
soma = soma + tello.get_mission_pad_id()

if soma >= 7:
    print(soma)

print(f"bateria: {tello.get_battery()}")

tello.land()