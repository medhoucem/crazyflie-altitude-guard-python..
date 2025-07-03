
import asyncio
import random
import datetime

# Constants for simulation
TARGET_ALTITUDE = 0.7
THRESHOLD = 0.05
SIM_DURATION_SEC = 30  # Total duration of the simulation

# State machine states
class DroneState:
    HOLD_STABLE = "HOLD_STABLE"
    ADJUST_UP = "ADJUST_UP"
    ADJUST_DOWN = "ADJUST_DOWN"
    ALERT = "ALERT"

# FSM logic
def determine_state(current_altitude, prev_altitude):
    delta = current_altitude - prev_altitude
    if abs(current_altitude - TARGET_ALTITUDE) <= THRESHOLD:
        return DroneState.HOLD_STABLE, delta
    elif current_altitude < TARGET_ALTITUDE - THRESHOLD:
        return DroneState.ADJUST_UP, delta
    elif current_altitude > TARGET_ALTITUDE + THRESHOLD:
        return DroneState.ADJUST_DOWN, delta
    else:
        return DroneState.ALERT, delta

# Simulated altitudes with occasional noise
async def simulate_drone():
    current_altitude = TARGET_ALTITUDE
    log = []
    start_time = datetime.datetime.now()

    while (datetime.datetime.now() - start_time).total_seconds() < SIM_DURATION_SEC:
        noise = random.uniform(-0.1, 0.1)
        drift = random.uniform(-0.15, 0.15) if random.random() < 0.1 else 0.0
        new_altitude = current_altitude + noise + drift

        state, delta = determine_state(new_altitude, current_altitude)
        timestamp = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
        print(f"[{timestamp}] State: {state:<13} | Altitude: {new_altitude:.3f} m | Δ: {delta:+.3f} m")

        log.append((timestamp, state, new_altitude, delta))
        current_altitude = new_altitude
        await asyncio.sleep(0.1)

    return log

# Entry point
if __name__ == "__main__":
    asyncio.run(simulate_drone())
