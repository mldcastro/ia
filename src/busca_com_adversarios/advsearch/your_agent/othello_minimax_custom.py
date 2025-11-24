from typing import Tuple

from ..othello.gamestate import GameState
from .othello_minimax_count import evaluate_count
from .minimax import minimax_move

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


_N_POSITIONS = 8 * 8


def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    return minimax_move(state, max_depth=4, eval_func=evaluate_custom)


def evaluate_custom(state: GameState, player: str) -> float:
    """
    Esta heurística avalia um estado de Othello com base em múltiplos fatores:
        1. Diferença de peças: A diferença entre o número de peças do jogador e do oponente.
        2. Mobilidade: A diferença no número de movimentos legais disponíveis para o jogador e o oponente.
        3. Canto: A posse dos cantos do tabuleiro.
        4. Borda: A posse das bordas do tabuleiro.
    A heurística atribui pesos diferentes a cada um desses fatores, ajustando-os com base no número de posições vazias restantes.

    Essa heurística foi projetada usando os links abaixo como referência e também utilizando a LLM GitHub Copilot.
    A ideia de variar os pesos com base no número de posições vazias foi ideia original do grupo.

    Referências:
        - https://www.cs.cornell.edu/~yuli/othello/othello.html
        - http://home.datacomm.ch/t_wolf/tw/misc/reversi/html/index.html
        - https://kartikkukreja.wordpress.com/2013/03/30/heuristic-function-for-reversiothello/

    :param state: state to evaluate (instance of GameState)
    :param player: player to evaluate the state for (B or W)
    """
    if state.is_terminal():
        winner = state.winner()
        if winner is None:
            return 0.0
        elif winner == player:
            return float("inf")
        else:
            return float("-inf")

    board = state.get_board()

    opponent = board.opponent(player)
    player_moves = board.legal_moves(player)
    opponent_moves = board.legal_moves(opponent)

    n_empty = _N_POSITIONS - board.num_pieces(player) - board.num_pieces(opponent)
    empty_factor = max(1, n_empty)

    piece_diff = evaluate_count(state, player)
    mobility_diff = len(player_moves) - len(opponent_moves)

    corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
    corner_score = 0
    for x, y in corners:
        owner = board.tiles[y][x]
        if owner == player:
            corner_score += 1
        elif owner == opponent:
            corner_score -= 1

    edge_score = 0
    for i in range(8):
        for x, y in ((0, i), (7, i), (i, 0), (i, 7)):
            owner = board.tiles[y][x]
            if owner == player:
                edge_score += 1
            elif owner == opponent:
                edge_score -= 1

    weight_pieces = 110 * (1 / empty_factor)
    weight_mobility = 200 * (1 / empty_factor)
    weight_corner = 250
    weight_edge = 40

    return (
        weight_pieces * piece_diff
        + weight_mobility * mobility_diff
        + weight_corner * corner_score
        + weight_edge * edge_score
    )
