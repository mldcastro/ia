import enum
import typing


class Action(enum.StrEnum):
    UP = "acima"
    DOWN = "abaixo"
    RIGHT = "direita"
    LEFT = "esquerda"


class PuzzleState:
    N_ROWS: typing.Final[int] = 3
    N_COLS: typing.Final[int] = 3
    N_POSITIONS: typing.Final[int] = 9

    OBJECTIVE_STATE: typing.Final[str] = "12345678_"
    BLANK_CHAR: typing.Final[str] = "_"

    _SWAP_MARKER: typing.Final[str] = "X"

    def __init__(self, state: str) -> None:
        self._state = state
        self._blank_index = self._get_blank_index()

    def can_move_to(self, action: Action) -> bool:
        if action is Action.UP:
            return self._get_blank_row() > 0

        if action is Action.DOWN:
            return self._get_blank_row() < (self.N_ROWS - 1)

        if action is Action.LEFT:
            return self._get_blank_col() > 0

        if action is Action.RIGHT:
            return self._get_blank_col() < (self.N_COLS - 1)

        raise NotImplementedError(action)

    def swap(self, action: Action) -> str | None:
        if not self.can_move_to(action):
            return None

        if action is Action.UP:
            target_number = self._state[self._blank_index - self.N_ROWS]
        elif action is Action.DOWN:
            target_number = self._state[self._blank_index + self.N_ROWS]
        elif action is Action.LEFT:
            target_number = self._state[self._blank_index - 1]
        elif action is Action.RIGHT:
            target_number = self._state[self._blank_index + 1]
        else:
            raise NotImplementedError(action)
        return (
            self._state.replace(target_number, self._SWAP_MARKER)
            .replace(self.BLANK_CHAR, target_number)
            .replace(self._SWAP_MARKER, self.BLANK_CHAR)
        )

    def _get_blank_index(self) -> int:
        return self._state.index(self.BLANK_CHAR)

    def _get_blank_row(self) -> int:
        return self._blank_index // self.N_ROWS

    def _get_blank_col(self) -> int:
        return self._blank_index % self.N_COLS


class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """

    def __init__(self, estado: str, pai: Self | None, acao: str | None, custo: int):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        # substitua a linha abaixo pelo seu codigo
        raise NotImplementedError


def sucessor(estado: str) -> set[tuple[str, str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    puzzle_state = PuzzleState(estado)
    successors: set[tuple[str, str]] = set()

    for action in Action:
        next_state = puzzle_state.swap(action)
        if next_state is None:
            continue
        successors.add((action.value, next_state))
    return successors


def expande(nodo: Nodo) -> set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_hamming(estado: str) -> list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado: str) -> list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


# opcional,extra
def bfs(estado: str) -> list[str]:
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


# opcional,extra
def dfs(estado: str) -> list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


# opcional,extra
def astar_new_heuristic(estado: str) -> list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError
