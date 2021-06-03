import re

fhand = open('day 14.txt')
p1 = re.compile(r'\[(\d+)\]') # pattern object
p2 = re.compile(r'=\s(\d+)\n')
values = {}

for line in fhand:
    if line.startswith('mask'):
        mask = line[7:-1]
    elif line.startswith('mem'):
        mem_addr = p1.search(line).group(1)
        val = p2.search(line).group(1)
        bin_val = bin(int(val))[2:]
        bin_val36 = (36-len(bin_val))*'0' + bin_val
        l = list(bin_val36)
        for i in range(36):
            if mask[i] != 'X':
                 l[i] = mask[i]
        values[mem_addr] = ''.join(l)

s = 0
for v in values.values():
    # for i in range(36):
    s += int(v, 2) # 将所有二进制字符转化为十进制数字

print(s)
        
        
            