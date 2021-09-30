#Тестирование PyTelnet библиотеки
import time

from telnet.telnet import *
from telnetlib import Telnet

#tln=telnet('10.0.0.18')
#tln.connect()
#tln.send(' ')
#while True:
    #time.sleep(1)
    #print(tln.recieve(1024))
    #tln.send(input())

tn = Telnet('10.0.0.18')   # connect to finger port
tn.write("vt100\n")
#time.sleep(2)
tn.write('admin'+'\n')
#time.sleep(2)
print(tn.read_all())
tn.close()
