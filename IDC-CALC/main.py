#calculadora de producao
import os
#Criando funções
lstProd = []
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def validarEsc():
    while True:
        esc = input(": ")
        if esc.isdigit():
            if int(esc) >= 0:
                break
        print("Valor invalido, digite novamente!")
        input("Clique enter para retornar: ")
    return int(esc)
    
def registrarProd(lista):
    print("Registrar produção")
    hora = input("Digite a hora: ")
    for h in lista:
        if h[0] == hora:
            print("Hora ja registrada!")
            print("Deseja atualizar a produção desse horario?")
            print("(1) - Sim\n(2) - Não")
            e = validarEsc()
            if e == 1:
                print("Digite a produção da hora")
                pn = validarEsc()
                h[1] = pn
                return
                
            else:
                return

    print("Digite a produção da hora: ")
    p = validarEsc()
    print("Valor invalido")
            
    prod = int(p)
    lista.append([hora,prod])
    lista.sort()
    return lista

def registrarTempo():
    print("Opção em desenvolvimento")
    input("Clique enter para voltar: ")

def resumo():
    c = 0
    for i in lstProd:
        print("A produção de {} foi {}".format(lstProd[c][0],lstProd[c][1]))
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
    esc = validarEsc()
    if esc == 1:
            registrarProd(lstProd)
    elif esc == 2:
            registrarTempo()
    elif esc == 3:
            resumo()
    elif esc == 4:
            print("Programa encerrado")
            break
    else:
            print("Valor invalido")
            input("Clique enter para voltar: ")
