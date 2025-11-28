# Trabalho 4 - Busca com adversário

Integrantes:

- (00314477)(Turma B) Andreas Emilio Panzenhagen Franz
- (00343701)(Turma B) Clara Schons Theisen
- (00314943)(Turma B) Matheus Luís de Castro


## Avaliação

a. Tic-Tac-Toe misere
- O minimax nunca perde para o random player, independente se começa jogando ou não, na maioria das vezes ganha mas tem uma boa quantidade de empates.

- O minimax sempre empata contra ele mesmo.

- Não conseguimos ganhar do minimax, independete de quem começa jogando, ele sempre faz as melhores jogadas e nós acabamos empatando ou perdendo.

- A partir das evidências relatadas, concluímos que o minimax está sim jogando perfeitamente.


b. Mini Torneio de Heurísticas para o jogo Othello

- Contagem de peças X Valor posicional:
 Ganhou o player com a heurística de Valor posicional, com 36 peças contra 28 peças do player com a heurística de Contagem de peças.

- Valor posicional X Contagem de peças:
 Ganhou o player com a heurística de Valor posicional, com 40 peças contra 24 peças do player com a heurística de Contagem de peças.

- Contagem de peças X Heurística customizada:
 Ganhou o player com a heurística customizada, com 39 peças contra 25 peças do player com a heurística de Contagem de peças.

- Heurística customizada X Contagem de peças:
 Ganhou o player com a heurística customizada, com 53 peças contra 11 peças do player com a heurística de Contagem de peças.

- Valor posicional X Heurística customizada:
 Ganhou o player com a heurística customizada, com 44 peças contra 20 peças do player com a heurística de Valor posicional.

- Heurística customizada X Valor posicional:
 Ganhou o player com a heurística customizada, com 46 peças contra 17 peças do player com a heurística de Valor posicional.


## Heurística Customizada

Esta heurística avalia um estado de Othello com base em múltiplos fatores:

1. Diferença de peças: A diferença entre o número de peças do jogador e do oponente.
2. Mobilidade: A diferença no número de movimentos legais disponíveis para o jogador e o oponente.
3. Canto: A posse dos cantos do tabuleiro.
4. Borda: A posse das bordas do tabuleiro.

A heurística atribui pesos diferentes a cada um desses fatores, ajustando-os com base no número de posições vazias restantes.
Essa heurística foi projetada usando os links abaixo como referência e também utilizando a LLM GitHub Copilot.
A ideia de variar os pesos com base no número de posições vazias foi ideia original do grupo.

A heurística tem um critério de parada por profundidade máxima fixa, que no nosso caso é 4.

Esta é a heurística que foi escolhida pelo grupo para ser utilizada no Torneio de Othello da turma.

Referências:

- https://www.cs.cornell.edu/~yuli/othello/othello.html
- http://home.datacomm.ch/t_wolf/tw/misc/reversi/html/index.html
- https://kartikkukreja.wordpress.com/2013/03/30/heuristic-function-for-reversiothello/"
