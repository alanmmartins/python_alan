import random

palavras = ['python', 'programacao', 'jogo', 'computador', 'internet']
palavra_secreta = random.choice(palavras)

letras_erradas = ''
letras_certas = ''

while True:
    # Mostra o estado atual da palavra
    estado_atual = ''
    for letra in palavra_secreta:
        if letra in letras_certas:
            estado_atual += letra
        else:
            estado_atual += '_'
    print(estado_atual)
    
    # Pede ao jogador para escolher uma letra
    palpite = input("Digite uma letra: ")
    
    # Verifica se a letra já foi escolhida antes
    if palpite in letras_certas or palpite in letras_erradas:
        print("Você já escolheu essa letra antes. Tente novamente.")
    elif palpite in palavra_secreta:
        print("Correto!")
        letras_certas += palpite
        if len(letras_certas) == len(set(palavra_secreta)):
            print("Parabéns, você ganhou!")
            break
    else:
        print("Incorreto!")
        letras_erradas += palpite
        if len(letras_erradas) == 6:
            print("Você perdeu. A palavra secreta era", palavra_secreta)
            break