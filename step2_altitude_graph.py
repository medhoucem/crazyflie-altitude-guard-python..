import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Parameters
TARGET_ALTITUDE = 0.7       # meters
THRESHOLD       = 0.05      # ±5 cm for “stable”
SIM_DURATION_SEC= 30        # total run time in seconds
UPDATE_INTERVAL = 0.2       # seconds between frames

# FSM states
class DroneState:
    HOLD_STABLE = "HOLD_STABLE"
    ADJUST_UP   = "ADJUST_UP"
    ADJUST_DOWN = "ADJUST_DOWN"
    ALERT       = "ALERT"

def determine_state(alt, prev_alt):
    dev = alt - TARGET_ALTITUDE
    if abs(dev) <= THRESHOLD:
        return DroneState.HOLD_STABLE, dev
    if abs(dev) > 0.10:      # > ±10 cm → alert
        return DroneState.ALERT, dev
    if dev < -THRESHOLD:
        return DroneState.ADJUST_UP, dev
    return DroneState.ADJUST_DOWN, dev

# Data buffers
times    = []
alts     = []
states   = []
frame    = 0

# Initial altitude
current_alt = TARGET_ALTITUDE

# Set up the plot
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.axhline(TARGET_ALTITUDE, color='green', linestyle='--', label='Target')
ax.axhline(TARGET_ALTITUDE+THRESHOLD, color='red', linestyle=':', label='±Threshold')
ax.axhline(TARGET_ALTITUDE-THRESHOLD, color='red', linestyle=':')
ax.set_xlim(0, SIM_DURATION_SEC/UPDATE_INTERVAL)
ax.set_ylim(0, TARGET_ALTITUDE + 0.5)
ax.set_xlabel('Time (ticks)')
ax.set_ylabel('Altitude (m)')
ax.legend()
ax.grid(True)

def update(_):
    global frame, current_alt

    # simulate sensor: small noise plus rare spike
    noise = random.uniform(-0.05, 0.05)
    spike = random.uniform(-0.2, 0.2) if random.random()<0.05 else 0
    new_alt = current_alt + noise + spike

    state, _ = determine_state(new_alt, current_alt)
    current_alt = new_alt

    times.append(frame)
    alts.append(new_alt)
    states.append(state)
    frame += 1

    ax.clear()
    ax.plot(times, alts, color='blue', label='Altitude')
    ax.axhline(TARGET_ALTITUDE, color='green', linestyle='--', label='Target')
    ax.axhline(TARGET_ALTITUDE+THRESHOLD, color='red', linestyle=':', label='Thresholds')
    ax.axhline(TARGET_ALTITUDE-THRESHOLD, color='red', linestyle=':')
    ax.set_xlim(0, len(times))
    ax.set_ylim(0, TARGET_ALTITUDE + 0.5)
    ax.set_title(f'State: {state}')
    ax.set_xlabel('Time (ticks)')
    ax.set_ylabel('Altitude (m)')
    ax.legend(loc='upper right')
    ax.grid(True)

ani = animation.FuncAnimation(fig, update, frames=int(SIM_DURATION_SEC/UPDATE_INTERVAL),
                              interval=UPDATE_INTERVAL*1000, repeat=False)
plt.tight_layout()
plt.show()
