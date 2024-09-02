import matplotlib.pyplot as plt
import numpy as np

# Konstanter

N = 10000
t0, t_end = 0, 20
h = (t_end - t0) / N

x0, y0 = 10, 5
a, b, c, d = 1, 1, 1, 1


def dx_dt(x,y, a, b):
    return a*x - b*x*y

def dy_dt(y,x,c,d):
    return -c*y + d*x*y

def euler(a,b,c,d, x0, y0):
    x = np.zeros(N+1)
    x[0] = x0
    y = np.zeros(N+1)
    y[0] = y0

    for i in range(N):
        x[i+1] = x[i] + h * dx_dt(x[i], y[i], a, b)
        y[i+1] = y[i] + h * dy_dt(y[i], x[i], c, d)

    return x, y


x, y = euler(a,b,c,d, x0, y0)
t = np.linspace(t0, t_end, N+1)

fig, [ax1, ax2] = plt.subplots(ncols=1, nrows=2)

ax1.plot(x, t)
ax1.plot(y, t)
ax1.grid(color='grey')

ax2.plot(x,y)
ax2.grid(color='grey')

plt.show()

print(x)
print(y)