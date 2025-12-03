#----------------------------------------------------------
# Project: Knight’s Dance
#
# Date: 03-Dec-2025
# Authors:
#           A01801044 Yael Sinuhe Grajeda Martinez
#           A01800840 Tadeo Emanuel Arellano Conde
#----------------------------------------------------------
from collections import deque

from dagor import JugadorCaballosBailadores


class JugadorCaballosBailadoresAlphaBeta(JugadorCaballosBailadores):
    """
    Jugador para Caballos bailadores basado en minimax con
    poda alfa-beta y heurística orientada a capturas y movilidad.

    Cambia 'EquipoX' por tu número real de equipo (por ejemplo, Equipo2)
    y guarda este archivo como 'equipoX.py' (por ejemplo, 'Equipo2.py').
    """

    def __init__(self, nombre: str) -> None:
        super().__init__(nombre)
        self._profundidad_max: int = 5
        self._memo = {}
        self._dist_cache = {}

    # ------------------------------------------------------------------
    # Interfaz requerida por Dagor
    # ------------------------------------------------------------------
    def heuristica(self, posicion) -> float:
        """
        Función heurística que evalúa la 'bondad' de una posición
        desde el punto de vista de ESTE jugador.
        """
        return self._evaluar(posicion, self)

    def tira(self, posicion):
        """
        Elige el mejor tiro usando minimax con poda alfa-beta.
        """
        self._memo = {}
        posibles = list(self.posiciones_siguientes(posicion))

        if len(posibles) == 1:
            return posibles[0]

        mejor_valor = float("-inf")
        mejor_tiro = posibles[0]
        alpha = float("-inf")
        beta = float("inf")

        posibles.sort(key=lambda p: self._evaluar(p, self), reverse=True)

        for tiro in posibles:
            valor = self._minimax(
                tiro,
                self._profundidad_max - 1,
                maximizando=False,
                jugador_max=self,
                alpha=alpha,
                beta=beta
            )
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_tiro = tiro
            alpha = max(alpha, valor)
            if beta <= alpha:
                break

        return mejor_tiro

    # ------------------------------------------------------------------
    # Implementación interna: minimax + evaluación
    # ------------------------------------------------------------------
    def _minimax(
        self,
        posicion,
        profundidad: int,
        maximizando: bool,
        jugador_max,
        alpha: float,
        beta: float,
    ) -> float:
        """
        Algoritmo minimax genérico sobre las 'posiciones' del juego Dagor.
        jugador_max es el jugador para el que evaluamos la posición
        (el que llama originalmente a tira).
        """
        llave = (posicion, profundidad, maximizando)
        if llave in self._memo:
            return self._memo[llave]

        if profundidad == 0 or self.juego.juego_terminado(posicion):
            return self._evaluar(posicion, jugador_max)

        hijos = list(self.posiciones_siguientes(posicion))

        hijos.sort(
            key=lambda p: self._evaluar(p, jugador_max),
            reverse=maximizando
        )

        if maximizando:
            valor = float("-inf")
            for hijo in hijos:
                valor_hijo = self._minimax(
                    hijo, profundidad - 1, False, jugador_max, alpha, beta
                )
                valor = max(valor, valor_hijo)
                alpha = max(alpha, valor)
                if beta <= alpha:
                    break
        else:
            valor = float("inf")
            for hijo in hijos:
                valor_hijo = self._minimax(
                    hijo, profundidad - 1, True, jugador_max, alpha, beta
                )
                valor = min(valor, valor_hijo)
                beta = min(beta, valor)
                if beta <= alpha:
                    break

        self._memo[llave] = valor
        return valor

    # ------------------------------------------------------------------
    # Heurística
    # ------------------------------------------------------------------
    def _evaluar(self, posicion, jugador_max) -> float:
        """
        Evalúa la posición desde el punto de vista de jugador_max.

        Posición: (T, rens, cols, rB, rN, cB, cN)
        """

        turno, rens, cols, rB, rN, cB, cN = posicion

        if jugador_max.triunfo(posicion) == jugador_max.simbolo:
            return 10_000.0

        if jugador_max.contrario.triunfo(posicion) == jugador_max.contrario.simbolo:
            return -10_000.0

        if jugador_max.simbolo == 'B':
            mi_rey = rB
            mi_caballo = cB
            rey_enemigo = rN
            caballo_enemigo = cN
        else:
            mi_rey = rN
            mi_caballo = cN
            rey_enemigo = rB
            caballo_enemigo = cB

        mis_movs = self._knight_moves(mi_caballo, rens, cols, mi_rey)
        movs_enemigo = self._knight_moves(caballo_enemigo, rens, cols, rey_enemigo)

        if rey_enemigo in mis_movs:
            return 9_000.0
        if mi_rey in movs_enemigo:
            return -9_000.0
        if caballo_enemigo in mis_movs:
            return 2_000.0
        if mi_caballo in movs_enemigo:
            return -2_000.0

        dist_mi_a_rey_enemigo = self._knight_distance(mi_caballo, rey_enemigo, rens, cols)
        dist_mi_a_caballo_enemigo = self._knight_distance(mi_caballo, caballo_enemigo, rens, cols)
        dist_enemigo_a_mi_rey = self._knight_distance(caballo_enemigo, mi_rey, rens, cols)
        dist_enemigo_a_mi_caballo = self._knight_distance(caballo_enemigo, mi_caballo, rens, cols)

        movilidad = len(mis_movs) - len(movs_enemigo)

        centro_r = (rens - 1) / 2
        centro_c = (cols - 1) / 2
        dist_centro_mi = abs(mi_caballo[0] - centro_r) + abs(mi_caballo[1] - centro_c)
        dist_centro_enemigo = abs(caballo_enemigo[0] - centro_r) + abs(caballo_enemigo[1] - centro_c)

        score = 0.0

        score += (8 - dist_mi_a_rey_enemigo) * 80
        score += (6 - dist_mi_a_caballo_enemigo) * 50
        score -= (8 - dist_enemigo_a_mi_rey) * 90
        score -= (6 - dist_enemigo_a_mi_caballo) * 55

        score += movilidad * 25
        score += (dist_centro_enemigo - dist_centro_mi) * 5

        if turno == jugador_max.simbolo:
            score += 5.0

        return score

    def _knight_moves(self, coord, rens, cols, forbidden=None):
        """Devuelve las casillas a las que puede brincar el caballo."""
        resultado = []
        row, col = coord
        for dr in (-2, -1, 1, 2):
            for dc in (-2, -1, 1, 2):
                if abs(dr) == abs(dc):
                    continue
                nr = row + dr
                nc = col + dc
                if 0 <= nr < rens and 0 <= nc < cols:
                    if forbidden is None or (nr, nc) != forbidden:
                        resultado.append((nr, nc))
        return resultado

    def _knight_distance(self, start, goal, rens, cols):
        """Calcula distancia en saltos de caballo con BFS corta y memo."""
        if start == goal:
            return 0
        key = (start, goal, rens, cols)
        if key in self._dist_cache:
            return self._dist_cache[key]

        visited = set([start])
        q = deque([(start, 0)])
        while q:
            (r, c), d = q.popleft()
            for nxt in self._knight_moves((r, c), rens, cols):
                if nxt == goal:
                    self._dist_cache[key] = d + 1
                    return d + 1
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, d + 1))

        self._dist_cache[key] = rens * cols
        return self._dist_cache[key]
    
if __name__ == '__main__':
    from dagor import JuegoCaballosBailadores, JugadorCaballosBailadoresAleatorio

    juego = JuegoCaballosBailadores(
        JugadorCaballosBailadoresAlphaBeta('Equipo 2'),
        JugadorCaballosBailadoresAleatorio('RandomBoy'),
        5, 8
    )
    juego.inicia(veces=20, delta_max=2)