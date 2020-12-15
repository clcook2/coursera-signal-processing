import numpy as np
import matplotlib.pyplot as plt
import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'sms-tools-master/software/models/'))
from scipy.signal import get_window
import utilFunctions as UF
import sineModel as SM
import harmonicModel as HM

inputFile = 'sms-tools-master/sounds/vignesh.wav'
window = 'blackman'
M = 1201
N = 2048
t = -90
minSineDur = 0.1
nH = 50
minf0 = 130
maxf0 = 300
f0et = 5
harmDevSlope = 0.01
H = 128

fs, x = UF.wavread(inputFile)
w = get_window(window, M)

hfreq, hmag, hphase = HM.harmonicModelAnal(x, fs, w, N, H, t, nH, minf0, maxf0, f0et, harmDevSlope, minSineDur)

hfreq[hfreq<=0] = np.nan
plt.plot(H*np.arange(int(hfreq[:,0].size))/float(fs), hfreq)

plt.show()
