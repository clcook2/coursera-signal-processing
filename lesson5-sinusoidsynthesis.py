import numpy as np
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'sms-tools-master/software/models/'))
import utilFunctions as UF
import dftModel as DFT
import matplotlib.pyplot as plt
from scipy.signal import blackmanharris, triang, get_window
from scipy.fftpack import ifft

bins = np.array([-4, -3, -2, -1, 0, 1, 2, 3])
X = UF.genBhLobe(bins)      #blackman harris is the sum of four sinc functions,
                            #this function finds the values of a blackman harris
                            #curve for given bins

(fs, x) = UF.wavread('sms-tools-master/sounds/oboe-A4.wav')
M = 501
#N = 512
Ns = 512
hNs = int(Ns/2)
H = int(Ns/4)
t = -70  #min threshold from the peak for other peaks
w = get_window('hamming', M)
x1 = x[int(.8*fs):int(.8*fs) + M]
mX, pX = DFT.dftAnal(x1, w, Ns)
peaks = UF.peakDetection(mX, t)

ipeaks, iMag, iPhase = UF.peakInterp(mX, pX, peaks)
ipfreq = fs * ipeaks / float(Ns)

#ipfreq = np.array([3000.0, 4000.0])
#iMag = np.array([0.0, 0.0])
#iPhase = np.array([0.0, 0.0])
Y = UF.genSpecSines_p(ipfreq, iMag, iPhase, Ns, fs)

y = np.real(ifft(Y))
print(y.size)

sw = np.zeros(Ns) #code in order to undo the blackman harris window and apply triangular function
ow = triang(Ns/2)
sw[hNs-H:hNs + H] = ow
bh = blackmanharris(Ns)
bh = bh / sum(bh)
sw[hNs-H:hNs + H] = sw[hNs-H:hNs+H] / bh[hNs-H:hNs+H]

yw = np.zeros(Ns)
yw[:hNs-1] = y[hNs+1:]
yw[hNs-1:] = y[:hNs+1]
yw *= sw

freqaxis = fs*np.arange(Ns/2 + 1)/float(Ns)

plt.plot(freqaxis, mX)
plt.plot(fs * ipeaks / float(Ns), iMag, marker = 'x', linestyle = '')

"""
absY = abs(Y[:int(Ns/2)])
absY[absY<np.finfo(float).eps] = np.finfo(float).eps

plt.plot(freqaxis, 20*np.log10(absY))
plt.show()
"""
