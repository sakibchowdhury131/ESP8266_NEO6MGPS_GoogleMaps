import serial
ser = serial.Serial('/dev/ttyUSB1', 115200)
ser.flushInput()

while True:
    try:
        ser_bytes = ser.readline()
        decoded_bytes = ser_bytes[0:len(ser_bytes)-2].decode("utf-8")
        print(decoded_bytes)
    except:
        print("Keyboard Interrupt")
        break