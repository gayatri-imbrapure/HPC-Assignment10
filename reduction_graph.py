import matplotlib.pyplot as plt

# Data
process_counts = [2, 4, 8, 16]
message_sizes = [1000, 10000, 100000, 1000000]

# Example time data for plotting (replace these with your actual times)
times = {
    2: [0.000078, 0.000031, 0.000269, 0.003224],
    4: [0.000139, 0.000061, 0.000550, 0.020732],
    8: [0.000403, 0.000035, 0.000381, 0.003118],
    16: [0.001012, 0.001885, 0.015095, 0.007953],
}

# Plotting
plt.figure(figsize=(10, 6))

for proc in process_counts:
    plt.plot(message_sizes, times[proc], marker='o', label=f'Processes: {proc}')

plt.xscale('log')  # Log scale for message size
plt.yscale('log')  # Log scale for time
plt.xlabel('Message Size (log scale)')
plt.ylabel('Time taken (seconds, log scale)')
plt.title('Performance of MPI Reduction Operation')
plt.legend()
plt.grid(True)
plt.show()
