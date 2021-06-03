fhand = open('Day 22.txt')
deck1, deck2 = [s[9:].strip().split() for s in fhand.read().split('\n\n')]
deck1 = [int(i) for i in deck1]
deck2 = [int(i) for i in deck2]


def combat_round(d1, d2):
    d1.extend([d1[0], d2[0]])
    d1.remove(d1[0])
    d2.remove(d2[0])
    
    
def calculate_score(d):
    d.reverse()
    count = 0
    for i, n in enumerate(d):
        count += (i+1) * n
    return count
    

while True:
    if deck1[0] > deck2[0]:
        combat_round(deck1, deck2)
    else:
        combat_round(deck2, deck1)
    if deck1 == []:
        score = calculate_score(deck2)
        break
    if deck2 == []:
        score = calculate_score(deck1)
        break

print(score)