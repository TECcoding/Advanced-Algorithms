#----------------------------------------------------------
# Lab #7: Dijkstra’s Shortest-Path Tree
#
# Date: 26-Nov-2025
# Authors:
#           A01801044 Yael Sinuhe Grajeda Martinez
#           A01800840 Tadeo Emanuel Arellano Conde
#----------------------------------------------------------
# File: dijkstra.py

type WeightedGraph = dict[str, set[tuple[str, float]]]


def dijkstra_spt(
        initial: str,
        graph: WeightedGraph) -> tuple[dict[str, float], WeightedGraph]:
    # The function's code goes here
    ...