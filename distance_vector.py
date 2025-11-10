n = 4
INF = 999
cost = [
    [0, 2, INF, 1],
    [2, 0, 3, 2],
    [INF, 3, 0, 4],
    [1, 2, 4, 0]
]
dist = [[0 for _ in range(n)] for _ in range(n)]
next_hop = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        dist[i][j] = cost[i][j]
        next_hop[i][j] = j if cost[i][j] != INF and i != j else -1
def print_table():
    for i in range(n):
        print(f"\nRouting Table for Router {i + 1}:")
        print("Destination\tCost\tNext Hop")
        for j in range(n):
            nh = "-" if next_hop[i][j] == -1 else f"R{next_hop[i][j]+1}"
            print(f"R{j + 1}\t\t{dist[i][j]}\t{nh}")
    print("\n" + "=" * 50)
iteration = 0
while True:
    iteration += 1
    updated = False
    print(f"\n==== Iteration {iteration} ====")
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dist[i][j] > cost[i][k] + dist[k][j]:
                    dist[i][j] = cost[i][k] + dist[k][j]
                    next_hop[i][j] = k
                    updated = True
    print_table()
    if not updated:
        print("\n✅ Routing tables have converged. Simulation complete.")
        break

