import numpy as np
import matplotlib.pyplot as plt
import math

class class_DFT:
    def __init__(self, Signal, Time, Zeropadding):
        self.Signal = Signal
        self.Time = Time
        self.Zeropadding = Zeropadding

    def def_DFT(self):
            N = len(self.Time)
            Fs = 1 / np.mean(np.diff(self.Time))                         # 보통 N으로 씀
            Ts = N/Fs
            M = np.pad(N, (0,2^math.ceil(math.log(N,2)/math.log(2,2))*2^(self.Zeropadding)))

            SampleIndex = np.arange(M)                              # 보통 k로 씀
            freq = SampleIndex/Ts 					                # two sides frequency range
            freq = freq[range(int(N/2))] 	                		# one side frequency range
            y = self.Signal - np.mean(self.Signal)                  # DC_Component

            FFT_out = np.fft.fft(y)/N*2 			                # fft computing and normalization
            FFT_out = FFT_out[range(int(N/2))]
            FFT_Gain = abs(FFT_out)

            return FFT_Gain, freq