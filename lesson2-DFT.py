import numpy as np
import matplotlib.pyplot as plt

#complex signal
N = 64
k0 = 7.5
xC = np.exp(1j * 2 * np.pi * k0 / N * np.arange(N)) #complex
x = np.cos(2 * np.pi * k0 / N * np.arange(N)) #real

X = np.array([])
nv = np.arange(-N/2, N/2)
kv = np.arange(-N/2, N/2)

"""
#Complex
for k in range(N):
    s = np.exp(1j * 2 * np.pi * k / N * np.arange(N))
    X = np.append(X, sum(xC*np.conjugate(s)))

for k in kv:
    s = np.exp(1j * 2 * np.pi * k / N * np.arange(N))
    X = np.append(X, sum(x*np.conjugate(s)))

y = np.array([])
for n in nv:
    s = np.exp(1j * 2 * np.pi * n / N * kv)
    y = np.append(y, 1.0/N * sum(X*s))


#complex plot
plt.plot (np.arange(N), abs(X))
plt.axis([0, N-1, 0, N])
"""
N = 4
kv = np.arange(N)
x = np.cos(2 * np.pi * k0 / N * np.arange(N))
y = np.array([])
nv = np.arange(-N/2, N/2)
X = np.array([4, 0, 0, 0])

for n in nv:
    s = np.exp(1j * 2 * np.pi * n / N * kv)
    y = np.append(y, 1.0/N * sum(X*s))

print(y)

plt.plot (nv, X)
plt.axis([-N/2, N/2 -1, -1, N])

plt.show()
