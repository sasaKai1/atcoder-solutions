a = [1,2,3,4,5]
b = list(map(int, input().split()))

tmp = b.copy()
tmp[0], tmp[1] = b[1], b[0]
if tmp == a:
    print("Yes")
    exit()

tmp = b.copy()
tmp[1], tmp[2] = b[2], b[1]
if tmp == a:
    print("Yes")
    exit()

tmp = b.copy()
tmp[2], tmp[3] = b[3], b[2]
if tmp == a:
    print("Yes")
    exit()

tmp = b.copy()
tmp[3], tmp[4] = b[4], b[3]
if tmp == a:
    print("Yes")
    exit()

print("No")