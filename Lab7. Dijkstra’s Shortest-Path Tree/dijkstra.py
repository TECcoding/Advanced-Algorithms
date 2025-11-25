#----------------------------------------------------------
# Lab #7: Dijkstra’s Shortest-Path Tree
#
# Date: 26-Nov-2025
# Authors:
#           A01801044 Yael Sinuhe Grajeda Martinez
#           A01800840 Tadeo Emanuel Arellano Conde
#----------------------------------------------------------
# File: dijkstra.py

from __future__ import annotations
from math import inf

type WeightedGraph = dict[str, set[tuple[str, float]]]

def dijkstra_spt(
        initial: str,
        graph: WeightedGraph) -> tuple[dict[str, float], WeightedGraph]:
    
    costs: dict[str, float] = {v: inf for v in graph}
    costs[initial] = 0.0

    previous: dict[str, str | None] = {v: None for v in graph}
    visited: set[str] = set()

    while len(visited) < len(graph):
        unvisited: list[str] = [v for v in graph if v not in visited]

        current: str = unvisited[0]
        for v in unvisited[1:]:
            if costs[v] < costs[current]:
                current = v
            elif costs[v] == costs[current] and v < current:
                current = v

        visited.add(current)

        for (neighbor, weight) in graph[current]:
            if neighbor in visited:
                continue
            new_cost = costs[current] + weight
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                previous[neighbor] = current

    tree: WeightedGraph = {v: set() for v in graph}

    for v in graph:
        parent = previous[v]
        if parent is None:
            continue

        for (neighbor, w) in graph[parent]:
            if neighbor == v:
                tree[parent].add((v, w))
                tree[v].add((parent, w))
                break

    return costs, tree