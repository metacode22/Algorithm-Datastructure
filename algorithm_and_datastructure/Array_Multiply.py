import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
    
M, k = map(int, input().split())
b = []
for _ in range(M):
    b.append(list(map(int, input().split())))
    
c = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for l in range(M):
            c[i][j] += a[i][l] * b[l][j]
            
print(c)