from collections import deque
import sys
sys.stdin = open('input.txt')

# 해당 노드로의 진입 간선이 제거된다.
# 단방향 그래프에 적용할 수 있다.
# 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것이다.
# 한 단계에서 큐에 새롭게 들어오는 원소가 2개 이상인 경우에는 답이 여러 가지 존재한다.
# 허나 알고리즘 수행 후 결과를 확인하면 문제 없는 답이 나온다. 오류는 없다.
# 사이클이 존재한다면 어떠한 원소도 큐에 들어가지 못하여 결과 도출에 실패한다.
# 위상 정렬을 위해 차례대로 모든 노드를 확인하며 각 노드에서 나가는 간선을 차례대로 제거한다.
# 한번 큐에서 나가는 노드는 다시 큐에 들어가지 않는다.

v, e = map(int, input().split())
# 진입 차수를 0으로 초기화
indegree = [0] * (v + 1)
graph = [[] for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1                # 해당 노드로의 진입 차수 1 증가

def topology_sort():
    result = []                     # 알고리즘 수행 결과를 담을 리스트
    q = deque()
    for i in range(1, v + 1):
        if indegree[i] == 0:        # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입한다.
            q.append(i)
    
    while q:                        # 큐가 빌 때까지 반복한다.
        now = q.popleft()
        result.append(now)
        for i in graph[now]:        
            indegree[i] -= 1        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
            if indegree[i] == 0:
                q.append(i)         # 진입차수가 0인 새로운 노드를 큐에 삽입한다.
    
    for i in result:
        print(i, end = ' ')
        
topology_sort()
