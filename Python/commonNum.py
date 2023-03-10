digs = list(map(int, input().split()))

target = ''.join([str(x) for x in digs])

if all(i == target[0] for i in target):
    print('Yes')
else:
    print('No')