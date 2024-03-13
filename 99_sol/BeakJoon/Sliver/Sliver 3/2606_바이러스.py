import sys
sys.stdin = open("input.txt")
from collections import deque

computer = int(input()) # 컴퓨터 개수 : 7
line = int(input()) # 연결선 개수 : 6
graph = [[] for i in range(computer+1)]
# [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
visited = [0]*(computer+1) # 방문한 컴퓨터인지 표시

for i in range(line): # 그래프 생성
    a, b = map(int, input().split())
    graph[a] += [b] # a에 b 연결
    graph[b] += [a] # b에 a 연결 -> 양방향
visited[1] = 1 # 1번 컴퓨터부터 시작이니 방문 표시
Q = deque([1])

while Q:
    c = Q.popleft()
    for g in graph[c]:
        if visited[g] == 0:
            Q.append(g)
            visited[g] = 1
print(sum(visited)-1)