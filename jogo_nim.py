def computador_escolhe_jogada(n,m):
    m_max = m
    m = 1
    if (n - m) % (m_max+1) == 0:
        m = m
    else:
        while (n - m) % (m_max+1) != 0:
            m += 1
            if m == m_max:
                break

    n = n - m

    if m == 1:
        print("O computador tirou uma peça.")
    else:
        print("O computador tirou", m, "peças.")


    if n == 0:
        print ("Fim do jogo! O computador ganhou!")
    else:
        if n ==1:
            print("Agora resta apenas uma peça no tabuleiro.\n")
        else:
            print("Agora restam",n,"peças no tabuleiro,\n")
      
    return m



def usuario_escolhe_jogada(n,m):
    m_max = m    
    m = int(input("Quantas peças você vai tirar? "))

    while ((m <= 0) or (m > m_max) or (m > n)):
        print("\nOops! Jogada inválida! Tende de novo\n")
        m = int(input("Quantas peças você vai tirar? "))
    
    n = n - m
   
    if m == 1:
        print("\nVocê tirou uma peça.")
    else:
        print("\nVocê tirou", m, "peças.")


    if n == 0:
        print ("Fim do jogo! Você ganhou!")    
    else:
        if n ==1:
            print("Agora resta apenas uma peça no tabuleiro.\n")
        else:
            print("Agora restam",n,"peças no tabuleiro.\n")
    
    return m



def partida():
    
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    while m > n:
        print("\nO limite de peças deve sem no máximo a quantidade inicial de peças.\n")
        m = int(input("Limite de peças por jogada? "))
    
    m_max = m
    
    
    if n % (m+1) == 0 and (not (n == m)):
        print ("\nVocê começa!\n")
        while n > 0:
            m = usuario_escolhe_jogada(n,m)                        
            n = n - m
            if n == 0:
                return 1
            else:
                m = m_max                      
                m = computador_escolhe_jogada(n,m)           
                n = n - m
                if n == 0:
                    return 0
                else:
                    m = m_max
            
    else:
            print("\nComputador começa!\n")
            while n > 0:
                m = computador_escolhe_jogada(n,m)              
                n = n - m
                if n == 0:
                    return 0
                else:
                    m = m_max               
                    m = usuario_escolhe_jogada(n,m)   
                    n = n - m
                    if n == 0:
                        return 1
                    else:
                        m = m_max
                    

def main():
    placar_computador = 0
    placar_jogador = 0

    i = 1

    print("\nBem vindo ao jogo do NIM! Escolha:\n")
    entrada = int(input("1 - para jogar uma partida isolada.\n2 - para jogar um campeonato. "))

    while entrada not in (1,2):
        print("\nEntrada inválida! Seleciona 1 ou 2.\n")
        entrada = int(input("1 - para jogar uma partida isolada.\n2 - para jogar um campeonato. "))
    if entrada == 1:
        print("\nVocê escolheu uma partida isolada.")
        print("\n**** Rodada Única ****\n")
        partida()
    else:
        print("\nVocê escolheu um campeonato!\n")
        while i <= 3:           
            print(f"\n**** Rodada {i} ****\n")
            if partida() == 0:
                placar_computador = placar_computador + 1
            else:
                placar_jogador = placar_jogador + 1
            i += 1
        print("\n**** Final do campeonato ****\n")
        print(f"Placar: Você {placar_jogador} X {placar_computador} Computador")


    verificar_novamente = input("\nDeseja jogar novamente? Y/N: ")

    while verificar_novamente not in ("Y", "y", "N", "n"):
        print("Digite 'Y' para jogar novamente e 'N' para encerrar o programa")
        verificar_novamente = input("\nDeseja jogar novamente? Y/N: ")

    return verificar_novamente


# Inicio do programa:

verificar_novamentre = main()


# Repetição do programa:

while verificar_novamentre in ("Y", "y"):
    verificar_novamentre = main()

quit()