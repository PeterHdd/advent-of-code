# rotation should be to the left (toward lower numbers)
#  to the right (toward higher numbers)

# we have from 0->99 and in a circular way, so start point is 50:
#L68, we are at 50, we need to go to lower number. So i need to remove 50 from 68, 68 - 50 = 18 at 0, so at 99 it would be 17 then 99 - 17 = 82
#L30, we are at 82, 82 - 30 = 52
#R48, 52 + 48 = 100 so its 0
#L5, 0 - 5 = -5 so its 95
#R60, 95 + 60 = 155 so its 55
#L55, 55 - 55 = 0
#L1, 0 - 1 = -1 so its 99
#L99, 99 - 99 = 0
#R14, 0 + 14 = 14
#L82, 14 - 82 = -68 so its 32



with open("input.txt") as f:
    data = f.read().strip()
start_num = 50
answer = 0
for line in data.splitlines():
    if line.startswith("L"):
        start_num = start_num - int(line.removeprefix("L"))
        while start_num < 0:
            start_num = start_num + 100
    elif line.startswith("R"):
        start_num = start_num + int(line.removeprefix("R"))
        while start_num > 99:
            start_num = start_num - 100
    if start_num == 0:
        answer += 1


print(answer)
