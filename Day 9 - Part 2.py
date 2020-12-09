fhand = open('day9.txt')
XMAS = [int(n) for n in fhand]

def check_validity(total, numbers):
    """check whether the sum is valid."""
    for n in numbers:
        complement = total - n
        if (complement != n) and (complement in numbers):
            return True
    return False

def find_contiguous_set(n):
    """
    find a contiguous set. 
    i equals list index, n equals number of addends.
    """
    for i in range(0, len(XMAS)-n+1):
        addends = XMAS[i:(i+n)]
        if sum(addends) == invalid_number:
            return addends
    return False
    

for i,number in enumerate(XMAS):
    if i < 25: 
        continue
    previous25 = XMAS[(i-25):i]
    if not check_validity(number, previous25):
        break

invalid_number = number

n = 2
while n>1:
    if find_contiguous_set(n):
        contiguous_set = find_contiguous_set(n)
        break
    n += 1

smallest = min(contiguous_set)
largest = max(contiguous_set)
print(smallest + largest)