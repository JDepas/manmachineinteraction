#!/bin/bash/python3
#coding=utf-8

minhalista_ips=[]
 
minhalista_portos=[]


a = 1

ficheiro_ips=open('escreveips.txt', 'w')

while a < 256 :

    minhalista_ips.append("192.168.1." + str(a))

    

    a+=1
ficheiro_ips.writelines(minhalista_ips)       
ficheiro_ips.close()


i=1
ficheiro_portos=open('escreveportos.txt', 'w')
for i in range(1024):
    
    minhalista_portos.append(str(i))
    print(i)
    
ficheiro_portos.writelines(minhalista_portos)
ficheiro_portos.close()    