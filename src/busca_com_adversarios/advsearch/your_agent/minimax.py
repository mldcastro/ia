import random
from typing import Optional, Tuple, Callable

def fmax(
        state, 
        depth: int,
        alpha: float, 
        beta: float, 
        eval_func: Callable
        ) -> Tuple[float, Optional[Tuple[int, int]]]:
    """
    Max function of the minimax algorithm with alpha-beta pruning.
    :param state: current game state
    :param depth: current depth of search (-1 = unlimited)
    :param alpha: alpha value for pruning
    :param beta: beta value for pruning
    :param eval_func: function to evaluate the game state
    :return: a tuple containing the maximum value and the corresponding move
    """
    if (depth == 0 or state.is_terminal()):
        return eval_func(state, "B"), None
    
    value: float = -float('inf')
    best_move: Optional[Tuple[int, int]] = None
    updated_depth: int = depth

    if depth != -1:
        updated_depth = depth - 1

    for move in state.legal_moves():
        new_state = state.next_state(move)
        new_value, _ = fmin(new_state, updated_depth, alpha, beta, eval_func)
        if new_value > value:
            value = new_value
            best_move = move
        alpha = max(alpha, value)
        if beta <= alpha:
            break

    return value, best_move

def fmin(
        state, 
        depth: int,
        alpha: float, 
        beta: float, 
        eval_func: Callable
        ) -> Tuple[float, Optional[Tuple[int, int]]]:
    """
    Min function of the minimax algorithm with alpha-beta pruning.
    :param state: current game state
    :param depth: current depth of search (-1 = unlimited)
    :param alpha: alpha value for pruning
    :param beta: beta value for pruning
    :param eval_func: function to evaluate the game state
    :return: a tuple containing the maximum value and the corresponding move
    """
    if (depth == 0 or state.is_terminal()):
        return eval_func(state, "W"), None
    
    value: float = float('inf')
    best_move: Optional[Tuple[int, int]] = None
    updated_depth: int = depth

    if depth != -1:
        updated_depth = depth - 1

    for move in state.legal_moves():
        new_state = state.next_state(move)
        new_value, _ = fmax(new_state, updated_depth, alpha, beta, eval_func)
        if new_value < value:
            value = new_value
            best_move = move
        beta = min(beta, value)
        if beta <= alpha:
            break
        
    return value, best_move

def minimax_move(state, max_depth:int, eval_func:Callable) -> Tuple[int, int]:
    """
    Returns a move computed by the minimax algorithm with alpha-beta pruning for the given game state.
    :param state: state to make the move (instance of GameState)
    :param max_depth: maximum depth of search (-1 = unlimited)
    :param eval_func: the function to evaluate a terminal or leaf state (when search is interrupted at max_depth)
                    This function should take a GameState object and a string identifying the player,
                    and should return a float value representing the utility of the state for the player.
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    move: Optional[Tuple[int, int]] = None
    _ , move = fmax(state, max_depth, alpha=-float('inf'), beta=float('inf'), eval_func=eval_func)
    return move
