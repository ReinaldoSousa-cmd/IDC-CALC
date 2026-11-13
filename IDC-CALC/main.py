#calculadora de producao
import os
#Criando funções
lstProd = []
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def validarNumero(mensagen):
    while True:
        esc = input(mensagen)
        if esc.isdigit():
            if int(esc) >= 0:
                break
        print("Valor invalido, digite novamente!")
        input("Clique enter para retornar: ")
    return int(esc)

def retornar(mensagem):
    print(mensagem)
    input("Clique enter para retornar: ")

def cabe(mensagem):
    limpar()
    print("="*len(mensagem))
    print(mensagem)
    print("="*len(mensagem))

def validarHora(mensagem):
    while True:
        horario = input(mensagem)
        separada = horario.split(":")
        hora = int(separada[0])
        minu = int(separada[1])
        if hora >= 0 and hora <= 23:
            if minu >= 0 and minu <= 59:
                return horario
        retornar("Horario invalido!")

def registrarProd(lista):
    cabe("Registrar produção")
    hora = validarHora("Digite o horario (HH:MM): ")
    for h in lista:
        if h[0] == hora:
            print("Hora ja registrada!")
            print("Deseja atualizar a produção desse horario?")
            print("(1) - Sim\n(2) - Não")
            e = validarNumero("Escolha: ")
            if e == 1:
                pn = validarNumero("Digite a produção da hora: ")
                h[1] = pn
                return
                
            else:
                return
    p = validarNumero("Digite a produção da hora: ")
            
    prod = p
    lista.append([hora,prod])
    lista.sort()
    return lista

def registrarTempo():
    retornar("Opção em desenvolvimento")

def resumo():
    cabe("Resumo")
    if not lstProd:
          retornar("Nada registrado ainda")
          return
    c = 0
    total = 0
    for i in lstProd:
        print("A produção de {} foi {}".format(lstProd[c][0],lstProd[c][1]))
        total += lstProd[c][1]
        c = c + 1
    retornar("A produção total foi de : {}".format(total))
    return

#Loop do menu

while True:
    cabe("I-D-C--CALC")
    print('''
(1) - Registrar produção
(2) - Registrar tempo
(3) - Ver resumo
(4) - Sair''')
    esc = validarNumero("Escolha: ")
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
