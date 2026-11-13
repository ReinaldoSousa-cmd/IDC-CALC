horas = input("Digite: ")
separada = horas.split(":")
if int(separada[0]) >= 0 and int(separada[0]) <= 23:
    print("Hora valida")
    if int(separada[1]) >= 0 and int(separada[1]) <= 59:
        print("Minuto valido")
hora = separada[0] 
minu = separada[1]
print(hora, minu)
