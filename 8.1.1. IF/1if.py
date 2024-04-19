from djitellopy import Tello

""" Escreva um programa que leia quatro bases de missao, caso o numero lido
seja igual a 4, de o comando para o drone dar uma cambalhota para tras. """
""" """
# distancia entre um missionpad e outro.
DISTANCIA = 78

tello = Tello()
tello.connect()
tello.takeoff()

# habilita o drone para reconhecer bases de missão
tello.enable_mission_pads()

# le o valor do mission pad
x = tello.get_mission_pad_id()
# verifica se o valor eh igual a 4
if x == 4:
    # caso verdadeiro, da a cambalhota para tras
    tello.flip_back()

# andando 60cm para frente para ler o proximo mission pad,
# experimente com diferentes distancias
tello.move_forward(DISTANCIA)
y = tello.get_mission_pad_id()
if y == 4:
    tello.flip_back()

tello.move_forward(DISTANCIA)
z = tello.get_mission_pad_id()
if z == 4:
    tello.flip_back()

tello.move_forward(DISTANCIA)
w = tello.get_mission_pad_id()
if w == 4:
    tello.flip_back()

# posteriormente vamos aprender a optimizar esse codigo :D

print(f"bateria: {tello.get_battery()}")
tello.land()