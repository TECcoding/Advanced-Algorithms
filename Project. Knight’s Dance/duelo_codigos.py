# duelo_codigos.py
#
# Prueba JugadorCaballosBailadoresSimple vs JugadorCaballosBailadoresAlphaBeta
# en muchas partidas y deja que Dagor imprima el resumen de victorias.

from dagor import JuegoCaballosBailadores
from equipo2 import JugadorCaballosBailadoresSimple
from equipo2T import JugadorCaballosBailadoresAlphaBeta


def duelo_simple_vs_alphabeta(
    veces: int = 100,
    rens: int = 5,
    cols: int = 8,
    delta_max: float = 2.0,
) -> None:
    """
    Enfrenta al jugador Simple contra AlphaBeta durante `veces` partidas.
    Dagor se encarga de alternar quién empieza y al final imprime el marcador.

    :param veces: número de partidas a jugar
    :param rens: número de renglones (filas) del tablero
    :param cols: número de columnas del tablero
    :param delta_max: tiempo máximo por jugada (segundos)
    """
    juego = JuegoCaballosBailadores(
        JugadorCaballosBailadoresSimple("Simple"),
        JugadorCaballosBailadoresAlphaBeta("AlphaBeta"),
        rens,
        cols,
    )

    # Dagor corre `veces` partidas y al final imprime cuántas ganó cada uno.
    juego.inicia(veces=veces, delta_max=delta_max)


if __name__ == "__main__":
    # Cambia aquí el número de partidas que quieras
    print("=== Duelo Simple vs AlphaBeta ===")
    duelo_simple_vs_alphabeta(veces=200, rens=5, cols=8, delta_max=2.0)
