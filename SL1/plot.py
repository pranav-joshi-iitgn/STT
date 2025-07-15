""" Simple example of plotting using pyplot """
import numpy as np
import matplotlib.pyplot as plt
if __name__ == "__main__":
    L = []
    x = np.linspace(-2*np.pi,2*np.pi,1000)
    y = np.sin(x)
    plt.plot(x,y)
    plt.xlim(-2*np.pi,2*np.pi)
    L.append(r"$ y=\sin(x) $")
    y1 = np.cos(x)
    plt.plot(x,y1)
    L.append(r"$ y=\cos(x) $")
    y2 = np.exp(x)
    plt.plot(x,y2)
    L.append(r"$ y=e^x $")
    y3 = x**2
    plt.plot(x,y3)
    L.append(r"$ y = x^2 $")
    y3 = 2*x - 1
    plt.plot(x,y3)
    L.append(r"$ y = 2x-1 $")
    P = 1009 # a very large prime
    T = 2
    randns = []
    for i in range(1000):
        randns.append(T)
        T = (T+1)**2 % P
    h = np.array(randns)
    h = 1000 * h/P
    plt.scatter(x,h,s=0.1)
    L.append("scatter")
    plt.legend(L)
    plt.title("example of plotting")
    plt.show()
