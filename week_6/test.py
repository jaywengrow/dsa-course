import vertex
import dfs_traverse
import topological_sort


def assert_equal(x, y):
    if x == y:
        print(".")
    else:
        print("FAIL")


# Vertex - Directed Graph - Add adjacent vertex
alice = vertex.Vertex("alice")
bob = vertex.Vertex("bob")
cynthia = vertex.Vertex("cynthia")

alice.add_adjacent_vertex(bob)
alice.add_adjacent_vertex(cynthia)
assert_equal(alice.adjacent_vertices[0].value, "bob")
assert_equal(alice.adjacent_vertices[1].value, "cynthia")

# Depth-first traverse
alice = vertex.Vertex("Alice")
bob = vertex.Vertex("Bob")
candy = vertex.Vertex("Candy")
derek = vertex.Vertex("Derek")
elaine = vertex.Vertex("Elaine")
fred = vertex.Vertex("Fred")
gina = vertex.Vertex("Gina")
helen = vertex.Vertex("Helen")
irena = vertex.Vertex("Irena")

alice.add_adjacent_vertex(bob)
alice.add_adjacent_vertex(candy)
alice.add_adjacent_vertex(derek)
alice.add_adjacent_vertex(elaine)
bob.add_adjacent_vertex(fred)
fred.add_adjacent_vertex(helen)
derek.add_adjacent_vertex(gina)
gina.add_adjacent_vertex(irena)
bob.add_adjacent_vertex(alice)
candy.add_adjacent_vertex(alice)
derek.add_adjacent_vertex(alice)
elaine.add_adjacent_vertex(alice)
fred.add_adjacent_vertex(bob)
helen.add_adjacent_vertex(fred)
gina.add_adjacent_vertex(derek)
irena.add_adjacent_vertex(gina)

print("DFS Traverse")
dfs_traverse.dfs_traverse(alice, {})

# Topological Sort
print("Topological Sort")
a = vertex.Vertex("a")
b = vertex.Vertex("b")
c = vertex.Vertex("c")
d = vertex.Vertex("d")
e = vertex.Vertex("e")
f = vertex.Vertex("f")
a.add_adjacent_vertex(b)
a.add_adjacent_vertex(c)
c.add_adjacent_vertex(f)
d.add_adjacent_vertex(e)
e.add_adjacent_vertex(f)
vertices = [a, b, c, d, e, f]
print(topological_sort.topological_sort(vertices))  # d, e, a, c, f, b
