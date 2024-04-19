from djitellopy import Tello

"""Escreva um programa que leia uma entrada do usu ́ario em string e, utili-
zando a estrutura estudada, faca o drone dar uma cambalhota na direcao
digitada. Dica: Utilize o comando flip(direction), reveja no capitulo 5
como ele funciona"""

tello = Tello()
tello.connect()
tello.takeoff()

print("Digite uma das opções:")
print("l - para esquerda\nr - para direita\n"
      + "f - para frente\nb - para trás")

entrada = input()

tello.flip(entrada)

print(f"bateria: {tello.get_battery()}")
tello.land()