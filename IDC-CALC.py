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

while True:
    limpar()
    escolha = menu()
    if (escolha == "1"):

        pontos()
        print ("Opção em criação")
        input("Clique enter para retornar")

    elif(escolha == "2"):

        pontos()
        print ("Opção em criação")
        input("Clique enter para retornar")

    elif(escolha == "3"):

        pontos()
        print ("Opção em criação")
        input("Clique enter para retornar")

    elif (escolha == "4"):
        print("Encerrado!")
        break