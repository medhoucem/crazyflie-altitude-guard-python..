# ✈️ Crazyflie Altitude Guard – Python FSM Simulation

A lightweight Python simulation that mimics a **table-top altitude guard** system for a drone (Crazyflie 2.1), using a **finite state machine (FSM)** to maintain stable flight at a target altitude.

This project simulates sensor readings, logs altitude data, visualizes the altitude graph, and analyzes system behavior using FSM logic.

---



---

## ⚙️ Setup & Environment

### 🔧 Requirements

This project uses standard Python libraries.  
No external dependencies are required beyond the standard library.

Python ≥ 3.8

Libraries used:
- `asyncio`
- `random`
- `datetime`
- `csv`
- `matplotlib`
- `pandas`

### 🐍 Virtual Environment (optional)

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install pandas matplotlib

🚀 How to Run
1. Simulate the altitude system
python step1_altitude_guard_simulation.py
🔹 This will print time-stamped drone altitude and state transitions.

2. Log altitude and states

python step3_logger.py
📄 Output: drone_altitude_log.csv

3. Plot altitude graph

python step2_altitude_graph.py
📈 Outputs a plot of altitude over time.

4. Analyze results

python step4_analysis.py
📊 You will get:

Minimum & Maximum altitude

Number of ALERT triggers

System response metrics
