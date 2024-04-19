from djitellopy import Tello

""" Escreva um programa que leia quatro bases de missao, armazene em uma
variavel a soma dos numeros lidos, quando essa soma for maior ou igual
a 7, trate os dois seguintes casos: Imprima “Perfeito!” caso a soma seja
exatamente 7 ou “Quase!” se o numero for maior que 7"""

tello = Tello()
tello.connect()
tello.takeoff()

# distancia entre um missionpad e outro.
DISTANCIA = 78

# habilita o drone para reconhecer bases de missão
tello.enable_mission_pads()

# le o valor do mission pad
x = tello.get_mission_pad_id()
soma = x
# verifica se o valor eh igual a 3
if soma == 7:
    print("Perfeito!")
elif soma > 7:
    print("Quase!")

# andando 60cm para frente para ler o proximo mission pad,
# experimente com diferentes distancias
tello.move_forward(DISTANCIA)
y = tello.get_mission_pad_id()
soma = soma + y
# verifica se o valor eh igual a 3
if soma == 7:
    print("Perfeito!")
elif soma > 7:
    print("Quase!")

tello.move_forward(DISTANCIA)
z = tello.get_mission_pad_id()
soma = soma + z
# verifica se o valor eh igual a 3
if soma == 7:
    print("Perfeito!")
elif soma > 7:
    print("Quase!")

tello.move_forward(DISTANCIA)
w = tello.get_mission_pad_id()
soma = soma + w
# verifica se o valor eh igual a 3
if soma == 7:
    print("Perfeito!")
elif soma > 7:
    print("Quase!")

print(f"bateria: {tello.get_battery()}")

tello.land()