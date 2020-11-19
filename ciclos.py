#!/bin/bash/python3
#coding=utf-8

x=["windows", "macos", "linux", "solaris", "android", "ios" ]
 
for i in x:
    ficheiro=open('escreve.txt', 'a')
    if i != "solaris":
        print(i)
        ficheiro.write(i + "     " )
    ficheiro.close


ficheiro2=open('escreve2.txt', 'a')
a = 0
while a < len(x) :

    var=x[a]
    if var != "solaris":
        print(var)
        ficheiro2.write(i + "     " )

    a += 1        
    ficheiro2.close    