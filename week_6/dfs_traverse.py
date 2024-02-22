def dfs_traverse(vertex, visited_vertices):
    visited_vertices[vertex.value] = True

    print(vertex.value)

    for adjacent_vertex in vertex.adjacent_vertices:
        if not visited_vertices.get(adjacent_vertex.value):
            dfs_traverse(adjacent_vertex, visited_vertices)
