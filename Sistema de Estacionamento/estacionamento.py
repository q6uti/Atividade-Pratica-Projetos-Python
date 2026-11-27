import os
os.system("cls")

capacidade = 20
tarifa = 8.00
estacionados = 0
faturamento = 0.0

def calcular(horas):
    return horas * tarifa

while True:
    print("===== SISTEMA DE ESTACIONAMENTO ===== \n")
    print("1 - Registrar entrada de veículo")
    print("2 - Registrar saída de veículo")
    print("3 - Consultar vagas disponíveis")
    print("4 - Consultar faturamento")
    print("0 - Sair \n")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        if estacionados >= capacidade:
            print("Estacionamento lotado \n")
        else:
            placa = input("Digite a placa do veículo: ")
            estacionados += 1
            print(f"Entrada do veículo {placa} registrada! \n")
            
    elif opcao == "2":
        if estacionados == 0:
            print("Não há veículos estacionados. \n")
        else:
            placa = input("Digite a placa do veículo: ")
            horas = int(input("Quantas horas ficou estacionado? "))
            
            valor = calcular(horas)
            faturamento += valor
            estacionados -= 1

            print(f"Valor a pagar: R$ {valor:.2f} \n")

    elif opcao == "3":
        print(f"Capacidade total: {capacidade}")
        print(f"Veículos estacionados: {estacionados}")
        print(f"Vagas disponíveis: {capacidade - estacionados} \n")
    
    elif opcao == "4":
        print(f"Faturamento total: R$ {faturamento:.2f}\n")
    
    elif opcao == "0":
        print("Até mais!")
        break

    else:
        print("Opção inválida \n")
