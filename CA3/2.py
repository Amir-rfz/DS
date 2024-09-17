
num_commands = int(input())

a = []
min_s = None
max_s = None
min_d = None
max_d = None


def recalculate():
    global a, max_s, min_s, max_d, min_d
    min_s = None
    max_s = None
    min_d = None
    max_d = None
    for i in a:
        if i is not None:
            s, d = i
            check_max_min(s, d)


def check_max_min(s, d):
    global max_s, min_s, max_d, min_d
    if min_s is None or min_s > s:
        min_s = s
    if min_d is None or min_d > d:
        min_d = d
    if max_s is None or max_s < s:
        max_s = s
    if max_d is None or max_d < d:
        max_d = d


for _ in range(num_commands):
    command = input().strip().split()
    cmd_type = command[0]
    if cmd_type == '+':
        x, y = int(command[1]), int(command[2])
        s = x+y
        d = x-y
        a.append((s, d))
        check_max_min(s, d)

    elif cmd_type == '-':
        k = int(command[1])
        if k > len(a) or k <= 0:
            continue
        item = a[k-1]
        if item is None:
            continue
        s, d = a[k-1]
        a[k-1] = None
        if s == min_s or s == max_s or d == min_d or d == max_d:
            recalculate()
    elif cmd_type == '?':
        x, y = int(command[1]), int(command[2])
        s = x+y
        d = x-y
        print(max(s-min_s, max_s-s, d-min_d, max_d-d))

