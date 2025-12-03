#----------------------------------------------------------
# Project: Knight’s Dance
#
# Date: 03-Dec-2025
# Authors:
#           A01801044 Yael Sinuhe Grajeda Martinez
#           A01800840 Tadeo Emanuel Arellano Conde
#----------------------------------------------------------
from dagor import JugadorCaballosBailadores


class JugadorCaballosBailadoresSimple(JugadorCaballosBailadores):
    """
    Jugador para Caballos bailadores basado en búsqueda minimax
    con profundidad fija y una heurística sencilla de distancias.

    Cambia 'EquipoX' por tu número real de equipo (por ejemplo, Equipo7)
    y guarda este archivo como 'equipoX.py' (por ejemplo, 'equipo7.py').
    """

    def __init__(self, nombre: str) -> None:
        super().__init__(nombre)
        # Profundidad máxima de búsqueda (en medias jugadas / plies)
        self._profundidad_max: int = 4

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
        Elige el mejor tiro usando minimax a profundidad fija.
        """
        posibles = self.posiciones_siguientes(posicion)

        # Si solo hay un tiro posible, no hay nada que pensar
        if len(posibles) == 1:
            return posibles[0]

        mejor_valor = float("-inf")
        mejor_tiro = posibles[0]

        # Maximizamos siempre desde la perspectiva de este jugador
        for tiro in posibles:
            valor = self._minimax(
                tiro,
                self._profundidad_max - 1,
                maximizando=False,      # el siguiente nodo es del oponente
                jugador_max=self
            )
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_tiro = tiro

        return mejor_tiro

    # ------------------------------------------------------------------
    # Implementación interna: minimax + evaluación
    # ------------------------------------------------------------------
    def _minimax(self, posicion, profundidad: int, maximizando: bool, jugador_max) -> float:
        """
        Algoritmo minimax genérico sobre las 'posiciones' del juego Dagor.
        jugador_max es el jugador para el que evaluamos la posición
        (el que llama originalmente a tira).
        """

        # Caso base: juego terminado o se alcanzó la profundidad límite
        if profundidad == 0 or self.juego.juego_terminado(posicion):
            return self._evaluar(posicion, jugador_max)

        hijos = self.posiciones_siguientes(posicion)

        if maximizando:
            valor = float("-inf")
            for hijo in hijos:
                valor_hijo = self._minimax(hijo, profundidad - 1, False, jugador_max)
                if valor_hijo > valor:
                    valor = valor_hijo
            return valor
        else:
            valor = float("inf")
            for hijo in hijos:
                valor_hijo = self._minimax(hijo, profundidad - 1, True, jugador_max)
                if valor_hijo < valor:
                    valor = valor_hijo
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

        # 1. Comprobamos si hay ganador (valor "muy grande")
        if jugador_max.triunfo(posicion) == jugador_max.simbolo:
            # Ganamos
            return 10_000.0

        if jugador_max.contrario.triunfo(posicion) == jugador_max.contrario.simbolo:
            # Perdimos
            return -10_000.0

        # 2. Heurística intermedia (nadie ha ganado todavía)
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

        def dist(a, b) -> int:
            # Distancia manhattan simple
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        max_dist = (rens - 1) + (cols - 1)

        # Queremos estar cerca del rey enemigo
        d_mi_caballo_a_rey_enemigo = dist(mi_caballo, rey_enemigo)
        # Queremos que el caballo enemigo esté lejos de nuestro rey
        d_caballo_enemigo_a_mi_rey = dist(caballo_enemigo, mi_rey)
        # También que esté lejos de nuestro caballo (para no ser cazados)
        d_caballo_enemigo_a_mi_caballo = dist(caballo_enemigo, mi_caballo)

        # Score base
        score = 0.0

        # Entre más cerca estemos del rey enemigo, mejor
        score += (max_dist - d_mi_caballo_a_rey_enemigo) * 3.0

        # Entre más lejos esté el caballo enemigo de nuestro rey, mejor
        score += d_caballo_enemigo_a_mi_rey * 2.0

        # Entre más lejos esté el caballo enemigo de nuestro caballo, mejor
        score += d_caballo_enemigo_a_mi_caballo * 1.0

        # Pequeño ajuste a favor del jugador que tiene el turno,
        # para desempatar situaciones simétricas
        if turno == jugador_max.simbolo:
            score += 0.5

        return score
    
from dagor import JuegoCaballosBailadores, JugadorCaballosBailadoresAleatorio
from equipo2 import JugadorCaballosBailadoresSimple  # ajusta X

if __name__ == '__main__':
    juego = JuegoCaballosBailadores(
        JugadorCaballosBailadoresSimple('Equipo 2'),
        JugadorCaballosBailadoresAleatorio('RandomBoy'),
        5, 8
    )
    juego.inicia(veces=20, delta_max=2)
