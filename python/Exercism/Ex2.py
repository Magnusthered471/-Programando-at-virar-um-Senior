"""
Funções usadas no preparo da lasanha de Guido.

Este é um docstring de módulo: serve para explicar o que o arquivo faz.
"""

# Constantes são valores fixos que usamos no programa.
# Aqui definimos o tempo total esperado de forno e o tempo de preparo por camada.
EXPECTED_BAKE_TIME = 40   # tempo total de forno em minutos
PREPARATION_TIME = 2      # tempo de preparo por camada em minutos


def bake_time_remaining(elapsed_bake_time):
    """
    Calcula o tempo de forno restante.

    Parâmetros:
        elapsed_bake_time (int): tempo já decorrido no forno.

    Retorna:
        int: tempo restante de forno em minutos.
    """
    # Fórmula: tempo restante = tempo esperado - tempo já decorrido
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(layers):
    """
    Calcula o tempo de preparo da lasanha.

    Parâmetros:
        layers (int): número de camadas da lasanha.

    Retorna:
        int: tempo total de preparo em minutos.
    """
    # Fórmula: tempo de preparo = número de camadas * tempo por camada
    return layers * PREPARATION_TIME


def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """
    Calcula o tempo total já gasto (preparo + forno).

    Parâmetros:
        layers (int): número de camadas da lasanha.
        elapsed_bake_time (int): tempo já decorrido no forno.

    Retorna:
        int: tempo total em minutos.
    """
    # Fórmula: tempo total = tempo de preparo + tempo de forno decorrido
    return preparation_time_in_minutes(layers) + elapsed_bake_time

print(bake_time_remaining(30))          # saída: 10 minutos restantes
print(preparation_time_in_minutes(3))   # saída: 6 minutos de preparo
print(elapsed_time_in_minutes(3, 20))   # saída: 26 minutos totais
