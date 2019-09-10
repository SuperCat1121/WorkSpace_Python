# 1
print('# 1')
for i in range(5):
    for j in range(i+1):
        print('*',end= ' ')
    print()

# 2
print('# 2')
for i in range(5) :
    for j in range(5-i) :
        print('*', end=' ')
    print()

# 3
print('# 3')
for i in range(5) :
    for j in range(4-i, 0, -1) :
        print(' ', end=' ')
    for j in range(0, i+1, +1) :
        print('*', end=' ')
    print()

# 4
print('# 4')
for i in range(5) :
    for j in range(i) :
        print(' ', end=' ')
    for j in range(5-i) :
        print('*', end=' ')
    print()

# 5
print('# 5')
for i in range(5) :
    for j in range(4-i) :
        print(' ', end=' ')
    for j in range(2*i+1) :
        print('*', end=' ')
    print()
    







