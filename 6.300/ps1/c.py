from math import sin, pi
from matplotlib.pyplot import plot, show

x = []
y = []

def f(t):
    sum = 0
    for k in range(1, 10000, 2):
        sum += sin(k*t)/k
    return sum

t = 0
while t<10:
    x.append(t)
    y.append(f(t))
    t += 0.01

plot(x,y)
show()
