'''
https://www.acmicpc.net/problem/1680
쓰레기 수거 출처다국어
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	102	46	41	49.398%
문제
쓰레기장에서 출발한 쓰레기차가 여러 지점들을 방문하며 쓰레기를 모으고 있다. 쓰레기차는 쓰레기장에서 가까운 지점부터 방문하며, 쓰레기를 모으다가 다음과 같은 경우에 쓰레기장으로 돌아가 싣고 있는 쓰레기를 비운다.

쓰레기의 양이 용량에 도달했을 때.
그 지점의 쓰레기를 실었을 때 쓰레기차의 용량을 넘게 될 때.
더 이상 쓰레기를 실을 지점이 없을 때.
쓰레기 모으기는 쓰레기차가 모든 지점의 쓰레기를 수거하여 쓰레기장에 도달했을 때 끝난다. 또한, 쓰레기차가 특정 지점에서 쓰레기를 실을 때는 한 번에 모두 실어야 한다.(즉, 쓰레기의 일부를 싣고 쓰레기장에 다녀온 뒤 나머지를 싣는 것은 허용되지 않는다.)

쓰레기차의 용량과 각 지점의 위치와 쓰레기의 양이 주어졌을 때, 위의 방법처럼 쓰레기차가 모든 쓰레기들을 쓰레기장에 수거했을 때 쓰레기차의 총 이동 거리를 구하자.

입력
입력의 첫 번째 줄에는 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 쓰레기차의 용량 W와 지점의 개수 N이 주어진다. (1 <= W <= 1000, 1 <= N <= 1000)

다음 N개의 줄에는 i번째 지점의 쓰레기장으로부터의 거리 x_i와 쓰레기의 양 w_i가 주어진다. 각 지점의 x_i는 서로 다르며 x_i가 작은 지점부터 순서대로 입력이 주어진다. (0 <= x_i <= 100000, 1 <= w_i <= W) 모든 지점은 일직선 상에 있다.

출력
각 테스트 케이스에 대하여, 쓰레기차가 모든 쓰레기를 수거하여 쓰레기장에 도달할 때까지 움직인 거리를 출력한다.

예제 입력 1 
3
2 2
1 1
2 2
6 3
1 1
2 2
3 3
3 3
1 2
2 2
3 1
예제 출력 1 
8
6
10
'''

import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    weight, N = map(int,input().split())
    
    dist = 0
    plus_dist = 0
    now_w = 0

    over = False

    for i in range(1, N + 1):
        x, w = map(int,input().split())

        plus_dist = x
        now_w += x
        if i == N:
            if now_w > weight:
                dist += plus_dist * 4

            else:
                dist += plus_dist * 2
        
        else:    
            if now_w > weight:
                now_w = w
                dist += plus_dist * 2

                if w == weight:
                    dist += plus_dist * 2
                    now_w = 0
            
            elif now_w == weight:
                dist += plus_dist * 2
                now_w = 0
        
    print(dist)