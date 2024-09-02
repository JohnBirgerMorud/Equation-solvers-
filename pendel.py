import matplotlib.pyplot as plt
import numpy as np

# p = theta_dot
# q = theta

g = 9.81
l = 1
a = 2

q0 = np.pi/6
p0 = - 0.010

N = 100000
t0, t_end = 0, 15
h = (t_end-t0) / N

def dq_dt(p):
    return p

def dp_dt(q, p):
    return - g/l * np.sin(q) - a * abs(p**3) / p

def pendel():
    q = np.zeros(N+1)
    q[0] = q0

    p = np.zeros(N+1)
    p[0] = p0

    for i in range(N):
        est_q = q[i] + h * dq_dt(p[i])
        est_p = p[i] + 1/2 * h * dp_dt(q[i], p[i])

        q[i+1] = q[i] + 1/2 * h * dq_dt((p[i] + est_p))
        p[i+1] = p[i] + 1/2 * h * dp_dt((q[i] + est_q), (p[i] + est_p))
    
    return q, p 

theta, theta_dot = pendel()
t = np.linspace(t0, t_end, N+1)

fig, (ax1, ax2) = plt.subplots(ncols=1, nrows=2)
ax1.plot(t, theta, 'r')
ax1.set_ylabel('theta')
ax1.grid('g')
ax1.set_title('Med luftmotstand')


ax2.plot(t, theta_dot, 'b')
ax2.set_xlabel('Tid')
ax2.set_ylabel('Theta dot')
ax2.grid('g')

plt.show()
