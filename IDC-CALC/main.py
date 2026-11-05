#calculadora de producao
import os
#Criando funções
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def registrarProd():
    print("Opção em desenvolvimento")
    input("Clique enter para voltar: ")

def registrarTempo():
    print("Opção em desenvolvimento")
    input("Clique enter para voltar: ")

def resumo():
    print("Opção em desenvolvimento")
    input("Clique enter para voltar: ")

#Loop do menu

while True:
    limpar()
    print("="*8)
    print("IDC-CALC")
    print("="*8)
    print('''
(1) - Registrar produção
(2) - Registrar tempo
(3) - Ver resumo
(4) - Sair''')
    esc = input("Escolha: ")
    if esc.isdigit():
        select = int(esc)
        if select == 1:
            registrarProd()
        elif select == 2:
            registrarTempo()
        elif select == 3:
            resumo()
        elif select == 4:
            print("Programa encerrado")
            break
        else:
            print("Valor invalido")
            input("Clique enter para voltar: ")
    else:
        print("Valor invalido")
        input("Clique enter para voltar: ")
