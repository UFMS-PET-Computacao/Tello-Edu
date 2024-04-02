from djitellopy import Tello

tello = Tello()
tello.connect()
tello.takeoff()

print(tello.query_battery())

tello.land()