import matplotlib.pyplot as plt
import numpy as np

"""
#real sinewave:
A = .8
f0 = 1000
phi = np.pi/2
fs = 44100
t = np.arange (-0.002, .002, 1.0/fs)
x = A * np.cos (2 * np.pi * f0 * t + phi)
"""

#complex sinewave
N = 32
k = 5 #frequency
n = np.arange (-N/2, N/2)
s = np.exp (1j * 2 * np.pi * k * n / N)

plt.plot(n, np.imag(s)) #imaginary part
#plt.plot(n, np.real(s)) #real part
plt.axis([-N/2, N/2 -1, -1, 1])
plt.xlabel('n (time index)')
plt.ylabel('amplitude')

"""
plt.plot (t, x)
plt.axis([-0.002, .002, -0.8, .8])
plt.xlabel('time')
plt.ylabel('amplitude')
"""

plt.show()
