import enum
import heapq
import typing

from collections.abc import Callable


Heuristics = Callable[[str], int]


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

    def has_solution(self) -> bool:
        inversion_count = 0
        numbers = [ch for ch in self._state if ch != self.BLANK_CHAR]

        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] > numbers[j]:
                    inversion_count += 1

        return inversion_count % 2 == 0

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
    _ACTION_COST: typing.Final[int] = 1

    def __init__(
        self,
        estado: str,
        pai: typing.Self | None,
        acao: str | None,
        custo: int,
        heuristica: Heuristics | None = None,
    ) -> None:
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        if pai is not None and acao is None:
            raise ValueError("'acao' não pode ser None para nó não raíz.")

        self._state = estado
        self._parent = pai
        self._action = Action(acao) if acao is not None else None
        self._cost = custo
        self._heuristics = heuristica

        if heuristica is not None:
            self._total_cost = heuristica(estado) + custo
        else:
            self._total_cost = custo

    @property
    def estado(self) -> str:
        return self._state

    @property
    def is_objective_state(self) -> bool:
        return self._state == PuzzleState.OBJECTIVE_STATE

    @property
    def pai(self) -> typing.Self | None:
        return self._parent

    @property
    def acao(self) -> str | None:
        if self._action is None:
            return None
        return self._action.value

    @property
    def custo(self) -> int:
        return self._cost

    @property
    def custo_total(self) -> int:
        return self._total_cost

    def collect_all_actions(self) -> list[str]:
        actions: list[str] = []
        node = self

        while node.pai is not None:
            if node._action is None:
                raise ValueError("'acao' não pode ser None para nó não raíz.")

            actions.append(node._action.value)
            node = node.pai

        actions.reverse()
        return actions

    def filhos(self) -> set[typing.Self]:
        return {
            self._make_child(action, next_state, parent=self)
            for action, next_state in sucessor(self._state)
        }

    @classmethod
    def _make_child(
        cls, action: str, state: str, *, parent: typing.Self
    ) -> typing.Self:
        return cls(
            estado=state,
            acao=action,
            pai=parent,
            custo=parent._cost + cls._ACTION_COST,
            heuristica=parent._heuristics,
        )

    def __lt__(self, other: typing.Self) -> bool:
        if self.custo_total == other.custo_total:
            return self.estado < other.estado
        return self.custo_total < other.custo_total

    def __le__(self, other: typing.Self) -> bool:
        return self.custo_total <= other.custo_total

    def __gt__(self, other: typing.Self) -> bool:
        if self.custo_total == other.custo_total:
            return self.estado > other.estado
        return self.custo_total > other.custo_total

    def __ge__(self, other: typing.Self) -> bool:
        return self.custo_total >= other.custo_total

    def __eq__(self, other: typing.Any) -> bool:
        return (
            isinstance(other, Nodo)
            and (self.estado == other.estado)
            and (self.pai is other.pai)
            and (self.acao == other.acao)
            and (self.custo_total == other.custo_total)
        )

    def __hash__(self) -> int:
        return hash((self.estado, id(self.pai), self.acao, self.custo_total))

    def __repr__(self) -> str:
        return f"estado={self.estado} | acao={self.acao} | custo={self.custo} | custo_total={self.custo_total}"


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
    return nodo.filhos()


def astar(state: str, heuristics: Heuristics) -> list[str] | None:
    if not PuzzleState(state).has_solution():
        return None

    root = Nodo(state, pai=None, acao=None, custo=0, heuristica=heuristics)

    seen: set[str] = set()
    border_heap = [root]
    border_map = {root.estado: root}

    heapq.heapify(border_heap)

    while len(border_heap) > 0:
        smaller_cost_node = heapq.heappop(border_heap)
        border_map.pop(smaller_cost_node.estado, None)

        if smaller_cost_node.estado in seen:
            continue

        if smaller_cost_node.is_objective_state:
            return smaller_cost_node.collect_all_actions()

        seen.add(smaller_cost_node.estado)
        for child in smaller_cost_node.filhos():
            if child.estado in seen:
                continue

            if child.estado not in border_map:
                border_map[child.estado] = child
                heapq.heappush(border_heap, child)
                continue

            child_in_border = border_map[child.estado]
            if child.custo_total < child_in_border.custo_total:
                border_heap.remove(child_in_border)
                heapq.heapify(border_heap)

                border_map[child.estado] = child
                heapq.heappush(border_heap, child)
    return None


def hamming_distance(state: str) -> int:
    assert len(state) == len(PuzzleState.OBJECTIVE_STATE)

    distance = 0
    for char, target_char in zip(state, PuzzleState.OBJECTIVE_STATE):
        if char == PuzzleState.BLANK_CHAR:
            continue
        if char != target_char:
            distance += 1
    return distance


def astar_hamming(estado: str) -> list[str] | None:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    return astar(estado, heuristics=hamming_distance)


def astar_manhattan(estado: str) -> list[str] | None:
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
