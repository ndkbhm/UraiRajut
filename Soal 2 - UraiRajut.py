def urai(a):
    b, c = 0, ''
    while b < len(a):
        b += 1
        c += a[:b]
    return c

def rajut(d):
    e = [1]
    f = 1
    for g in range (2,len(d)):
        f += g
        e.append(f)
    h = e.index(len(d)) + 1
    h *= -1
    i = d[h:len(d)]
    return i

# Use the function
print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))

print()

# Use the function
print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))