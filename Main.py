
while True:

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Programa encerrado.")
        

    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if opcao == "+":
        print("Resultado:", a + b)
    elif opcao == "-":
        print("Resultado:", a - b)
    elif opcao =="x":
        print("Resultado:", a * b)
    elif opcao == "÷":
        print("Resultado:", a / b)
    else:
        print("Opção inválida")