import build_path

def BFS_SP(graph, start, goal) :
    explored = []
    queue = [[start]]

    if start == goal:
        return "Same Node"

    while queue:
        path = queue.pop()
        node = path[-1]

        if node not in explored:
            neighbours = graph[node]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == goal:
                    return "Shortest Path = ", * new_path
        explored.append(node)

    return "No Path Exists"

if __name__ == "__main__":
        
    print(BFS_SP(build_path.build_graph(), 'A', 'G'))