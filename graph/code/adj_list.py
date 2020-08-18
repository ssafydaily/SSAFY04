import sys
sys.stdin = open("graph_input.txt", "r")

V, E = map(int, input().split())        # 정점수, 간선수 입력
G = [[] for _ in range(V + 1)]          # 인접 리스트 생성
                                        # 정점 번호 1 ~ V
for i in range(E):                      # 간선 정보 입력
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)                      # 무향 또는 유향 그래프인지 주의


for i in range(1, V + 1):
    print(i, '-->', G[i])
