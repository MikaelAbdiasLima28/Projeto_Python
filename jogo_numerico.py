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
            print("Resposta errada. Tente novamente.")
def jogar_rodada(limite):
    numero_secreto = random.randint(1, limite)
    tentativas = 0
    print(f"\n Um número entre 1 e {limite} foi escolhido...")

    while True:
        try:
            palpite = int(input("Qual é o seu palpite? "))
            tentativas += 1
            if palpite < numero_secreto:
                print("Muito baixo! Tente um número maior.")
            elif palpite > numero_secreto:
                print("Muito alto! Tente um número menor.")
            else:
                print(f"Parabéns! Você acertou em {tentativas} tentativa(s).")
                return tentativas
        except ValueError:
            print("Por favor, digite um número válido.")
def jogo_principal():
    print("Bem-vindo ao Jogo de Adivinhação!")

    placar = []
    while True:
        limite = escolher_dificuldade()
        tentativas = jogar_rodada(limite)
        placar.append(tentativas)

        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            break 

    print("\n Placar Final:")
    for i, t in enumerate(placar, start=1):
        print(f"Rodada {i}: {t} tentativa(s)")

    print("Obrigado por jogar!")

jogo_principal()
