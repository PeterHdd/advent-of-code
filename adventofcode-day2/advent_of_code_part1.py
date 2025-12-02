

# you can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. 
# So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.
# 11 ==> invalid
# 1010 ==> invalid

with open("input.txt") as f:
    data = f.read().strip()

sum_invalid_id = 0
for line in data.split(","):
    range_num = line.split("-")
    for i in range(int(range_num[0]), int(range_num[1])):
        s = str(i)
        len_i = len(s)
        if len_i % 2 == 0 and s[:len_i//2] == s[len_i//2:]:
            sum_invalid_id += i

print(sum_invalid_id)
    



