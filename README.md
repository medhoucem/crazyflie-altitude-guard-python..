# ✈️ Crazyflie Altitude Guard – Python FSM Simulation

A lightweight Python simulation that mimics a **table-top altitude guard** system for a drone (Crazyflie 2.1), using a **finite state machine (FSM)** to maintain stable flight at a target altitude.

This project simulates sensor readings, logs altitude data, visualizes the altitude graph, and analyzes system behavior using FSM logic.

---

## 📁 Project Structure

iot_project/
├── step1_altitude_guard_simulation.py # Simulates altitude and FSM transitions
├── step2_altitude_graph.py # Plots altitude graph over time
├── step3_logger.py # Logs altitude and state to CSV
├── step4_analysis.py # Analyzes performance metrics
├── drone_altitude_log.csv # Logged data from logger script
├── altitude_log.csv # Additional log file for visualization
└── README.md # Project documentation


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
bash
Copy
Edit
python step1_altitude_guard_simulation.py
🔹 This will print time-stamped drone altitude and state transitions.

2. Log altitude and states
bash
Copy
Edit
python step3_logger.py
📄 Output: drone_altitude_log.csv

3. Plot altitude graph
bash
Copy
Edit
python step2_altitude_graph.py
📈 Outputs a plot of altitude over time.

4. Analyze results
bash
Copy
Edit
python step4_analysis.py
📊 You will get:

Minimum & Maximum altitude

Number of ALERT triggers

System response metrics
