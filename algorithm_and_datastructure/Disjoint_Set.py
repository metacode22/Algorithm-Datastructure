# 특정 원소가 속한 집합 찾기
# parent는 부모 테이블, x는 노드 번호를 의미한다.
# 노드: 1   2   3 (x)
# 부모: 1   1   2 (parent)

# find_parent(parent, 3)
# parent[3]은 2로, 자기 자신인 3이 아니다.
# 따라서 재귀 호출

# find_parent(parent, 2)
# parent[2]는 1로, 자기 자신인 2가 아니다.
# 따라서 다시 재귀 호출

# find_parent(parent, 1)
# parent[1]은 1로, 자기 자신이 맞다. 따라서 if문을 실행하지 않고 x를 반환한다.
# def find_parent(parent, x):                         # 기본적인 형태의 서로소 집합 자료구조에서는 root 노드에 즉시 접근할 수 없다.
#     if parent[x] != x:                              # 현재 부모가 자기 자신이 아니라면, root 노드가 아니라는 이야기이다.
#         return find_parent(parent, parent[x])       # root 노드를 찾기 위해 재귀 호출.
#     return x
    
def find_parent(parent, x):                         # 경로 압축 기법
    if parent[x] != x:                              # 앞의 find_parent()는 그저 부모 노드를 반환한다.
        parent[x] = find_parent(parent, parent[x])  # 허나 경로 압축 기법의 find_parent()는 동일하게 재귀로 부모 노드를 찾고 난 후 해당 노드의 부모 노드 값을 직접 바꾼다.
    return parent[x]                                # 다음부터는 parent[x]를 하면 바로 부모 노드를 찾을 수 있다.
                                                    # 찾기 함수 이후에는 해당 노드의 루트 노드가 바로 부모 노드가 되는 것이다.

def union_parent(parent, a, b):                     # 두 원소가 속한 집합 합치기.
    a = find_parent(parent, a)                      # a와 b의 부모를 하나로 통일하겠다.
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a       # 처음엔 b = a라고 하면 되지 않을까 생각했는데, 그러면 parent의 b가 바뀌는 것이 아니다.
    else:                   # 단지 처음에 나온 b라는 숫자가 a라는 숫자로 바뀔 뿐이다.
        parent[a] = b       # parent라는 테이블의 숫자를 바꾸려면 parent[b] 혹은 parent[a]를 해줘야 한다.
        

