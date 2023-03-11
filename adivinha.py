import random

numero_secreto = random.randint(1, 100)

print("Tente adivinhar o número secreto (entre 1 e 100)")

while True:
    palpite = int(input("Digite seu palpite: "))
    
    if palpite == numero_secreto:
        print("Parabéns, você acertou!")
        break
    elif palpite < numero_secreto:
        print("O número secreto é maior do que isso. Tente novamente.")
    else:
        print("O número secreto é menor do que isso. Tente novamente.")