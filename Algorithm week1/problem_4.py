M, N = map(int, input().split())

turn_reps = 0

for i in range(N,0):
    turn_reps=turn_reps+1

for j in range(M-1,1):
    turn_reps=turn_reps+1

print(turn_reps)