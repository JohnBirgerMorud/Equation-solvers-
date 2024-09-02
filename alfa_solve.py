import matplotlib.pyplot as plt
import numpy as np

N = 50000
t_0 = 0
t_end = 20
h = (t_end - t_0) / N
t = np.linspace(t_0, t_end, N + 1)
y_0 = 0.1

def alfa(T):
    return (np.e**(1/T)) / (T**2 * (np.e**(1/T) - 1)**2)

def faktisk(t):
    return 2 - 19 / 10 * np.e**(-t)

def dy_dt(y):
    return 2*alfa(y) - y*alfa(y)

def euler(y_0, N):
    y = np.zeros(N+1)
    y[0] = y_0
    
    for i in range(N):
        y[i+1] = y[i] + h * (dy_dt(y[i]))
    return y

def heuns(y_0, N):
    heuns = np.zeros(N+1)
    heuns[0] = y_0

    for i in range(N):
        print(i)
        est = heuns[i] + h * (dy_dt(heuns[i]))
        heuns[i+1] = heuns[i] + h * (dy_dt((heuns[i] + est) / 2))
    return heuns

def trapes(y_0, N):
    trapes = np.zeros(N+1)
    trapes[0] = y_0

    for i in range(N):
        trapes[i+1] = (trapes[i] + h / 2 * dy_dt(trapes[i]) + h) / (1 + h/2)
    return trapes

def midtpunkt(y_0, N):
    midtpunkt = np.zeros(N+1)
    midtpunkt[0] = y_0

    for i in range(N):
        midtpunkt[i+1] = (midtpunkt[i] - h / 2 * midtpunkt[i] + 2*h) / (1 + h/2)
    return midtpunkt

#Funksjonen
y_faktisk = [faktisk(t) for t in t]

#Numeriske metoder
y_euler = euler(y_0, N)
y_alfa = [alfa(T) for T in y_faktisk]

minim = 100000
for index, val in enumerate(y_euler):
    while abs(val - 1) < minim:
        minim = abs(val-1)
        imin = index

print(y_euler[imin], t[imin])

plt.plot(t, y_euler, 'b')
plt.plot(t, y_faktisk, 'r')
plt.plot(t, y_alfa, 'y')

plt.show()

