from collections import Counter

N = int(input())
cards = list(map(int, input().split()))

card_counter = Counter(cards)

M = int(input())
targets = list(map(int, input().split()))

result = [card_counter[target] for target in targets]
print(*result)
