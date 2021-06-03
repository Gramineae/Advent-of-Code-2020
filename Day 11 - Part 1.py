import copy

def round_seat_change(s_before):
    '''进行一轮位置变动'''
    s_after = copy.deepcopy(s_before)
    empty = ('.','L')
    rows = len(s_before)-1
    columns = len(s_before[0])-1
    for i in range(1, rows):
        for j in range(1,columns):
            if s_before[i][j] != '.':
                a = s_before[i-1][j-1] in empty
                b = s_before[i-1][j] in empty
                c = s_before[i-1][j+1] in empty
                d = s_before[i][j-1] in empty
                e = s_before[i][j+1] in empty
                f = s_before[i+1][j-1] in empty
                g = s_before[i+1][j] in empty
                h = s_before[i+1][j+1] in empty
                counts = a+b+c+d+e+f+g+h
                if counts == 8:
                    s_after[i][j] = '#'
                elif counts <= 4:
                    s_after[i][j] = 'L'
            else:
                continue
    return s_after


with open('day 11.txt') as fhand:
    lines = fhand.readlines()

# 在座位四周加上一圈floor，以便indexing
seats = [list((len(lines[0])+1)*'.')]
for line in lines:
    seats.append(['.']+list(line.rstrip())+['.'])

seats.append(list((len(lines[0])+1)*'.'))
seats_changed = round_seat_change(seats)

while seats != seats_changed:
    seats = seats_changed
    seats_changed = round_seat_change(seats_changed)

counts = 0
for i in range(1, len(seats)-1):
    for j in range(1, len(seats[0])-1):
        if seats[i][j] == '#':
            counts += 1

print(f'There are {counts} seats ending up occupied.')