def mostra_tabuleiro(tabuleiro):
    print(tabuleiro[0] + "\n" + tabuleiro[1] + "\n" + tabuleiro[2] + "\n")

def jogada_valida(jogada, tabuleiro):
    if jogada in "0123456789":
        jogada = int(jogada)
        if jogada >= 1 and jogada <= 9:
            linha = (jogada - 1) // 3
            coluna = (jogada - 1) % 3
            if tabuleiro[linha][coluna] == " ":
                return True
    return False

def vitoria(tabuleiro, jogador):
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador:
            return True
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador:
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False

def jogo_da_velha():
    tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    jogador_atual = "X"
    jogadas = 0
    while jogadas < 9:
        mostra_tabuleiro(tabuleiro)
        jogada = input("Digite a posição para jogar (1-9): ")
        if jogada_valida(jogada, tabuleiro):
            linha = (int(jogada) - 1) // 3
            coluna = (int(jogada) - 1) % 3
            tabuleiro[linha][coluna] = jogador_atual
            if vitoria(tabuleiro, jogador_atual):
                print(f"{jogador_atual} ganhou!")
                mostra_tabuleiro(tabuleiro)
                return
            jogador_atual = "O" if jogador_atual == "X" else "X"
            jogadas += 1
        else:
            print("Jogada inválida. Tente novamente.")
    print("Empate!")
    mostra_tabuleiro(tabuleiro)