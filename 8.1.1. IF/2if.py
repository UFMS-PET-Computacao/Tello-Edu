from djitellopy import Tello

""" Escreva um programa que leia quatro bases de missao e pouse o drone
imediatamente caso o numero lido seja igual a 3. """

# distancia entre um missionpad e outro.
DISTANCIA = 78

tello = Tello()
tello.connect()
tello.takeoff()

# habilita o drone para reconhecer bases de missão
tello.enable_mission_pads()

# le o valor do mission pad
x = tello.get_mission_pad_id()
# verifica se o valor eh igual a 3
if x == 3:
    # caso verdadeiro, da a cambalhota para tras
    tello.land()

# andando 60cm para frente para ler o proximo mission pad,
# experimente com diferentes distancias
tello.move_forward(DISTANCIA)
y = tello.get_mission_pad_id()
if y == 3:
    tello.land()

tello.move_forward(DISTANCIA)
z = tello.get_mission_pad_id()
if z == 3:
    tello.land()

tello.move_forward(DISTANCIA)
w = tello.get_mission_pad_id()
if w == 3:
    tello.land()

print(f"bateria: {tello.get_battery()}")

tello.land()