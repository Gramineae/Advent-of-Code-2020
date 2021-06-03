fhand = open('Day 15.txt')
numbers = [int(x) for x in fhand.read().split(',')]
numbers.reverse()

while True:
    if numbers.count(numbers[0]) == 1:
        numbers.insert(0, 0)
    else:
        n = numbers[1:].index(numbers[0])
        numbers.insert(0, n+1)
    if len(numbers) == 2020:
        print(numbers[0])
        break

fhand.close()