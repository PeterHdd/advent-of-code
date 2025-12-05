ranges = []
numbers = []
ingredient_ids = 0

with open("input.txt") as f:
    lines = [line.strip() for line in f if line.strip()]

i = 0
while i < len(lines) and "-" in lines[i]:
    start, end = map(int, lines[i].split("-"))
    ranges.append((start, end))
    i += 1

for line in lines[i:]:
    numbers.append(int(line))


for number in numbers:
    for start,end in ranges:
         if start <= number <= end:
            ingredient_ids += 1
            break


print(ingredient_ids)