import pandas as pd
import matplotlib.pyplot as plt

# Load the logged CSV file
df = pd.read_csv('drone_altitude_log.csv')

# Separate states for color plotting
hold = df[df['State'] == 'HOLD_STABLE']
adjust = df[df['State'].str.startswith('ADJUST')]
alert = df[df['State'] == 'ALERT']

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(df['Time(s)'], df['Altitude(m)'], color='lightgray', label='Altitude (raw trace)', linewidth=1)

plt.scatter(hold['Time(s)'], hold['Altitude(m)'], color='green', label='HOLD_STABLE')
plt.scatter(adjust['Time(s)'], adjust['Altitude(m)'], color='orange', label='ADJUST')
plt.scatter(alert['Time(s)'], alert['Altitude(m)'], color='red', label='ALERT')

# Draw target and thresholds
target = 0.7
threshold = 0.05
plt.axhline(target, color='blue', linestyle='--', label='Target')
plt.axhline(target + threshold, color='gray', linestyle=':', label='Thresholds')
plt.axhline(target - threshold, color='gray', linestyle=':')

# Labels
plt.title('Drone Altitude FSM State Visualization')
plt.xlabel('Time (s)')
plt.ylabel('Altitude (m)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Summary statistics
total_duration = df['Time(s)'].iloc[-1]
alert_duration = alert['Time(s)'].iloc[-1] - alert['Time(s)'].iloc[0] if not alert.empty else 0

print("\n=== Flight Summary ===")
print(f"Total duration: {total_duration:.1f} seconds")
print(f"Time in ALERT state: {alert_duration:.1f} seconds")
print(f"Percentage in ALERT: {100 * alert_duration / total_duration:.1f}%")
