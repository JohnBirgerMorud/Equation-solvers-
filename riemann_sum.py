import matplotlib.pyplot as plt
import numpy as np

def hoyre_riemann(a, b):
    M = np.sqrt(2)*np.e**(-1/2)
    N =  int(abs(M * (b-a)**2 / (2*10**-8)))

    x = np.linspace(a,b, N)
    y = [np.e**(-x**2) for x in x]
    
    sum = 0
    dx = (b-a) / N

    for i in range(len(x)-1):
        sum += y[i+1] * dx

    print(N)
    return sum

def simpsons(a,b, N):
    if N % 2 == 0:
        N += 1

    dx = (b-a) / (N-1)

    x = np.linspace(a,b, N)
    y = [np.e**(-x**2) for x in x]
    
    sum = 0


    for i in range(len(x)):
        if i == 0 or i == len(x) - 1:
            #print(i, 1)
            sum += dx/3 * y[i]

        elif i % 2 == 1:
            sum += 4/3 * y[i] * dx
            #print(i,4)

        else:
            sum += 2/3*dx * y[i]
            #print(i,2)
    print(len(x))

    return sum

def trapes(a,b, N):
    dx = (b-a) / (N-1)

    x = np.linspace(a,b, N)
    y = [np.sin(x)/x for x in x]

    sum = 0

    for i in range(len(x)-1):
        sum += 1/2 * dx * (y[i] + y[i+1])

    return y, sum


def midtpunkt(a,b, N):
    dx = (b-a) / (N-1)

    x = np.linspace(a,b,N)
    y = [np.sin(x+dx)/(x+dx) for x in x[:-1]]

    sum = 0

    for i in range(len(y)):
        sum += dx * y[i]
    
    return y, sum

#a = 0.7468241328124270253994674361318530053544996868126063290276544989
a = 1.85193705196


def comb(y1, y2, a, b, N): 
    dx = (b-a) / (N-1)



    x = np.linspace(a,b,N)
    y3 = [(1/3 * (2*y1[i] + 1/2*(y2[i] + y2[i+1]))) for i in range(len(x)-1)]

    sum = 0

    for i in range(len(y3)):
        sum += dx * y3[i]

    return sum

N = 101

y1, midt = midtpunkt(0.0000000000000001,np.pi, N)
y2, trap = trapes(0.0000000000000001,np.pi, N)
kombo = comb(y1, y2, 0.0000000000000001, np.pi, N)
simp = simpsons(0,1, N)


#print(simpsons(0,1) - a)

print("")
print(f"Simpsons:                       {simp-a}")
print(f"Trapesmetoden:                  {trap-a}")
print(f"Midtpunktmetode:                {midt-a}")
print(f"Snittet av midt og trapes:      {kombo-a} ")
print("")