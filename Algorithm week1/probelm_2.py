def calculate_distance(num1,num2):
    east_west_distance = abs((num1//4 - num2//4))
    north_south_distance = abs((num1 % 4) - (num2 % 4))
    return east_west_distance + north_south_distance

num1, num2 = map(int, input().split())

result = calculate_distance(num1,num2)
print(result)