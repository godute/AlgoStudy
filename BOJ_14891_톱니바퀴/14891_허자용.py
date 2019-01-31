class gear:
    def __init__(self, string):
        self.teeth = []
        for i in string:
            self.teeth.append((int(i)))
        return


def spin(now, direction):
    temp_teeth = gearlist[now].teeth[0]

    if direction:
        for i in range(7):
            gearlist[now].teeth[(8 - i) % 8] = gearlist[now].teeth[7 - i]
        gearlist[now].teeth[1] = temp_teeth

    else:
        for i in range(7):
            gearlist[now].teeth[i] = gearlist[now].teeth[i + 1]
        gearlist[now].teeth[7] = temp_teeth
    return


def left(now, direction):
    if(now != 0 and gearlist[now].teeth[6] != gearlist[now - 1].teeth[2]):
        left(now - 1, not(direction))
    spin(now, direction)
    return


def right(now, direction):
    if(now != 3 and gearlist[now].teeth[2] != gearlist[now + 1].teeth[6]):
        right(now + 1, not(direction))
    spin(now, direction)
    return

# def printgear():
#     for i in gearlist:
#         for j in i.teeth:
#             print(j, end='')
#         print()
#     return


gearlist = []
for i in range(4):
    newgear = gear(input())
    gearlist.append(newgear)

n_rotation = int(input())
for i in range(n_rotation):
    [n, d] = list(map(int,input().split(" ")))
    d = int(d * (d + 1)/2)
    left(n-1, d)
    spin(n-1, not(d))
    right(n-1,d)

score = 0
temp = 1
for i in gearlist:
    if i.teeth[0]:
        score += temp
    temp *= 2

print(score, end = '')
