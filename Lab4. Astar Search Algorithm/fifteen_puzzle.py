#----------------------------------------------------------
# Lab #4: A* Search Algorithm
# Solving the 15 puzzle.
#
# Date: 10-Oct-2025
# Authors:
#           A01801044 Yael Sinuhe Grajeda Martinez
#           A01800840 Tadeo Emanuel Arellano Conde
#----------------------------------------------------------

# File: fifteen_puzzle.py

from generic_search import astar, Node, node_to_path

type Frame = tuple[tuple[int, ...], ...]

def solve_puzzle(frame: Frame) -> None:
    result: Node[Frame] | None = astar(
        frame, goal_test, successors, heuristic)
    
    if result is None:
        print("No solution found")
        return

    path = node_to_path(result)
    steps = len(path) - 1
    word = "step" if steps == 1 else "steps"
    print(f"Solution requires {steps} {word}")
    for i in range(steps):
        print(f"Step {i + 1}: {_describe_move(path[i], path[i + 1])}")


GOAL: Frame = (
    (1, 2, 3, 4),
    (5, 6, 7, 8),
    (9, 10, 11, 12),
    (13, 14, 15, 0),
)


def goal_test(frame: Frame) -> bool:
    return frame == GOAL


def successors(frame: Frame) -> list[Frame]:
    r, c = next(
        (i, j)
        for i, row in enumerate(frame)
        for j, v in enumerate(row)
        if v == 0
    )

    def swap(r1: int, c1: int, r2: int, c2: int) -> Frame:
        grid: list[list[int]] = [list(row) for row in frame]
        grid[r1][c1], grid[r2][c2] = grid[r2][c2], grid[r1][c1]
        return tuple(tuple(row) for row in grid)

    neighbors: list[Frame] = []

    if r > 0:
        neighbors.append(swap(r, c, r - 1, c))
    if r < 3:
        neighbors.append(swap(r, c, r + 1, c))
    if c > 0:
        neighbors.append(swap(r, c, r, c - 1))
    if c < 3:
        neighbors.append(swap(r, c, r, c + 1))
    return neighbors


def heuristic(frame: Frame) -> float:
    mismatches = 0
    for r in range(4):
        for c in range(4):
            if frame[r][c] != GOAL[r][c]:
                mismatches += 1
    return float(mismatches)


def _find_blank(frame: Frame) -> tuple[int, int]:
    for i, row in enumerate(frame):
        for j, v in enumerate(row):
            if v == 0:
                return i, j
    raise ValueError("No blank tile found.")


def _describe_move(prev: Frame, nxt: Frame) -> str:
    r0, c0 = _find_blank(prev)
    r1, c1 = _find_blank(nxt)
    dr, dc = r1 - r0, c1 - c0

    if dr == -1 and dc == 0:        
        tile, direction = prev[r0 - 1][c0], "down"
    elif dr == 1 and dc == 0:        
        tile, direction = prev[r0 + 1][c0], "up"
    elif dr == 0 and dc == -1:       
        tile, direction = prev[r0][c0 - 1], "right"
    elif dr == 0 and dc == 1:        
        tile, direction = prev[r0][c0 + 1], "left"
    else:
        raise ValueError("Frames are not one legal move apart.")
    return f"Move {tile} {direction}"


if __name__ == "__main__":
    solve_puzzle((
        (2, 3, 4, 8),
        (1, 5, 7, 11),
        (9, 6, 12, 15),
        (13, 14, 10, 0),
    ))