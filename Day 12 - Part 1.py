with open('day 12.txt') as fhand:
    instructions = fhand.readlines()

def move(action, value, x, y):
    '''发生位移，不改变方向'''
    if action == 'E':
        x += value
    elif action == 'W':
        x -= value
    elif action == 'N':
        y += value
    elif action == 'S':
        y -= value
    return (x,y)


def change_direction(action, direction, angle):
    '''改变方向，但不发生位移'''
    D = ('E', 'S', 'W', 'N','E', 'S', 'W', 'N')
    i = D.index(direction)
    if angle == 90:
        if action == 'R':
           direction = D[i+1]
        elif action == 'L':
            direction = D[i-1]
    elif angle == 180:
        if action == 'R':
           direction = D[i+2]
        elif action == 'L':
            direction = D[i-2]
    elif angle == 270:
        if action == 'R':
           direction = D[i+3]
        elif action == 'L':
            direction = D[i-3]
    return direction
    

x, y = 0, 0
direction = 'E'
for ins in instructions:
    ins = ins.rstrip()
    action = ins[0]
    value = int(ins[1:])
    if action in ('E', 'W', 'N', 'S'):
        x, y = move(action, value, x, y)
    elif action in ('L', 'R'):
        direction = change_direction(action, direction, value)
    elif action == 'F':
        x, y = move(direction, value, x, y)

Manhattan_distance = abs(x) + abs(y)
print(Manhattan_distance)