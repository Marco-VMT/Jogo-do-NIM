# Jogo do NIM

Este é um jogo de NIM implementado em Python, onde o jogador e o computador se alternam para remover peças de um tabuleiro, com o objetivo de evitar ser o último a retirar as peças.

## Descrição do Jogo

No Jogo do NIM, as regras são as seguintes:
- Há um número inicial de peças no tabuleiro.
- Cada jogador, na sua vez, deve retirar entre 1 e um número máximo permitido de peças.
- O vencedor é aquele que deixa o adversário sem jogadas válidas.

## Funcionalidades

- **Partida isolada**: permite jogar uma única partida contra o computador.
- **Campeonato**: disputa três rodadas contra o computador, com pontuação total exibida ao final.
- **Escolha inteligente do computador**: o computador calcula a melhor jogada para otimizar suas chances de vitória.
- **Validação de entrada**: garante que o jogador escolha uma quantidade válida de peças.

## Como Jogar

Para iniciar o jogo, o usuário escolhe:
1. **Partida isolada** - uma única partida.
2. **Campeonato** - uma série de três partidas, onde o placar total será exibido ao final.

### Regras

1. O número inicial de peças é escolhido pelo usuário.
2. O limite de peças que podem ser removidas por jogada também é definido pelo usuário.
3. O jogo define quem começa, dependendo do número inicial de peças e do limite de peças por jogada.

Durante cada turno, o usuário deve escolher quantas peças retirar (respeitando o limite máximo permitido), e o computador joga em seguida.

## Exemplo de Uso

Ao iniciar o programa, o jogador é solicitado a escolher entre uma partida isolada ou um campeonato. Em seguida, define o número de peças iniciais e o limite por jogada.

Durante o jogo, o computador ou o jogador removerá as peças conforme a lógica implementada para otimizar suas chances de vitória.
