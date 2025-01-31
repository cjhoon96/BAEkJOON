'''
테트로미노
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	72280	27308	17731	35.773%
문제
폴리오미노란 크기가 1×1인 정사각형을 여러 개 이어서 붙인 도형이며, 다음과 같은 조건을 만족해야 한다.

정사각형은 서로 겹치면 안 된다.
도형은 모두 연결되어 있어야 한다.
정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.
정사각형 4개를 이어 붙인 폴리오미노는 테트로미노라고 하며, 다음과 같은 5가지가 있다.



아름이는 크기가 N×M인 종이 위에 테트로미노 하나를 놓으려고 한다. 종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 정수가 하나 쓰여 있다.

테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.

테트로미노는 반드시 한 정사각형이 정확히 하나의 칸을 포함하도록 놓아야 하며, 회전이나 대칭을 시켜도 된다.

입력
첫째 줄에 종이의 세로 크기 N과 가로 크기 M이 주어진다. (4 ≤ N, M ≤ 500)

둘째 줄부터 N개의 줄에 종이에 쓰여 있는 수가 주어진다. i번째 줄의 j번째 수는 위에서부터 i번째 칸, 왼쪽에서부터 j번째 칸에 쓰여 있는 수이다. 입력으로 주어지는 수는 1,000을 넘지 않는 자연수이다.

출력
첫째 줄에 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값을 출력한다.

예제 입력 1 
5 5
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1
예제 출력 1 
19
예제 입력 2 
4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
예제 출력 2 
20
예제 입력 3 
4 10
1 2 1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1 2 1
1 2 1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1 2 1
예제 출력 3 
7
출처
데이터를 추가한 사람: appie701, crookid, esuperstar, raboribus, rlatpwlsdlek, stack, vjerksen
문제를 만든 사람: baekjoon
문제의 오타를 찾은 사람: bluebrown
알고리즘 분류
구현
브루트포스 알고리즘
'''

import sys
input=sys.stdin.readline

N, M = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]

graph_one_dim = sorted(sum(graph, []), reverse=True)
inspection = [sum(graph_one_dim[0:4-i]) for i in range(4)]
inspection.append(0)

end = False
answer = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visit = [[0 for i in range(M)] for j in range(N)]

def dfs_tetro(x, y, idx, score):
    global answer, end
    if answer >= score + inspection[idx + 1]:
        return
    if idx == 3:
        answer = max(answer, score)
        if answer == inspection[0]:
            end = 1
            return
        
    else:        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and visit[ny][nx] == 0:
                if idx == 1:
                    visit[ny][nx] = 1
                    dfs_tetro(x, y, idx + 1, score + graph[ny][nx])
                    visit[ny][nx] = 0
                
                visit[ny][nx] = 1
                dfs_tetro(nx, ny, idx + 1, score + graph[ny][nx])
                visit[ny][nx] = 0
            


for y in range(N):
    if end: 
        break
    for x in range(M):
        if end:
            break
        visit[y][x] = 1
        dfs_tetro(x, y, 0, graph[y][x])
        visit[y][x] = 0


print(answer)