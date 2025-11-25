from graph import Graph
from generic_search import bfs, Node, node_to_path


if __name__ == '__main__':
    metrorrey: Graph[str] = Graph([ 
    
    # Línea 1
    "Talleres", "San Bernabé", "Unidad Modelo", "Aztlán", "Penitenciaría",
    "Alfonso Reyes", "Mitras", "Simón Bolivar", "Hospital", "Edison", "Central",
    "Del Golfo", "Parque Fundidora", "Y Griega", "Eloy Cavazos",
    "Lerdo de Tejada", "Exposición",

    # Línea 2
    "Sendero", "Santiago Tapia", "San Nicolás", "Anáhuac", "Universidad",
    "Niños Héroes", "Regina", "General Anaya", "Alameda", "Fundadores",
    "Padre Mier",

    # Línea 3
    "Hospital Metropolitano", "Los Ángeles", "Ruiz Cortines", "Colonia Moderna",
    "Metalúrgicos", "Colonia Obrera", "Santa Lucía",

    # Estaciones de Transferencia
    "Cuauhtémoc", "Félix U. Gómez", "General I. Zaragoza"
])
    metrorrey.add_edge_by_vertices("Talleres", "San Bernabé")
    metrorrey.add_edge_by_vertices("San Bernabé", "Unidad Modelo")
    metrorrey.add_edge_by_vertices("Unidad Modelo", "Aztlán")
    metrorrey.add_edge_by_vertices("Aztlán", "Penitenciaría")
    metrorrey.add_edge_by_vertices("Penitenciaría", "Alfonso Reyes")
    metrorrey.add_edge_by_vertices("Alfonso Reyes", "Mitras")
    metrorrey.add_edge_by_vertices("Mitras", "Simón Bolivar")
    metrorrey.add_edge_by_vertices("Simón Bolivar", "Hospital")
    metrorrey.add_edge_by_vertices("Hospital", "Edison")
    metrorrey.add_edge_by_vertices("Edison", "Central")
    metrorrey.add_edge_by_vertices("Central", "Cuauhtémoc")
    metrorrey.add_edge_by_vertices("Cuauhtémoc", "Del Golfo")
    metrorrey.add_edge_by_vertices("Del Golfo", "Félix U. Gómez")
    metrorrey.add_edge_by_vertices("Félix U. Gómez", "Parque Fundidora")
    metrorrey.add_edge_by_vertices("Parque Fundidora", "Y Griega")
    metrorrey.add_edge_by_vertices("Y Griega", "Eloy Cavazos")
    metrorrey.add_edge_by_vertices("Eloy Cavazos", "Lerdo de Tejada")
    metrorrey.add_edge_by_vertices("Lerdo de Tejada", "Exposición")
    
    metrorrey.add_edge_by_vertices("Sendero", "Santiago Tapia")
    metrorrey.add_edge_by_vertices("Santiago Tapia", "San Nicolás")
    metrorrey.add_edge_by_vertices("San Nicolás", "Anáhuac")
    metrorrey.add_edge_by_vertices("Anáhuac", "Universidad")
    metrorrey.add_edge_by_vertices("Universidad", "Niños Héroes")
    metrorrey.add_edge_by_vertices("Niños Héroes", "Regina")
    metrorrey.add_edge_by_vertices("Regina", "General Anaya")
    metrorrey.add_edge_by_vertices("General Anaya", "Cuauhtémoc")
    metrorrey.add_edge_by_vertices("Cuauhtémoc", "Alameda")
    metrorrey.add_edge_by_vertices("Alameda", "Fundadores")
    metrorrey.add_edge_by_vertices("Fundadores", "Padre Mier")
    metrorrey.add_edge_by_vertices("Padre Mier", "General I. Zaragoza")
    
    metrorrey.add_edge_by_vertices("Hospital Metropolitano", "Los Ángeles")
    metrorrey.add_edge_by_vertices("Los Ángeles", "Ruiz Cortines")
    metrorrey.add_edge_by_vertices("Ruiz Cortines", "Colonia Moderna")
    metrorrey.add_edge_by_vertices("Colonia Moderna", "Metalúrgicos")
    metrorrey.add_edge_by_vertices("Metalúrgicos", "Félix U. Gómez")
    metrorrey.add_edge_by_vertices("Félix U. Gómez", "Colonia Obrera")
    metrorrey.add_edge_by_vertices("Colonia Obrera", "Santa Lucía")
    metrorrey.add_edge_by_vertices("Santa Lucía", "General I. Zaragoza")

    result: Node[str] | None = bfs(
        "Talleres",
        lambda x: x == "Unidad Modelo",
        metrorrey.neighbors_for_vertex
    )
    
    # result: Node[str] | None = bfs(
    #     "Sendero",
    #     lambda x: x == "Exposición",
    #     metrorrey.neighbors_for_vertex
    # )
    
    # result: Node[str] | None = bfs(
    #     "Talleres",
    #     lambda x: x == "Hospital Metropolitano",
    #     metrorrey.neighbors_for_vertex
    # )
    
    # result: Node[str] | None = bfs(
    #     "Alameda",
    #     lambda x: x == "Colonia Obrera",
    #     metrorrey.neighbors_for_vertex
    # )
    
    # result: Node[str] | None = bfs(
    #     "Universidad",
    #     lambda x: x == "Santa Lucía",
    #     metrorrey.neighbors_for_vertex
    # )
    
    # result: Node[str] | None = bfs(
    #     "General I. Zaragoza",
    #     lambda x: x == "Del Golfo",
    #     metrorrey.neighbors_for_vertex
    # )
    
    # result: Node[str] | None = bfs(
    #     "Lerdo de Tejada",
    #     lambda x: x == "Padre Mier",
    #     metrorrey.neighbors_for_vertex
    # )
    
    resultados = [
        bfs(
            "Talleres",
            lambda x: x == "Unidad Modelo",
            metrorrey.neighbors_for_vertex
        ),
        bfs(
            "Sendero",
            lambda x: x == "Exposición",
            metrorrey.neighbors_for_vertex
        ),
        bfs(
            "Talleres",
            lambda x: x == "Hospital Metropolitano",
            metrorrey.neighbors_for_vertex
        ),
        bfs(
        "Alameda",
        lambda x: x == "Colonia Obrera",
        metrorrey.neighbors_for_vertex
        ),
        bfs(
            "Universidad",
            lambda x: x == "Santa Lucía",
            metrorrey.neighbors_for_vertex
        ),
        bfs(
            "General I. Zaragoza",
            lambda x: x == "Del Golfo",
            metrorrey.neighbors_for_vertex
        ),
        bfs(
            "Lerdo de Tejada",
            lambda x: x == "Padre Mier",
            metrorrey.neighbors_for_vertex
        )
    ]

    for i in resultados:
        if i:
            path: list[str] = node_to_path(i)
            print(path)
            print('----------------')
        else:
            print('No solution found.')
