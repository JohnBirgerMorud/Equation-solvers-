import matplotlib.pyplot as plt
import numpy as np

# Konstanter ligningløser
N = 1000
t0, t_end = 0, 150
h = t_end / N

# Andre konstanter
m = 750
g = 9.81
c_drag = 1
p = 2.2
A = 1.8*0.2
v0 = 0

F_l = c_drag * 1/2 * p * A / m

def dv_dt(v, F_l):
    return 9.81 - F_l * v**2


def euler():
    v = np.zeros(N+1)
    v[0] = v0
    for i in range(N):
        est = v[i] + h * dv_dt(v[i], F_l)
        v[i+1] = v[i] + h * dv_dt((v[i] + est) / 2, F_l)
    
    return v

v = euler(N, v0, h, F_l)
v_G = euler(N, v0, h, 0)
time = np.linspace(t0, t_end, N+1)


plt.style.use('seaborn')

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

ax1.plot(time, v)
ax2.plot(time, v_G)

ax1.set_title("Fritt fall med luftmotstand")
ax1.set_ylabel('fart')

ax2.set_title('Fritt fall uten luftmostand')
ax2.set_xlabel('tid')
ax2.set_ylabel('fart')

plt.show()

