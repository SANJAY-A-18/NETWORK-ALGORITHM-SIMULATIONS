n = 4
INF = 999
graph = [
    [0, 2, 5, 1],
    [2, 0, 3, 2],
    [5, 3, 0, 3],
    [1, 2, 3, 0]
]
def dijkstra(src):
    visited = [False] * n
    distance = [INF] * n
    parent = [-1] * n
    distance[src] = 0
    for _ in range(n):
        min_dist, u = INF, -1
        for i in range(n):
            if not visited[i] and distance[i] < min_dist:
                min_dist, u = distance[i], i
        if u == -1:
            break
        visited[u] = True
        for v in range(n):
            if graph[u][v] != INF and not visited[v]:
                new_dist = distance[u] + graph[u][v]
                if new_dist < distance[v]:
                    distance[v] = new_dist
                    parent[v] = u
    return distance, parent
def print_routing_table(src, distance, parent):
    print(f"\nRouting Table for Router {src + 1}")
    print("Destination\tNext Hop\tCost")
    for dest in range(n):
        if dest == src:
            continue
        next_hop = dest
        while parent[next_hop] != src and parent[next_hop] != -1:
            next_hop = parent[next_hop]
        nh = f"R{next_hop + 1}" if parent[dest] != -1 else "-"
        print(f"R{dest + 1}\t\t{nh}\t\t{distance[dest]}")
print("=== Link State Routing Simulation ===")
for i in range(n):
    dist, parent = dijkstra(i)
    print_routing_table(i, dist, parent)
print("\n✅ Routing tables successfully computed using Dijkstra's algorithm.")

