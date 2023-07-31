def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Não é possível dividir por zero."

def calculadora():
    print("Bem-vindo à calculadora!")
    print("Digite 'sair' a qualquer momento para encerrar.")

    while True:
        operacao = input("Escolha uma operação (adição, subtração, multiplicação, divisão): ").lower()

        if operacao == 'sair':
            print("Encerrando a calculadora. Até logo!")
            break

        if operacao not in ['adição', 'subtração', 'multiplicação', 'divisão']:
            print("Operação inválida. Tente novamente.")
            continue

        try:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar números válidos.")
            continue

        if operacao == 'adição':
            resultado = adicao(numero1, numero2)
        elif operacao == 'subtração':
            resultado = subtracao(numero1, numero2)
        elif operacao == 'multiplicação':
            resultado = multiplicacao(numero1, numero2)
        else:
            resultado = divisao(numero1, numero2)

        print(f"Resultado: {resultado}\n")


if __name__ == "__main__":
    calculadora()
