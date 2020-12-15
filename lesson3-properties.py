import numpy as np
from scipy.signal import triang
from scipy.fftpack import fft
import sys, os, math
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'sms-tools-master/software/models/'))
import utilFunctions as UF
import dftModel as DFT
from scipy.signal import get_window

#COMPUTES THE MAGNITUDE AND PHASE OF A SPECTRUM

'''
#triangle function fft buffer
x = triang(15)
fftbuffer = np.zeros(15)
fftbuffer[:8] = x[7:]
fftbuffer[8:] = x[:7]
X = fft(fftbuffer)
mX = abs(X)
pX = np.angle(X)
'''

M = 501 #location of the window that we are taking samples from
#helps to find the middle of a window
hM1 = int(math.floor((M+1)/2))
hM2 = int(math.floor(M/2))

fs, x = UF.wavread('sms-tools-master/sounds/soprano-E4.wav')
x1 = x[5000:5000+M] * np.hamming(M)

N = 1024 #number of samples
fftbuffer = np.zeros(N)
fftbuffer[:hM1] = x1[hM2:]
fftbuffer[N-hM2:] = x1[:hM2]

X = fft(fftbuffer)
#mX = abs(X)
mX = 20 * np.log10(abs(X)) #decibels
#pX = np.angle(X)
pX = np.unwrap(np.angle(X)) #unwrapping the phase from notes

#tests the given DFT Model in sms-tools
fs2, x2 = UF.wavread('sms-tools-master/sounds/piano.wav')
M2 = 511
w2 = get_window('hamming', M2)

time = .2
x3 = x2[int(time * fs2):int(time*fs2) + M2]

N2 = 1024
mX2, pX2 = DFT.dftAnal(x3, w2, N2)

y2 = DFT.dftSynth(mX2, pX2, w2.size) * sum(w2)
