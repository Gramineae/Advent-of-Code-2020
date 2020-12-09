fhand = open('day9.txt')
XMAS = [int(n) for n in fhand]

def check_validity(total, numbers):
    """check whether the sum is valid."""
    for n in numbers:
        complement = total - n
        if (complement != n) and (complement in numbers):
            return True
    return False
    

for i,number in enumerate(XMAS):
    if i < 25: 
        continue
    previous25 = XMAS[(i-25):i]
    if not check_validity(number, previous25):
        break

print(number)
