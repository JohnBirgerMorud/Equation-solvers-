import matplotlib.pyplot as plt
import numpy as np

N = 15
t_0 = 0
t_end = 10
h = (t_end - t_0) / N
t = np.linspace(t_0, t_end, N + 1)
y_0 = 0

def faktisk(t):
    return (np.e**(2*t) - 1)/ (np.e**(2*t)+1)

def dy_dt(y):
    return 1 - y**2

def euler():
    y = np.zeros(N+1)
    y[0] = y_0
    
    for i in range(N):
        y[i+1] = y[i] + h * (dy_dt(y[i]))
    return y

def heuns():
    heuns = np.zeros(N+1)
    heuns[0] = y_0

    for i in range(N):
        print(i)
        est = heuns[i] + h * (dy_dt(heuns[i]))
        heuns[i+1] = heuns[i] + h * (dy_dt((heuns[i] + est) / 2))
    return heuns

def trapes():
    trapes = np.zeros(N+1)
    trapes[0] = y_0

    for i in range(N):
        trapes[i+1] = (trapes[i] + h / 2 * dy_dt(trapes[i]) + h) / (1 + h/2)
    return trapes

def midtpunkt():
    midtpunkt = np.zeros(N+1)
    midtpunkt[0] = y_0

    for i in range(N):
        midtpunkt[i+1] = (midtpunkt[i] - h / 2 * midtpunkt[i] + 2*h) / (1 + h/2)
    return midtpunkt


def runga_kutta():
    y = np.zeros(N+1)
    y[0] = y_0

    for i in range(N):
        k1 = h * dy_dt(y[i])
        k2 = h * dy_dt(y[i] + 1/2*k1)
        k3 = h * dy_dt(y[i] + 1/2*k2)
        k4 = h * dy_dt(y[i] + k3)
        y[i+1] = y[i] + 1/6 * (k1 + 2*k2 + 2*k3 + k4)
    
    return y


#Funksjonen
t_faktisk = np.linspace(t_0, t_end, 10000)
y_faktisk = [faktisk(t) for t in t_faktisk]

#Numeriske metoder
y_euler = euler()
y_heuns = heuns()
y_trapes = trapes()
y_midtpunkt = midtpunkt()
y_runge_kutta = runga_kutta()

plt.plot(t, y_heuns, 'g')
plt.plot(t, y_euler, 'y')
plt.plot(t, y_runge_kutta, 'b')

#plt.plot(t, y_trapes, 'y')
#plt.plot(t, y_midtpunkt, 'grey')
plt.plot(t_faktisk, y_faktisk, 'r')

plt.show()