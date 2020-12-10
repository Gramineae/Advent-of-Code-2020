fhand = open('day10.txt')
adapters = [int(jolt) for jolt in fhand]
adapters.sort()

one_jolt_count = 0
two_jolt_count = 0
three_jolt_count = 1

for i in range(0, len(adapters)):
    if i == 0:
        diff = adapters[i] - 0
    else:
        diff = adapters[i] - adapters[i-1]
    if diff == 1:
        one_jolt_count += 1
    elif diff == 2:
        two_jolt_count += 1
    elif diff == 3:
        three_jolt_count += 1

print(one_jolt_count * three_jolt_count)
        
    