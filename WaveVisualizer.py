import matplotlib.pyplot as plt
import numpy as np
from WaveTableSynthesis import waveform

x = np.linspace(0, 20, 100) # creates a list
# of evenly spaced numbers over the range

plt.plot(x, waveform)   # Plot sine of each point
plt.show()              # Display Plot