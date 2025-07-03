# Crazyflie Altitude Guard – Python Simulation

This project simulates an **altitude guard** mechanism for a Crazyflie drone using Python.  
It models an FSM (Finite State Machine) that monitors the drone's altitude and triggers alerts or corrections based on deviations from a target altitude.

---

## 🚁 Project Overview

- A simulation of the drone's altitude readings over time
- FSM states:
  - `HOLD_STABLE`
  - `ADJUST_UP`
  - `ADJUST_DOWN`
  - `ALERT`
- Generates logs and visual graphs to analyze drone behavior.

---

## ⚙️ Environment Setup

Make sure you have Python 3.10+ installed.

### Install required libraries:

```bash
pip install matplotlib pandas
