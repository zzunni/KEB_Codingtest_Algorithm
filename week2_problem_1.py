import random

# N = random.randint(1,29)
# M = random.randint(N,29)

import math

def count_bridge_options(N, M):
    # 서쪽의 사이트 개수 N 중 M개를 선택하여 다리를 지을 수 있는 경우의 수
    return math.comb(M, N)

# 입력 받기
N, M = map(int, input().split())

# 다리를 지을 수 있는 경우의 수 계산
result = count_bridge_options(N, M)
print(result)
