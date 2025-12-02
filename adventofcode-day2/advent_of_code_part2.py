# you can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. 
# So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.
# 11 ==> invalid
# 1010 ==> invalid

#Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. 
# So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times)
# and 1111111 (1 seven times) are all invalid IDs.
# 824824824 invalid id because 824 repeats 3 times

with open("input.txt") as f:
    data = f.read().strip()

sum_invalid_id = 0
for line in data.split(","):
    range_num = line.split("-")
    for i in range(int(range_num[0]), int(range_num[1])+1):
        s = str(i)
        len_i = len(s)
        for j in range(1, len_i):
            if len_i % j == 0:
                first_part = s[:j]
                repeat_count = len_i // j
                if first_part * repeat_count == s and repeat_count >= 2:
                    sum_invalid_id += i
                    break

print(sum_invalid_id)