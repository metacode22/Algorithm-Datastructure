# 우선순위 큐 : 가장 우선순위가 높은 데이터부터 pop된다.
# 방문하지 않은 노드 중에서 최단 거리가 가장 짤은 노드를 선택하기 위해 힙을 사용한다.
# 방문하지 않은 노드를 찾기 위해 선형 탐색하는 것이 아니라 곧바로 나오므로 수행시간을 더 빠르게 만든다.
# 최단 거리의 방문하지 않은 노드가 나와야 하므로 최소힙을 사용한다.
# 그 노드를 거쳐가는 거리를 구해 갱신시키는 것은 기존과 같다.
# 시간 복잡도는 O(ElogV)

# 우선순위 큐에 넣을 때 거리를 앞에 두고 튜플로 넣으면 알아서 순서를 맞춘다. ex. (거리, 노드)

import sys, heapq
input = sys.stdin.readline
INF = 1e9
n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
# 매번 현재 상황에서 짧은 노드를 찾기 위한 함수가 없다는 것을 알 수 있다.
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 방문하지 않은 노드 중 가장 짧은 노드를 꺼낼 수 있도록 구현
        dist, now = heapq.heappop(q)        # dist는 now까지의 거리
        # 이미 처리된 적이 있는 노드라면 무시한다. 방문 테이블을 사용하지 않는다.
        # 따라서 노드의 갯수 V만큼만 while문이 수행된다.
        # 이 때 노드는 우선순위 큐를 이용해 나오고 들어가므로 log V
        if distance[now] < dist:
            continue
        # 최대 간선의 갯수 E만큼 수행된다.
        for i in graph[now]:
            print(f"dist: {dist} now: {now}")
            print(f"i : {i}")
            cost = dist + i[1]      # dist는 pop되면서 나온 거리로, 해당 노드까지의 거리를 말한다. if를 만나지 않았다는 것은 갱신할 수도 있다는 뜻. 이 때 i[1]은 더해져서 비교해볼 거리
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
               
               
dijkstra(1)
for i in range(1, n + 1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])