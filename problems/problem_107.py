#Henry Maltby 2017

def minl_spanning_tree(vertices, edges, distances):
    visited = set()
    edges_out = set()
    v = vertices.pop()
    def dist (tup): return distances[tup]
    total = 0
    while vertices:
        visited.add(v)
        for neighbor in edges[v]:
            if neighbor not in visited:
                edges_out.add((v, neighbor))
        edge = min(edges_out, key=dist)
        total += distances[edge]
        v = edge[1]
        vertices.remove(v)
        to_remove = []
        for e in edges_out:
            if e[1] == v:
                to_remove.append(e)
        for e in to_remove:
            edges_out.remove(e)
    return total

def parse_network():
    f = open("problem_107_network.txt")
    lines = f.read().strip().split('\n')
    vertices = set(range(len(lines)))
    edges = {}
    distances = {}
    total = 0
    for i in range(len(lines)):
        els = lines[i].split(',')
        edges[i] = set()
        for j in range(len(lines)):
            if els[j] != '-':
                d = int(els[j])
                total += d
                edges[i].add(j)
                distances[(i, j)] = d
                distances[(j, i)] = d
    return total // 2 - minl_spanning_tree(vertices, edges, distances)

print(parse_network())