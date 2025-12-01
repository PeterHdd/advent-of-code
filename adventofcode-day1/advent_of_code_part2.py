#The dial starts by pointing at 50.
#The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
#The dial is rotated L30 to point at 52.
#The dial is rotated R48 to point at 0.
#The dial is rotated L5 to point at 95.
#The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
#The dial is rotated L55 to point at 0.
#The dial is rotated L1 to point at 99.
#The dial is rotated L99 to point at 0.
#The dial is rotated R14 to point at 14.
#The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.



with open("input.txt") as f:
    data = f.read().strip()
start_num = 50
password = 0
for line in data.splitlines():
    distance = int(line[1:])
    zeros_this_move = 0
    if line.startswith("L"):
        while True:
            steps_to_zero = start_num if start_num > 0 else 100
            if distance < steps_to_zero:
                break
            distance -= steps_to_zero
            zeros_this_move += 1
            start_num = 0
        start_num = (start_num - distance) % 100
    elif line.startswith("R"):
        while True:
            steps_to_zero = (100 - start_num) if start_num > 0 else 100
            if distance < steps_to_zero:
                break
            distance -= steps_to_zero
            zeros_this_move += 1
            start_num = 0
        start_num = (start_num + distance) % 100

    if start_num == 0 and zeros_this_move == 0:
        zeros_this_move = 1

    password += zeros_this_move

print(password)
