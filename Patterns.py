# Right side increment triangle...

for i in range(5):
    for j in range(i+1):
        print('*',end=' ')
    print()

#right side decrement triangle..

for i in range(5):
    for j in range(i,5):
        print('*',end=' ')
    print()

#left side increment triangle..

for i in range(5):
    for j in range(i,5):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=" ")
    print()

#left side decrement triangle..

for i in range(5):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,5):
        print('*',end=' ')
    print()

#half pyramid..

for i in range(4):
    for j in range(i,5):
        print(' ',end=" ")
    for j in range(i+1):
        print('*',end=" ")
    for j in range(i):
        print('*',end=" ")
    print()

#another
for i in range(5):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,4):
        print('*',end=" ")
    for j in range(i,5):
        print('*',end=" ")
    print()