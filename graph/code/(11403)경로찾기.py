start = 0
def DFS(v):

    visit[start][v] = 1
    for i in range(N):
        if G[v][i] and visit[start][i] == 0:
            DFS(i)

N = int(input())
G = []

for i in range(N):
    G.append(list(map(int, input().split())))


visit = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    start = i
    DFS(i)


for i in range(N):
    print(' '.join(map(str, visit[i])))

