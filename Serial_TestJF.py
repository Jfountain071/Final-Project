import serial		# importing the serial port
import string

ser=serial.Serial('/dev/ttyACM0', 250000)	# reads the serial port on the raspi, and reads at a 250000 bit rate

while True:
    serialdata=ser.readline()			# reads the current line of the Arduino's serial monitor
    print("Success! Data found!")
    print(ser)		# this will be replaced with the starting of the timer