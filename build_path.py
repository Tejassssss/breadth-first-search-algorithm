from collections import defaultdict

def make_graph():
    return [ 
        ["A", "B"], ["A", "E"],
        ["A", "C"], ["B", "D"],
        ["B", "E"], ["C", "F"],
        ["C", "G"], ["D", "E"]
    ]
def build_graph(edges):
    graph = defaultdict(list)

    # Loop over every edge of the graph
    for edge in edges:
        a, b = edge[0], edge[1]
        graph[a].append(b)
        graph[b].append(a)
    return graph

if __name__ == "__main__" :
    graph = build_graph(make_graph())
    print(graph)