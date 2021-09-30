#Тестирование easymodbus библиотеки
from easymodbus.modbusClient import *

mb_cli = ModbusClient('10.0.0.41', 502)

#mb_cli = ModbusClient('COM3')
#mb_cli.baudrate=115200
#mb_cli.parity='None'
#mb_cli.stopbits=1

mb_cli.connect()
res=mb_cli.read_holdingregisters(0,10)
print(res)

mb_cli.close()
