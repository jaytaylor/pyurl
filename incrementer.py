# z > Z

def inc(x, pos=-1):
    lx = list(x)
    if (ord(x[pos]) >= ord('A') and ord(x[pos]) < ord('Z')) or \
        (ord(x[pos]) >= ord('0') and ord(x[pos]) < ord('9')) or \
        (ord(x[pos]) >= ord('a') and ord(x[pos]) < ord('z')):
        lx[pos] = chr(ord(x[pos]) + 1)
    elif ord(x[pos]) == ord('Z'):
        lx[pos] = '0'
    elif ord(x[pos]) == ord('9'):
        lx[pos] = 'a'
    elif ord(x[pos]) == ord('z'):
        if abs(pos) == len(x):
            lx[pos] = 'A'
            lx.append('A')
        else:
            lx[pos] = 'A'
            return inc(''.join(lx), pos - 1)
    return ''.join(lx)

s = 'A'
for _ in range(250000):
#    if len(s) == 3:
#        break
    s = inc(s)
    print s

