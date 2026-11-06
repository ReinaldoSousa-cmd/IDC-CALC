#calculadora de producao
import os
#Criando funções
lstProd = []
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def registrarProd(lista):
    print("Registrar produção")
    prod = int(input("Digite a produção da hora: "))
    lista.append(prod)
    return lista

def registrarTempo():
    print("Opção em desenvolvimento")
    input("Clique enter para voltar: ")

def resumo():
    c = 0
    for i in lstProd:
        print("A produção da hora {} foi {}".format(1+c,lstProd[c]))
        c = c + 1
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
            registrarProd(lstProd)
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
