#Informar a quantidade produzida;
#Informar quantidade de peças boas;
#informar quantidade de peças defeituosas;
#Informar tempo de produção;
#Calcular produção total;
#Calcular percentual de defeitos;
#Calcular produção por hora;
#Mostrar um resumo dos resultados.

import os

#Criar variaveis e funções

prodt = 0
pcdef = 0
pcboas = 0
porcent = 0
tempo = 0
prodh = 0

#Funções para facilitar personalização
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def pontos():
    print("--------------")

def idc():

    pontos()
    print("---IDC-CALC---")
    pontos()

#Funções de funcionamento do programa

def menu():
    idc()
    print("---M-E--N-U---")
    pontos()
    print("(1)-Registrar produção")
    print("(2)-Registrar tempo")
    print("(3)-Ver resumo")
    print("(4)-Sair")
    pontos()
    escolha = input("Escolha; ")

    return escolha

def reg_prod():
    limpar()
    idc()
    print("Registrar Produção")
    pontos()

    print("Diga a produção total do dia: ")
    pcboas = int(input("Digite a produção total: "))
    pcdef = int(input("Digite a quantidade de defeitos: "))
    prodt = pcboas + pcdef
    porcent = (pcdef/prodt)*100

    return prodt,pcdef,pcboas,porcent

def reg_tempo():
    limpar()
    idc()
    print ("Registrar tempo")

    tempo = int(input("Quanto tempo pra produzir?(Ex: 8: "))
    ph = prodt / tempo
    print ("Tempo registrado")

    return ph, tempo


def resumo():
    limpar()
    idc()
    print ("---Resumo da produção---")
    pontos()
    print ("A produção foi de", pcboas, "Peças")
    print ("O numero de retrabalhos foi de", pcdef, " peças")
    print ("A produção total foi de", prodt, "peças")
    print ("A produção teve ", porcent, " % " "de retrabalho")
    print ("Foram precisas", tempo, "Horas para produzir" )
    print ("A produção foi de cerca de ", prodh, "peças por hora")


while True:
    limpar()
    escolha = menu()
    if (escolha == "1"):

        prodt,pcdef,pcboas,porcent = reg_prod()
        input ("Digite enter para voltar: ")
        
    elif(escolha == "2"):

        prodh,tempo = reg_tempo()
        input ("Digite enter para voltar: ")

    elif(escolha == "3"):

        resumo()
        input ("Digite enter para voltar: ")

    elif (escolha == "4"):
        print("Encerrado!")
        break

    else :
        print ("Opção invalida, escolha uma opção valida")
        input ("Clique enter para voltar: ")