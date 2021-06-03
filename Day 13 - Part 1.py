fhand = open('day 13.txt').read()
notes = fhand.rstrip().split('\n')
ts = int(notes.pop(0))
ids = notes[0].split(',')

waiting_time = {}
for id in ids:
    try:
        id = int(id)
    except:
        continue
    if ts % id == 0:
        waiting_time[id] = 0
        break
    else:
        waiting_time[id] = id - ts % id

for k, v in waiting_time.items():
    if v == min(waiting_time.values()):
        break
    
print(k * v)
        