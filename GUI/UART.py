from serial import Serial

ser = Serial('COM3', 115200)

while True:
    if ser.readable():
        res = ser.readline()
        print(res.decode()[:len(res)-1])