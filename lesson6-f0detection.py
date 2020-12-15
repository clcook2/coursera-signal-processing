import numpy as np
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'sms-tools-master/software/models/'))
import utilFunctions as UF
import dftModel as DFT
import harmonicModel as HM
from scipy.signal import get_window

'''
fs, x = UF.wavread('sms-tools-master/sounds/sawtooth-440.wav')
N = 1024
M = 601
t = -60
minf0 = 50
maxf0 = 2000

hN = N/2
hM = (M+1)/2

w = get_window('hamming', M)
start = .8*fs
x1 = x[int(start): int(start+M)]
mX, pX = DFT.dftAnal(x1, w, N)
ploc = UF.peakDetection(mX, t)
iploc, ipmag, ipphase = UF.peakInterp(mX, pX, ploc)
ipfreq = fs * iploc / N
f0c = np.argwhere((ipfreq > minf0) & (ipfreq < maxf0))[:, 0]
f0cf = ipfreq[f0c]
f0, f0Error = UF.TWM_p(ipfreq, ipmag, f0cf)
'''
#fs, x = UF.wavread('sms-tools-master/sounds/sawtooth-440.wav')
fs, x = UF.wavread('sms-tools-master/sounds/oboe-A4.wav')
N = 2048
M = 1001
t = -50
minf0 = 300
maxf0 = 500
H = 1000
w = get_window('blackman', M)
f0et = 1

f0 = HM.f0Detection(x, fs, w, N, H, t, minf0, maxf0, f0et)
#has an array because it finds the fundamental frequency in different points of
#time as per the hop size

