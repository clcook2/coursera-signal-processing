import numpy as np
from scipy.signal import get_window, resample
import math
import sys, os, time
from scipy.fftpack import fft, ifft
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'sms-tools-master/software/models/'))
import utilFunctions as UF
import stochasticModel as SM
import harmonicModel as HM
import dftModel as DFT

fs, x = UF.wavread('sms-tools-master/sounds/ocean.wav')
M = N = 256

stocf = 0.2

w = get_window('hanning', M)
xw = x[10000:10000+M] * w
X = fft(xw)
mX = 20*np.log10(abs(X[:int(N/2)])) #N/2 samples
mXenv = resample(np.maximum(-200, mX), int(N/2 * stocf)) #downsampling the input signal

mY = resample(mXenv, int(N/2)) #upsampling
pY = 2 * np.pi * np.random.rand(int(N/2))
Y = np.zeros(N, dtype = complex)
Y[:int(N/2)] = 10 ** (mY / 20) * np.exp(1j * pY)
Y[int(N/2 + 1):] = 10 ** (mY[:0:-1] / 20) * np.exp(-1j * pY[:0:-1])
y = np.real(ifft(Y))

H = 128
#stocEnv = SM.stochasticModelAnal(x, H, N, stocf)


