from itertools import zip_longest

with open("input.txt", encoding="utf-8") as f:
    rows = [line.split() for line in f if line.strip()]

cols = list(zip_longest(*rows, fillvalue=None))

i = 0
array_numbers = []
sub_array_numbers = []
while i <= len(cols) - 1:
    value_multiply = 1
    value_addition = 0

    for elem in cols[i]:
        sign = cols[i][4]
        if elem == "*" or elem == "+":
            break
        if sign == "*":
            value_multiply *= int(elem)
        else:
            value_addition += int(elem)

    if value_multiply != 1:
        sub_array_numbers.append(value_multiply)
    else:
        sub_array_numbers.append(value_addition)
    i += 1 


answer = 0
for elem in sub_array_numbers:
    answer += elem

print(answer)
