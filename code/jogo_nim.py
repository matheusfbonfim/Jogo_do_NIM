def computador_escolhe_jogada(n,m):
    """
    - Se n for igual a m, tira todas as peças.
    - Se o resto da divisão der maior que 1, retirar esse resto para induzir o usuario
      a jogar multiplos de (m+1)
    - Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.
    """
    if n == m:
        return n
    else:
        if (n % (m+1)) > 0:
            return n % (m+1)
        else:
            return m

def usuario_escolhe_jogada(n,m):
    """
    - Solicita quantas peças o usuário irá tirar
    - Verifica a validade dos parâmetros
    - Retorna o valor de peças retiradas
    """
    numero = int(input('\nQuantas peças você vai tirar? '))

    while numero > n or numero > m or numero <= 0:
        print("\nOops! Jogada inválida! Tente de novo.")
        numero = int(input("\nQuantas peças você vai tirar? "))
    return numero

def partida():
    n = int(input("\nQuantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    vez = None
    retirada = 0

    while m < 1:
        print("O limite de peças é inválido. O limite de peças deve ser menor ou igual a quantidade de peças")
        m = int(input("Limite de peças por jogada? "))

    if (n % (m + 1)) == 0:

        print("\nVocê começa!")
        vez = False

        while n > 0:
            if not(vez):
                retirada = usuario_escolhe_jogada(n, m)
                print(f"\nVocê tirou {retirada} peça(s).")
                n = n - retirada
                if n == 0:
                    vez = False
                else:
                    print(f"Agora restam {n} peças no tabuleiro.")
                    vez = True
            else:
                retirada = computador_escolhe_jogada(n, m)
                print(f"\nO computador tirou {retirada} peça(s).")
                n = n - retirada
                if n == 0:
                    vez = True
                else:
                    print(f"Agora restam {n} peças no tabuleiro.")
                    vez = False

        if vez:
            print("Fim do jogo! O computador ganhou!")
            return True
        else:
            print("Fim do jogo! O você ganhou!")
            return False

    else:
        print("\nComputador começa!")
        vez = True # Vez do computador

        while n > 0:
            if vez:
                retirada = computador_escolhe_jogada(n,m)
                print(f"\nO computador tirou {retirada} peça(s).")
                n = n - retirada
                if n == 0:
                    vez = True
                else:
                    vez = False
                    print(f"Agora restam {n} peças no tabuleiro.")
            else:
                retirada = usuario_escolhe_jogada(n, m)
                print(f"\nVocê tirou {retirada} peça(s).")
                n = n - retirada

                if n == 0:
                    vez = False
                else:
                    print(f"Agora restam {n} peças no tabuleiro.")
                    vez = True

        if vez:
            print("Fim do jogo! O computador ganhou!")
            return True
        else:
            print("Fim do jogo! O você ganhou!")
            return False

def campeonato():
    contador_partidas = 0
    contador_computador = 0
    contador_usuario = 0

    while contador_partidas < 3:
        print(f"\n**** Rodada {contador_partidas+1} ****")

        ocorrencia_partida = partida()

        if ocorrencia_partida:
            contador_computador += 1
        else:
            contador_usuario += 1

        contador_partidas += 1

    print(f"\n**** Final do campeonato! ****")
    print(f"\nPlacar: Você {contador_usuario} X {contador_computador} Computador")

def main():

    print("Bem-vindo ao jogo do NIM! Escolha:",end='\n')
    print("\n1 - para jogar uma partida isolada")
    opcao = int(input("2 - para jogar um campeonato "))

    while opcao != 1 and opcao != 2:
        print("Opção Inválida. Tente novamente")
        opcao = int(input("Escolha: "))

    if opcao == 1:
        print("\nVoce escolheu uma partida!")
        partida()
    else:
        print("\nVoce escolheu um campeonato!")
        campeonato()

main()