#!/bin/bash/python3
#coding=utf-8
import os 
import platform

sistema=platform.system()
print(sistema+" é o sistema actual")

print("opçao 1 - criar directoria")
print("opçao 2 - renomear directoria")
print("opçao 3 - remover directoria")
print("opçao 4 - listar directoria")

opcao= input("escolha a opçao pretendida " )

if int(opcao) == 1:
    print("vamos criar a directoria em "+ os.getcwd()+" ...")
    directoria=input(" introduza o nome da directoria:")
    os.mkdir(directoria)


elif int(opcao) == 2:
    print("vamos renomear a directoria em "+ os.getcwd()+" ...")
    directoria=input(" introduza o nome da directoria a alterar:")
    os.rename(directoria,'nome_alterado')

elif int(opcao) == 3:
    print("vamos remover a directoria em "+ os.getcwd()+" ...")
    directoria=input(" introduza o nome da directoria:")
    os.rmdir(directoria)


elif int(opcao) == 4:
    print("vamos listar directoria "+ os.getcwd()+" ...")
    listDir()
    
    #isto faz directamente a listagem em linux
    print(os.listdir())

else: 
    print("opcao errada!!!")


def listDir():
    if sistema=="Linux":
        listCMD='ls-la'
    
    elif sistema=="Windows":
        listCMD='dir'

    os.system(listCMD)        