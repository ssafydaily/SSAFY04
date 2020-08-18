def DFS(v):

    S = []
    S.append(v)                 # while문 진입을 위히 시작점 삽입
    visit[v] = True
    print(v, end=" ")

    while len(S) > 0:
        for w in G[v]:
            if not visit[w]:
                S.append(w)     # 주의> 시작점이 2번 스택에 삽입된다.
                v = w
                visit[w] = True
                print(v, end=" ")
                break
        else:
            v = S.pop()

# ----------------------------------------------
import sys

sys.stdin = open("graph_input.txt", "r")

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
visit = [False for _ in range(V + 1)]

for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

DFS(1)