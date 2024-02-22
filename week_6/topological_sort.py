# There are a few different algorithms for topological sorting,
# but this is the DFS-based approach


def topological_sort(vertices):
    result = []
    visited_vertices = {}

    for vertex in vertices:
        if not visited_vertices.get(vertex.value):
            dfs_traverse(vertex, visited_vertices, result)

    result.reverse()
    return result


def dfs_traverse(vertex, visited_vertices, result):
    visited_vertices[vertex.value] = True

    for adjacent_vertex in vertex.adjacent_vertices:
        if not visited_vertices.get(adjacent_vertex.value):
            dfs_traverse(adjacent_vertex, visited_vertices, result)

    result.append(vertex.value)
