# 초기에 무한으로 해놓는 이유는, 갈 수 있는 길이 없으면 완전히 떨어져 있는 것이므로 무한으로 표현하는 듯.
# 방문하지 않은 노드 중 가장 짧은 거리인 노드를 방문(방문하고 있는 노드와 연결되어 있지 않아도 상관 없다)
# 연결되어 있지 않아도 가장 짧은 거리부터 확인하므로 모든 노드들을 방문하게 된다.
# 해당 노드와 연결된 노드를 확인하면서, 해당 노드를 거쳐가면 얼마나 걸리는지 확인 후 더 작은 거리이면 갱신
# 출발점으로부터 이미 방문한 노드까지의 최단 거리는 갱신되지 않는다. 방문하면서 가장 짧은 거리로 갱신했기 때문이다.
# 한 단게당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해할 수 있다.
# 알고리즘을 거치고 나면 테이블에는 출발점으로부터 해당 노드까지의 최단 거리를 저장하고 있다.
# O(V)에 거쳐 선형 탐색하고 모든 노드들을 방문하기에 시간 복잡도는 O(V^2)라고 볼 수 있다.

import sys
input = sys.stdin.readline
INF = 1e9

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 방문하지 않은 노드 중(not visited[i])에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index
    
def dijkstra(start):
    # 출발 노드 초기화
    distance[start] = 0     
    visited[start] = True
    
    # 출발 노드로부터 당장 방문이 가능한 곳까지의 거리를 갱신
    for j in graph[start]:
        distance[j[0]] = j[1]
    
    # 출발 노드를 제외하고 위 과정에 대해 반복
    for i in range(n - 1):
        # 현재 노드에서 최단 거리의 노드를 꺼내 방문하도록 하겠다.
        now = get_smallest_node()
        visited[now] = True
        
        # 현재 노드와 연결된 다른 노드를 확인한다.
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧을 경우 갱신한다.
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                
dijkstra(start)

# 출발 노드로부터 모든 노드들까지의 최단 거리 출력.
for i in range(1, n + 1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])