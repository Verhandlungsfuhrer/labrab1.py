import math

def frange(start,next, stop):
    s = start
    while s < stop:
        yield s
        s += next
def y(x):
    y: float = (math.asin(x)**2 + math.acos(x)**4)**3
    return y
for x in frange (0.26, 0.66,0.08):
    print (y(x))

xrange = [0.1, 0.35, 0.4, 0.55, 0.6]
xlen = len(xrange)
for s in range(0,xlen):
    x = xrange [s]
    print(y(x))