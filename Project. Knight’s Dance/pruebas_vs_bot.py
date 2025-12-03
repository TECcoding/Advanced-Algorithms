# pruebas_vs_bot.py
#
# Prueba JugadorCaballosBailadoresSimple y JugadorCaballosBailadoresAlphaBeta
# contra JugadorCaballosBailadoresAleatorio durante muchas partidas.

from dagor import JuegoCaballosBailadores, JugadorCaballosBailadoresAleatorio
from equipo2 import JugadorCaballosBailadoresSimple
from equipo2T import JugadorCaballosBailadoresAlphaBeta


def simple_vs_random(
    veces: int = 100,
    rens: int = 5,
    cols: int = 8,
    delta_max: float = 2.0,
) -> None:
    """
    Mide el desempeño del jugador Simple contra un jugador aleatorio.
    Dagor imprime cuántas partidas gana cada uno.

    :param veces: número de partidas a jugar
    :param rens: filas del tablero
    :param cols: columnas del tablero
    :param delta_max: tiempo máximo por jugada (segundos)
    """
    juego = JuegoCaballosBailadores(
        JugadorCaballosBailadoresSimple("Simple"),
        JugadorCaballosBailadoresAleatorio("RandomBoy"),
        rens,
        cols,
    )
    juego.inicia(veces=veces, delta_max=delta_max)


def alphabeta_vs_random(
    veces: int = 100,
    rens: int = 5,
    cols: int = 8,
    delta_max: float = 2.0,
) -> None:
    """
    Mide el desempeño del jugador AlphaBeta contra un jugador aleatorio.
    Dagor imprime cuántas partidas gana cada uno.

    :param veces: número de partidas a jugar
    :param rens: filas del tablero
    :param cols: columnas del tablero
    :param delta_max: tiempo máximo por jugada (segundos)
    """
    juego = JuegoCaballosBailadores(
        JugadorCaballosBailadoresAlphaBeta("AlphaBeta"),
        JugadorCaballosBailadoresAleatorio("RandomBoy"),
        rens,
        cols,
    )
    juego.inicia(veces=veces, delta_max=delta_max)


if __name__ == "__main__":
    # print("=== Simple vs RandomBoy ===")
    # simple_vs_random(veces=100, rens=5, cols=8, delta_max=2.0)

    print("\n=== AlphaBeta vs RandomBoy ===")
    alphabeta_vs_random(veces=100, rens=5, cols=8, delta_max=2.0)
