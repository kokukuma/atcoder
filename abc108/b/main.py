import math

def length(x1, y1, x2, y2):
    l = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return l

p = map(int, raw_input().split())
p1 = list(p)[:2]
p2 = list(p)[2:]
l = length(p1[0], p1[1], p2[0], p2[1])

if p1[0] == p2[0]:
    if p1[1] < p2[1]:
        print("%d %d %d %d" % (p2[0]-l, p2[1], p1[0]-l, p1[1]))
    else:
        print("%d %d %d %d" % (p2[0]+l, p2[1], p1[0]+l, p1[1]))
elif p1[1] == p2[1]:
    if p1[1] < p2[1]:
        print("%d %d %d %d" % (p2[0], p2[1]+l, p1[0], p1[1]+l))
    else:
        print("%d %d %d %d" % (p2[0], p2[1]-l, p1[0], p1[1]-l))
else:
    a =  float(p2[1] - p1[1]) / (p2[0] - p1[0])
    b = float(p1[1] * p2[1] - p1[0] * p2[1]) / (p2[0] - p1[0])

    p3 = []
    for x in range(-800, 800):
        for y in range(-800, 800):
            if p1[0] < p2[0]:
                if a * x + b < y:
                    if length(x, y, p1[0], p1[1]) == l * math.sqrt(2) and length(x,y,p2[0],p2[1]) == l:
                        p3 = [x, y]
            else:
                if a * x + b > y:
                    if length(x, y, p1[0], p1[1]) == l * math.sqrt(2) and length(x,y,p2[0],p2[1]) == l:
                        p3 = [x, y]
    p4 = []
    for x in range(-800, 800):
        for y in range(-800, 800):
            if p1[0] < p2[0]:
                if a * x + b < y:
                    if length(x, y, p1[0], p1[1]) == l and length(x,y,p2[0],p2[1]) == l * math.sqrt(2):
                        p4 = [x, y]
            else:
                if a * x + b > y:
                    if length(x, y, p1[0], p1[1]) == l and length(x,y,p2[0],p2[1]) == l * math.sqrt(2):
                        p4 = [x, y]

    print("%d %d %d %d" % (p3[0], p3[1], p4[0], p4[1]))
