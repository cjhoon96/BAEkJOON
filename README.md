# 그래프 탐색 알고리즘 : DFS/BFS

* ## 탐색(Search)이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 말한다.
* ## 대표적인 그래프 탐색 알고리즘으로는 DFS와 BFS가 있다.
* # DFS/BFS는 코테에서 매우 자주 등장하는 유형이므로 반드시 숙지!!!


# 1. 스택과 큐 자료구조

# 1-1 스택 자료구조
* ## 먼저 들어온 데이터가 나중에 나가는 형식 (선입 후출)의 자료구조
* ## 입구와 출고가 동일한 형태로 스택을 시각화 할 수 있음

### 파이썬에서는 리스트의 .append()와 .pop() 을 통해 스택을 구현할 수 있음
~~~
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소 부터 출력
print(stack)
~~~
[1, 3, 2, 5]
[5, 2, 3, 1]



# 1-2 큐 자료구조 
* ## 먼저 들어온 데이터가 먼저 나가는 형식(선입 선출)의 자료구조
* ## 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화 할 수 있음

### 파이썬에서는 from collections import deque를 통해 구현 가능
### 리스트로 가능하지만 시간 복잡도가 더 커짐
~~~
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)
~~~
deque([3, 7, 1, 4])
deque([4, 1, 7, 3])



# 2. DFS(Depth-First Search)

* ## DFS는 깊이 우선 탐색이라고도 부르며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다.
* ## DFS는 스택 자료구조 (혹은 재귀 함수)를 이용하며, 구체적인 동작 과정은 다음과 같다.
    * ## 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
    * ## 스택의 최상단 노드에 방문 하지 않은 인접한 노드가 하나라도 있으며 그 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
    * ## 더이상 2번의 과정을 수행할 수 없을 때까지 반복한다.

## DFS 소스코드 구현
~~~
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
graph = [
    [],        # 인덱스가 1부터 시작 하는 경우가 많으므로 0번째는 빈 리스트를 넣음
    [2,3,8], 
    [1,7], 
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False] * 9  # 인덱스 0은 사용 하지 않기 위해 1~8 만 필요

dfs(graph, 1, visited)
~~~
1 2 7 6 8 3 4 5 


# 4. BFS(Breadth-First Search)

* ## BFS는 너비 우선 탐색이라고도 부르며 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘이다.
* ## BFS는 큐 자료구조를 이용하며, 구체적인 동작 과정은 다음과 같다.
    * ## 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
    * ## 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리한다.
    * ## 더이상 2번의 과정을 수행할 수 없을 때까지 반복한다.  

## BFS 소스코드 구현
~~~
from collections import deque

def bfs(graph, start, visited):
    
    queue = deque([start])
    
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
graph = [
    [],        # 인덱스가 1부터 시작 하는 경우가 많으므로 0번째는 빈 리스트를 넣음
    [2,3,8], 
    [1,7], 
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9  # 인덱스 0은 사용 하지 않기 위해 1~8 만 필요

bfs(graph, 1, visited)
~~~
1 2 3 8 7 4 5 6 


# 4. DFS&BFS 문제풀이

# EX1) 음료수 얼려먹기
* ## nxm 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시한다. 
* ## 구멍이 뚫려 있는 부분끼리 상,하,좌,우 로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
* ## 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.
* ## 다음의 4x5 얼음틀 예시에서는 아이스크림이 총 3개 생성된다.
    ## 00110
    ## 00011
    ## 11111
    ## 00000
~~~
n, m = map(int,input().split())

graph=[]

for _ in range(n):
    graph.append(list(map(int,input())))
    
def dfs(x,y):
    
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y] == 0:
        
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        
        return True
    return False

ans = 0

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            ans += 1
            print(ans)

print(ans)
~~~
3 3
 001
 010
 101
1
2
3
3


# EX2) 미로 탈출
* ## 동빈이는 nxm 크기의 직사각형 형태의 미로에 갇혀 있습니다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 합니다.
* ## 동빈이의 위치는 (1,1)이며 미로의 출구는 (n,m) 의 위치에 존재하며 한번에 한칸씩 이동할 수 있습니다.
* ## 이때 괴물이 있는 부분은 0, 괴물이 없는 부분은 1로 표시되어 있습니다.
* ## 미로는 반드시 탈출 할 수 있은 형태로 제시됩니다.
* ## 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하세요
    * ## 칸을 셀때는 시작칸과 마지막 칸을 모두 포함해서 계산합니다.

~~~
from collections import deque
import numpy as np
n, m = map(int,input().split())

maze = []
for _ in range(n):
    maze.append(list(map(int,input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs_maze(x,y):
    
    queue = deque([(x,y)])
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and maze[nx][ny] == 1:
                    maze[nx][ny] = maze[x][y] + 1
                    print(np.array(maze))
                    queue.append((nx,ny))
    return maze[n-1][m-1]

bfs_maze(0,0)
print(bfs_maze(0,0))
~~~
  
5 6  
 101010  
 111111  
 000001  
 111111  
 111111  
[[1 0 1 0 1 0]  
 [2 1 1 1 1 1]  
 [0 0 0 0 0 1]  
 [1 1 1 1 1 1]  
 [1 1 1 1 1 1]]  
[[3 0 1 0 1 0]  
 [2 1 1 1 1 1]  
 [0 0 0 0 0 1]  
 [1 1 1 1 1 1]  
 [1 1 1 1 1 1]]  
[[3 0 1 0 1 0]  
 [2 3 1 1 1 1]  
 [0 0 0 0 0 1]  
 [1 1 1 1 1 1]  
 [1 1 1 1 1 1]]  
[[3 0 1 0 1 0]  
 [2 3 4 1 1 1]  
 [0 0 0 0 0 1]  
 [1 1 1 1 1 1]  
 [1 1 1 1 1 1]]  
[[3 0 5 0 1 0]  
 [2 3 4 1 1 1]  
 [0 0 0 0 0 1]  
 [1 1 1 1 1 1]  
 [1 1 1 1 1 1]]  
[[3 0 5 0 1 0]  
 [2 3 4 5 1 1]  
 [0 0 0 0 0 1]  
 [1 1 1 1 1 1]  
 [1 1 1 1 1 1]]  
[[3 0 5 0 1 0]  
 [2 3 4 5 6 1]  
 [0 0 0 0 0 1]  
 [1 1 1 1 1 1]  
 [1 1 1 1 1 1]]  
[[3 0 5 0 7 0]  
 [2 3 4 5 6 1]  
 [0 0 0 0 0 1]  
 [1 1 1 1 1 1]  
 [1 1 1 1 1 1]]  
[[3 0 5 0 7 0]  
 [2 3 4 5 6 7]  
 [0 0 0 0 0 1]  
 [1 1 1 1 1 1]  
 [1 1 1 1 1 1]]  
[[3 0 5 0 7 0]  
 [2 3 4 5 6 7]  
 [0 0 0 0 0 8]  
 [1 1 1 1 1 1]  
 [1 1 1 1 1 1]]  
[[3 0 5 0 7 0]  
 [2 3 4 5 6 7]  
 [0 0 0 0 0 8]  
 [1 1 1 1 1 9]  
 [1 1 1 1 1 1]]  
[[ 3  0  5  0  7  0]  
 [ 2  3  4  5  6  7]  
 [ 0  0  0  0  0  8]  
 [ 1  1  1  1  1  9]  
 [ 1  1  1  1  1 10]]  
[[ 3  0  5  0  7  0]  
 [ 2  3  4  5  6  7]  
 [ 0  0  0  0  0  8]  
 [ 1  1  1  1 10  9]  
 [ 1  1  1  1  1 10]]  
[[ 3  0  5  0  7  0]  
 [ 2  3  4  5  6  7]  
 [ 0  0  0  0  0  8]  
 [ 1  1  1  1 10  9]  
 [ 1  1  1  1 11 10]]  
[[ 3  0  5  0  7  0]  
 [ 2  3  4  5  6  7]  
 [ 0  0  0  0  0  8]  
 [ 1  1  1 11 10  9]  
 [ 1  1  1  1 11 10]]  
[[ 3  0  5  0  7  0]  
 [ 2  3  4  5  6  7]  
 [ 0  0  0  0  0  8]  
 [ 1  1  1 11 10  9]  
 [ 1  1  1 12 11 10]]  
[[ 3  0  5  0  7  0]  
 [ 2  3  4  5  6  7]  
 [ 0  0  0  0  0  8]  
 [ 1  1 12 11 10  9]  
 [ 1  1  1 12 11 10]]  
[[ 3  0  5  0  7  0]  
 [ 2  3  4  5  6  7]  
 [ 0  0  0  0  0  8]  
 [ 1  1 12 11 10  9]  
 [ 1  1 13 12 11 10]]  
[[ 3  0  5  0  7  0]  
 [ 2  3  4  5  6  7]  
 [ 0  0  0  0  0  8]  
 [ 1 13 12 11 10  9]  
 [ 1  1 13 12 11 10]]  
[[ 3  0  5  0  7  0]  
 [ 2  3  4  5  6  7]  
 [ 0  0  0  0  0  8]  
 [ 1 13 12 11 10  9]  
 [ 1 14 13 12 11 10]]  
[[ 3  0  5  0  7  0]  
 [ 2  3  4  5  6  7]  
 [ 0  0  0  0  0  8]  
 [14 13 12 11 10  9]  
 [ 1 14 13 12 11 10]]  
[[ 3  0  5  0  7  0]  
 [ 2  3  4  5  6  7]  
 [ 0  0  0  0  0  8]  
 [14 13 12 11 10  9]  
 [15 14 13 12 11 10]]  
10







