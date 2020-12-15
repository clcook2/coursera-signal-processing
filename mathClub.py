import numpy as np
from scipy.fftpack import fft
import sys, os, math
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'sms-tools-master/software/models/'))
import utilFunctions as UF
import dftModel as DFT
import matplotlib.pyplot as plt
from scipy.io import wavfile

#oboe-A4 single note

M = 501 #location of the window that we are taking samples from
hM1 = int(math.floor((M+1)/2))
hM2 = int(math.floor(M/2))

fs, x = UF.wavread('oboe-A4copy.wav')

x1 = x[5000:5000+M] * np.hamming(M)

"""
plt.plot(x)
plt.show()

"""
N = 1024 #number of samples
fftbuffer = np.zeros(N)
fftbuffer[:hM1] = x1[hM2:]
fftbuffer[N-hM2:] = x1[:hM2]

X = fft(fftbuffer) #FOURIER TRANSFORM
mX = 20 * np.log10(abs(X)) #decibels
pX = np.unwrap(np.angle(X)) #unwrapping the phase from notes
plt.plot(np.arange(0, fs/2, fs/float(2*M)), mX[:M])
plt.show()
