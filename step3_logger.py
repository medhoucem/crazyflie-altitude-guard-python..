import asyncio
import random
import datetime
import csv

# Constants
TARGET_ALTITUDE = 0.7
THRESHOLD = 0.05
SIM_DURATION_SEC = 30
LOG_FILE = "altitude_log.csv"

class DroneState:
    HOLD_STABLE = "HOLD_STABLE"
    ADJUST_UP = "ADJUST_UP"
    ADJUST_DOWN = "ADJUST_DOWN"
    ALERT = "ALERT"

def determine_state(current_altitude, prev_altitude):
    delta = current_altitude - TARGET_ALTITUDE
    if abs(delta) <= THRESHOLD:
        return DroneState.HOLD_STABLE, delta
    elif delta < -THRESHOLD:
        return DroneState.ADJUST_UP, delta
    elif delta > THRESHOLD:
        if abs(delta) > 0.1:
            return DroneState.ALERT, delta
        return DroneState.ADJUST_DOWN, delta

def initialize_logger():
    with open(LOG_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Time(s)", "Altitude(m)", "Delta(m)", "State"])

def log_to_csv(timestamp, time_sec, altitude, delta, state):
    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, time_sec, round(altitude, 3), round(delta, 3), state])

async def simulate_and_log():
    initialize_logger()
    prev_altitude = TARGET_ALTITUDE
    start_time = datetime.datetime.now()

    for tick in range(SIM_DURATION_SEC * 2):  # 0.5s interval
        current_time = datetime.datetime.now()
        elapsed = (current_time - start_time).total_seconds()

        # Simulated altitude with slight randomness and occasional fault
        noise = random.uniform(-0.02, 0.02)
        fault = random.choice([0, 0, 0, 0.15]) if random.random() < 0.1 else 0
        current_altitude = prev_altitude + noise + fault

        state, delta = determine_state(current_altitude, prev_altitude)

        print(f"[{elapsed:.1f}s] Altitude: {current_altitude:.2f} m → State: {state}")
        log_to_csv(current_time.strftime("%H:%M:%S"), round(elapsed, 1), current_altitude, delta, state)

        prev_altitude = current_altitude
        await asyncio.sleep(0.5)

if __name__ == "__main__":

    asyncio.run(simulate_and_log())
