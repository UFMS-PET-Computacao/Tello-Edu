from djitellopy import Tello

"""" Escreva um programa que leia quatro bases de missao, armazene em uma
variavel “diff1” a diferenca entre o primeiro e segundo ID lidos, em uma
variavel “diff2” a diferenca entre o terceiro e quarto. Trate os seguintes
casos: Se diff1 e diff2 forem ambos positivos, de o comando para o drone
dar uma cambalhota para frente; Senao, se diff1 e diff2 forem ambos
negativos, de o comando para o drone dar uma cambalhota para tras; Se
nenhum dos casos anteriores se aplica, apenas pouse o drone."""

tello = Tello()
tello.connect()
tello.takeoff()

# distancia entre um missionpad e outro.
DISTANCIA = 78

x = tello.get_mission_pad_id()

tello.move_forward(DISTANCIA)
y = tello.get_mission_pad_id()

diff1 = x - y

tello.move_forward(DISTANCIA)
z = tello.get_mission_pad_id()

tello.move_forward(DISTANCIA)
w = tello.get_mission_pad_id()

diff2 = z - w

if diff1 > 0 and diff2 > 0:
    tello.flip_forward() 
elif diff1 < 0 and diff2 < 0:
    tello.flip_back()

print(diff1, diff2)

print(f"bateria: {tello.get_battery()}")
tello.land()