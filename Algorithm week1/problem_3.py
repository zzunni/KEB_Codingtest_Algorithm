while True:
    N = int(input("N값을 입력하세요: "))
    if 1<=N<=100:
        break
    else:
        print("1이상 100이하의 숫자를 입력해주세요.")

for i in range(1, N+1):
    print(" " * (N-i) + "*" * (2*i-1) + " " * (N-i))

for i in range(N-1, 0, -1):
    print(" " * (N-i) + "*" * (2*i-1) + " " * (N-i))
