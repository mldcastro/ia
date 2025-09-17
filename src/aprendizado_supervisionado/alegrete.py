import numpy as np
import numpy.typing as npt


def compute_mse(b: float, w: float, data: npt.NDArray[np.floating]) -> float:
    """
    Calcula o erro quadratico medio
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """

    input_ = data[:, 0]
    observed = data[:, 1]

    predicted = w * input_ + b
    return np.mean((observed - predicted) ** 2).astype(float)


def step_gradient(
    b: float, w: float, data: npt.NDArray[np.floating], alpha: float
) -> tuple[float, float]:
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de b e w.
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de b e w, respectivamente
    """
    input_vector = data[:, 0]
    input_matrix = np.c_[np.ones_like(input_vector), input_vector]

    observed_vector = data[:, 1]
    parameters_vector = np.array([b, w])

    gradients = (2 / input_vector.shape[0]) * input_matrix.T.dot(
        input_matrix.dot(parameters_vector) - observed_vector
    )

    parameters_vector = parameters_vector - alpha * gradients
    return parameters_vector[0], parameters_vector[1]


def fit(
    data: npt.NDArray[np.floating],
    b: float,
    w: float,
    alpha: float,
    num_iterations: int,
) -> tuple[list[float], list[float]]:
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de b e w.
    Ao final, retorna duas listas, uma com os b e outra com os w
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os b e outra com os w obtidos ao longo da execução
    """
    # inicializa b_history e w_history vazios
    b_history: list[float] = []
    w_history: list[float] = []
    # para cada época
    for _ in range(num_iterations):
        # desce o gradiente
        b, w = step_gradient(b, w, data, alpha)
        # append b em b_history
        # append w em w_history
        b_history.append(b)
        w_history.append(w)

    return b_history, w_history
