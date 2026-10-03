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
    escolha = input("Esolha; ")
    return escolha

def reg_prod():
    limpar()
    idc()
    print("Registrar Produção")
    pontos()

    print("Diga a produção total do dia: ")
    prodt = int(input("Digite a produção total (Sem considerar os defeitos): "))
    pcdef = int(input("Digite a quantidade de defeitos: "))
    pcboas = prodt - pcdef
    porcent = (pcdef/prodt)*100

    

    return prodt,pcdef,pcboas,porcent

def resumo():
    limpar()
    idc()
    print ("---Resumo da produção---")
    pontos()
    print ("A produção real foi de ", pcboas, " Peças")
    print ("O numero de retrabalhos foi de ", pcdef, " peças")
    print ("A produção teve ", porcent, " % " "da produção como retrabalho")



while True:
    limpar()
    escolha = menu()
    if (escolha == "1"):

        prodt,pcdef,pcboas,porcent = reg_prod()
        input ("Digite enter para voltar: ")
        
    elif(escolha == "2"):

        print ("Opção em desenvolvimento")
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