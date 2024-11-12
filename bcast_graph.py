import matplotlib.pyplot as plt
import warnings
import numpy as np

# Suppress the numpy warning related to longdouble
warnings.filterwarnings("ignore", category=UserWarning, message=".*longdouble.*")

# Number of processes and corresponding times
processes = [2, 4, 8, 16]
times = [0.004067, 0.009785, 0.018716, 0.060165]

# Create the plot
plt.plot(processes, times, marker='o')
plt.xlabel('Number of Processes')
plt.ylabel('Broadcast Time (seconds)')
plt.title('MPI Broadcast Performance with Fixed Message Size')
plt.grid(True)
plt.show()