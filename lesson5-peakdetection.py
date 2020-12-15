import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import get_window
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'sms-tools-master/software/models/'))
import dftModel as DFT
import utilFunctions as UF

(fs, x) = UF.wavread('sms-tools-master/sounds/sine-440.wav')
M = 501
N = 512
t = -20  #min threshold from the peak for other peaks
w = get_window('hamming', M)
x1 = x[int(.8*fs):int(.8*fs) + M]
mX, pX = DFT.dftAnal(x1, w, N)
peaks = UF.peakDetection(mX, t) #in the util functions file, finds x values/bins
pmag = mX[peaks]

print(peaks)
print(pmag)

print(fs * peaks / N)

#parabolic interpolation
ipeaks, iMag, iPhase = UF.peakInterp(mX, pX, peaks) #iMag is the pMag version with interpolation
print(ipeaks)
print(fs * ipeaks / N)

plt.plot(fs * np.arange(N/2 + 1) / float(N), mX)
plt.plot(fs * ipeaks / float(N), iMag, marker = 'x', linestyle = '')
