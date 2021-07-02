'''
https://www.acmicpc.net/problem/2458
키 순서 성공출처
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	8296	4362	3164	51.963%
문제
1번부터 N번까지 번호가 붙여져 있는 학생들에 대하여 두 학생끼리 키를 비교한 결과의 일부가 주어져 있다. 단, N명의 학생들의 키는 모두 다르다고 가정한다. 예를 들어, 6명의 학생들에 대하여 6번만 키를 비교하였고, 그 결과가 다음과 같다고 하자. 

1번 학생의 키 < 5번 학생의 키
3번 학생의 키 < 4번 학생의 키
5번 학생의 키 < 4번 학생의 키
4번 학생의 키 < 2번 학생의 키
4번 학생의 키 < 6번 학생의 키
5번 학생의 키 < 2번 학생의 키
이 비교 결과로부터 모든 학생 중에서 키가 가장 작은 학생부터 자신이 몇 번째인지 알 수 있는 학생들도 있고 그렇지 못한 학생들도 있다는 사실을 아래처럼 그림을 그려 쉽게 확인할 수 있다. a번 학생의 키가 b번 학생의 키보다 작다면, a에서 b로 화살표를 그려서 표현하였다. 



1번은 5번보다 키가 작고, 5번은 4번보다 작기 때문에, 1번은 4번보다 작게 된다. 그러면 1번, 3번, 5번은 모두 4번보다 작게 된다. 또한 4번은 2번과 6번보다 작기 때문에, 4번 학생은 자기보다 작은 학생이 3명이 있고, 자기보다 큰 학생이 2명이 있게 되어 자신의 키가 몇 번째인지 정확히 알 수 있다. 그러나 4번을 제외한 학생들은 자신의 키가 몇 번째인지 알 수 없다. 

학생들의 키를 비교한 결과가 주어질 때, 자신의 키가 몇 번째인지 알 수 있는 학생들이 모두 몇 명인지 계산하여 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 학생들의 수 N (2 ≤ N ≤ 500)과 두 학생 키를 비교한 횟수 M (0 ≤ M ≤ N(N-1)/2)이 주어진다. 다음 M개의 각 줄에는 두 학생의 키를 비교한 결과를 나타내는 두 양의 정수 a와 b가 주어진다. 이는 번호가 a인 학생이 번호가 b인 학생보다 키가 작은 것을 의미한다. 

출력
자신이 키가 몇 번째인지 알 수 있는 학생이 모두 몇 명인지를 출력한다. 

예제 입력 1 
6 6
1 5
3 4
5 4
4 2
4 6
5 2
예제 출력 1 
1
예제 입력 2 
6 7
1 3
1 5
3 4
5 4
4 2
4 6
5 2
예제 출력 2 
2
예제 입력 3 
6 3
1 2
2 3
4 5
예제 출력 3 
0
'''

a = list(map(int,input().split()))
if len(a) < 2:
    a.append(int(input()))

n,m = a[0],a[1]

import sys
input=sys.stdin.readline
from collections import deque

taller = {}
shorter = {}
for _ in range(m):
    a,b = map(int,input().split())
    if a in taller:
        taller[a].append(b)
    else:
        taller[a] = [b]
    if b in shorter:
        shorter[b].append(a)
    else:
        shorter[b] = [a]


def srch_up(x):
    queue = deque(taller[x])
    for i in taller[x]:
        vs_ch[i] = 0
    while queue:
        chck = queue.popleft()
        if chck in taller:
            for j in taller[chck]:
                if vs_ch[j]:
                    vs_ch[j] = 0
                    queue.append(j)

def srch_down(x):
    queue = deque(shorter[x])
    for i in shorter[x]:
        vs_ch[i] = 0
    while queue:
        chck = queue.popleft()
        if chck in shorter:
            for j in shorter[chck]:
                if vs_ch[j]:
                    vs_ch[j] = 0
                    queue.append(j)

cnt = 0
for x in range(1,n+1):
    vs_ch = [0]+[1 for _ in range(n)]
    vs_ch[x] = 0
    if x in taller:
        srch_up(x)
    if x in shorter:
        srch_down(x)
    if 1 not in vs_ch:
        cnt += 1 

print(cnt)