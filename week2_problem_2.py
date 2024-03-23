n, m = map(int, input().split())
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

# 대칭 차집합 구하기
symmetric_difference = (set_a - set_b) | (set_b - set_a)

# 결과 출력
print(len(symmetric_difference))