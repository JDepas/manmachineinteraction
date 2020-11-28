#!/bin/bash/python3
#coding=utf-8
import socket

from datetime import datetime

ficheiro_scans=open('escreve_scans.txt', 'w')
portos_abertos=[]


tinicial=datetime.now()




def portscan(ip,port):


    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result=sock.connect_ex((ip,port))
    if result==0:
        print("Port {}:     Open".format(port))
        portos_abertos.append(str(port))
    
    
    ficheiro_scans.writelines(portos_abertos)
    
    sock.close()

ip=input("Insira o IP: ")


try:
    for i in range(1024):
        portscan(ip,i)


except KeyboardInterrupt:
    print("pressionado ctrl+c")
    sys.exit()

except socket.gaierror:
    print("host invalido")
    sys.exit()

except socket.error:
    print("erro de conexao ao servidor")
    sys.exit()

 
ficheiro_scans.close() 

tfinal=datetime.now()

ttotal=tfinal-tinicial

print("tempo total de scan " +str(ttotal))

