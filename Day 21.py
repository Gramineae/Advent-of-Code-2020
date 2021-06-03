import re

fhand = open('Day 21.txt')
pattern1 = re.compile('(.+)\(')
pattern2 = re.compile('contains (.+)\)')
ing_allerg = dict() # 每种配料对应的致敏原
ALGT = set() # 所有不同致敏原
IGDT = set() # 所有不同配料
loi = [] # 存储每行食物的配料列表
loa = [] # 存储每行食物的致敏原列表

for line in fhand:
    ingredients = pattern1.match(line).group(1).split()
    loi.append(ingredients)
    IGDT = IGDT | set(ingredients)
    allergents = pattern2.search(line).group(1).split(', ')
    loa.append(allergents)
    ALGT = ALGT | set(allergents) # 长度为8
        
while len(ing_allerg) != len(ALGT):
    not_paired = ALGT - set(ing_allerg.keys())
    for allergent in not_paired:
        ingredient = IGDT
        for A, I in zip(loa, loi):
            if allergent in A:
                ingredient = ingredient & set(I)
            if len(ingredient) == 1:
                ing_allerg[allergent] = list(ingredient)[0]
                IGDT.remove(list(ingredient)[0])
                break

count = 0            
for food in loi:
    for ingredient in food:
        if ingredient not in ing_allerg.values():
            count += 1            

l = list(ALGT)
l.sort()
for allergent in l:
    print(ing_allerg[allergent], end=',')

print(count)