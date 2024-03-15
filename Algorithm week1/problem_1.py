def find_R2(R1,S):
    return 2 * S - R1

while True:
    R1, S = input('R1값과 S값을 입력하세요: ').split()
    R1 = int(R1)
    S = int(S)

    if -1000<= R1 <= 1000 and -1000 <= S <= 1000:
        break
    else:
        print("값의 범위를 벗어났습니다. 다시입력해주세요.")

R2 = find_R2(R1,S)
print(f"R2값은 {R2}입니다.")


