

# 987654321111111
#811111111111119
#234234234234278
#818181911112111

with open("input.txt") as f:
    data = f.read().strip()

answer = 0
for line in data.splitlines():
    max_right_number = int(line[len(line)-1])
    max_pair = 0
    for elem in reversed(line[:-1]):
        num = int(elem)
        pair = num*10 + max_right_number
        if num > max_right_number:
            max_right_number = num
        if pair > max_pair:
            max_pair = pair
    answer += max_pair

print(answer)