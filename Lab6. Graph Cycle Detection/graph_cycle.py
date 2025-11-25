#----------------------------------------------------------
# Lab #6: Graph Cycle Detection
#
# Date: 12-Nov-2025
# Authors:
#           A01801044 Yael Sinuhe Grajeda Martinez
#           A01800840 Tadeo Emanuel Arellano Conde
#----------------------------------------------------------
# File: graph_cycle.py

type Graph = dict[str, list[str]]
    
def has_cycle(initial: str, graph: Graph) -> list[str] | None:
    
    visited: set[str] = set()
    stack: list[str] = []
    
    def dfs(current: str, parent: list[str]) -> list[str] | None:

        visited.add(current)
        stack.append(current)
        
        for neighbor in graph[current]:
            
            if neighbor not in visited:
                found = dfs(neighbor, parent + [current])
                
                if found is not None:
                    return found
                
            elif neighbor in stack and neighbor != parent[-1]:
                start = stack.index(neighbor)
                return stack[start:] + [neighbor]
        
        stack.pop()
        return None
    
    return dfs(initial, [])