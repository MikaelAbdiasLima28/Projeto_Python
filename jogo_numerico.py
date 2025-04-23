import random

def escolher_dificuldade():
    print("\nEscolha o nível de dificuldade:")
    print("1 - Fácil (1 a 10)")
    print("2 - Médio (1 a 50)")
    print("3 - Difícil (1 a 100)")

    while True:
        escolha = input("Digite o número da dificuldade: ")
        if escolha == '1':
            return 10
        elif escolha == '2':
            return 50
        elif escolha == '3':
            return 100
        else:
            print("Opção inválida. Tente novamente.")
