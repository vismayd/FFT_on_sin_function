import numpy as np
import matplotlib.pyplot as plot
from matplotlib.pyplot import figure, show
from scipy import fftpack

def seperate_sine():
  Fs = 1000
  time = np.arange(0, 10, 1/Fs);

  y1 = 10*(np.sin(2*np.pi*10*time))
  y2 = 10*(np.sin(2*np.pi*50*time))
  y3 = 10*(np.sin(2*np.pi*180*time))

  fig = figure(1)
  ax1 = fig.add_subplot(311)
  ax1.grid(True)
  ax1.set_xticks(np.arange(0, 11, 1.0))
  ax1.plot(time, y1)
  ax1.set_title('f = 10 Hz')

  ax2 = fig.add_subplot(312)
  ax2.set_ylabel('Y')
  ax2.grid(True)
  ax2.set_xticks(np.arange(0, 11, 1.0))
  ax2.plot(time, y2)
  ax2.set_title('f = 50 Hz')

  ax3 = fig.add_subplot(313)
  ax3.set_xlabel('Time')
  ax3.grid(True)
  ax3.plot(time, y3)
  ax3.set_xticks(np.arange(0, 11, 1.0))
  ax3.set_title('f = 180 Hz')
  show()
 


def complicated_sine():

  Fs = 1000
  time = np.arange(0,10,1/Fs);
  y1 = 10*(np.sin(2*np.pi*10*time))
  y2 = 10*(np.sin(2*np.pi*50*time))
  y3 = 10*(np.sin(2*np.pi*180*time))
  #Complicated function
  Yt = y1+y2+y3

  plot.plot(time, Yt)
  #plot.stem(time, Yt, 'r')
  plot.xticks(np.arange(0, 11, 1))
  plot.title('Complicated Function')
  plot.xlabel('Time')
  plot.ylabel('Yt')
  plot.grid(True, which='both')
  plot.axhline(y=0, color='k')
  plot.show()

def fft():
  
  Fs = 1000
  x = [ 10*np.sin(2*np.pi*10 * (i/Fs)) + 20*np.sin(2*np.pi*50 * (i/Fs)) + 30*np.sin(2*np.pi*180 * (i/Fs)) for i in np.arange(Fs)]  
  X = fftpack.fft(x)
  freqs = fftpack.fftfreq(len(x)) * Fs
  plot.stem(freqs, np.abs(X))
  plot.xlabel('Frequency (Hz)')
  plot.ylabel('Frequency Domain Magnitude')
  plot.xlim(0, Fs / 2)
  plot.title('Fast Fourier Transform')
  plot.show()
   
def main():
  seperate_sine()
  complicated_sine()
  fft()

if __name__ == "__main__":
  main()





