import matplotlib.pyplot as plt

def analyze_performance(driver, laps, times):
    plt.figure(figsize=(10, 6))
    
    # Plotting the data
    plt.plot(laps, times, marker='s', color='#2ca02c', label='Lap Time')
    
    # Customizing the chart for a professional look
    plt.title(f"Track Session Analysis: {driver}", fontsize=14, fontweight='bold')
    plt.xlabel("Lap Number", fontsize=12)
    plt.ylabel("Time (seconds)", fontsize=12)
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.legend()

    # Save and show
    plt.savefig('performance_chart.png')
    print("✅ Analysis complete! Performance chart saved as performance_chart.png")

# Simulated session data (10 laps)
lap_numbers = list(range(1, 11))
lap_times = [61.2, 60.5, 60.1, 59.8, 62.4, 59.5, 59.2, 59.9, 60.3, 60.1]

analyze_performance("Continuum_Racer_07", lap_numbers, lap_times)
