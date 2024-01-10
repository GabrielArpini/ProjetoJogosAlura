import random
from termcolor import colored

def jogar():
    print("*******************************************************")
    print("******** Bem vindo ao jogo de forca! --- v1.01 ********")
    print("*******************************************************")

    # Abre o arquivo com as palavras
    with open("filtered_database.txt", "r") as f:
        # Lê o arquivo linha por linha e adiciona cada linha à lista de palavras
        palavras = [line.strip() for line in f]

    # Escolhe uma palavra aleatória da lista
    palavra_secreta = random.choice(palavras)
    acertou = False  # acertou palavra
    enforcou = False  # Perdeu o jogo
    letras_acertadas = []  # letras que o jogador acertou
    erros = 0  # Contador de erros
    chances_max = 5  # Máximo de chances permitidas
    used_letters = []  # letras que já foram usadas pelo jogador

    while not acertou and not enforcou:
        try:
            chute = input("Chute uma letra:").lower()

            # Verifica se o chute é uma letra válida
            if not chute.isalpha():
                raise ValueError("Por favor, insira apenas letras do alfabeto.")
            elif len(chute) > 1:
                raise ValueError("Por favor, insira apenas uma letra.")
            elif chute in used_letters:
                raise ValueError("Essa letra já foi usada. Por favor, escolha outra.")
        except ValueError as e:
            # Exibe a mensagem de erro em vermelho e volta ao início do loop
            print(colored(e, "red"))
            continue

        if chute in palavra_secreta:
            letras_acertadas.append(chute)
            used_letters.append(chute)  # adiciona a letra à lista de letras usadas
        else:
            print("Você errou!")
            erros += 1  # Incrementa o contador de erros

        # Verifica se o jogador enforcou
        if erros == chances_max:
            enforcou = True
            continue

        # Calcula as chances restantes
        chances_restantes = chances_max - erros

        # Mostra o progresso atual do jogador e as chances restantes
        progresso = "".join([l if l in letras_acertadas else "_" for l in palavra_secreta])
        print(f"{progresso} ({chances_restantes} chances restantes)")

        # Verifica se o jogador acertou todas as letras
        if all(l in letras_acertadas for l in palavra_secreta):
            acertou = True

    if acertou:
        print(colored("Parabéns, você acertou a palavra secreta!", "green"))
    else:
        # Exibe a mensagem de derrota em vermelho
        print(colored("Você perdeu! A palavra secreta era: {}".format(palavra_secreta), "red"))



    while True:
        novo_jogo = input("Deseja jogar novamente? (s/n)").lower()
        if novo_jogo == "s":
            jogar()
        elif novo_jogo == "n":
            print("Obrigado por jogar!")
            break
        else:
            print("Por favor, insira 's' para jogar novamente ou 'n' para sair.")