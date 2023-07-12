import tkinter as tk
from tkinter import ttk
import serial
import keyboard


# Initialize communication port for handheld scanner
ser = serial.Serial("COM3", baudrate=9600)

stoneList = []

# Create an input for barcode data
# while True:
#     data = (input("Enter a stone tag number: (or 'q' to quit)"))
#     print(data)
#
#     if data =='q':
#         break
#
#     stoneList.append(data)

while True:
    data = ser.readline().decode().strip()
    print(data)
    if data in stoneList:
        print("Duplicate Stone Tag")
    else:
        stoneList.append(data)
        print("List of barcode numbers: " + str(stoneList))
        print("Total Barcodes Scanned: " + str(len(stoneList)))






