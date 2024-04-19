from djitellopy import Tello

"""Escreva um programa que leia um número inteiro dado pelo usuário
 e faça o drone repetir esse número de vezes a instrução: 
 Andar 50 centímetros para frente."""

tello = Tello()
tello.connect()
tello.takeoff()

print("Digite o numero")

x = int(input())

for i in range(x):
    tello.move_forward(50)

print(f"bateria: {tello.get_battery()}")
tello.land()