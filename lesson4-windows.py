import numpy as np
from scipy.signal import get_window
from scipy.fftpack import fft
import math
import matplotlib.pyplot as plt
import sys
sys.path.append('sms-tools-master/software/models/')
import dftModel as DFT

#modeling the various windows

M = 63 #window size, odd
window = get_window('hanning', M) #can change the window for different mXs
hM1 = int(math.floor((M+1)/2))
hM2 = int(math.floor(M/2))

N = 512 #fft size
hN = int(N/2)
fftbuffer = np.zeros(N)
fftbuffer[:hM1] = window[hM2:]
fftbuffer[N-hM2:] = window[:hM2]

X = fft(fftbuffer)
absX = abs(X)
absX[absX<np.finfo(float).eps] = np.finfo(float).eps #checks if the value is less than epsilon
mX = 20*np.log(absX)
pX = np.angle(X)

#centers the mX so that the lobe is i the middle
mX1 = np.zeros(N)
pX1 = np.zeros(N)
mX1[:hN] = mX[hN:]
mX1[N-hN:] = mX[:hN]
pX1[:hN] = pX[hN:]
pX1[N-hN:] = pX[:hN]

plt.plot(np.arange(-hN, hN)/float(N)*M, mX)
plt.show()

'''
#plotting a sinusoid
fs = 44100
f = 5000.0
f2 = 2000.0
nM = 101
x = np.cos(2*np.pi*f*np.arange(nM)/float(fs))
x2 = np.cos(2*np.pi*f2*np.arange(nM)/float(fs))
xA = x+x2
nN = 512
nW = get_window('blackmanharris2', nM)
mX, pX = DFT.dftAnal(xA, nW, nN)

plt.plot(np.arange(0, (fs/2 +fs/float(nN)), fs/float(nN)), mX)
plt.show()
'''
