# 🛩️ Crazyflie Altitude Guard – Python FSM Simulation

A lightweight Python simulation that mimics a **table-top altitude guard** system for a drone (Crazyflie 2.1), using a **finite state machine (FSM)** to maintain stable flight at a target altitude.  

This project simulates sensor readings, logs altitude data, visualizes the altitude graph, and analyzes system behavior using FSM logic.

---

## 📁 Project Structure

```bash
iot_project/
├── step1_altitude_guard_simulation.py     # Simulates altitude and FSM transitions
├── step2_altitude_graph.py                # Plots altitude graph over time
├── step3_logger.py                        # Logs altitude and state to CSV
├── step4_analysis.py                      # Analyzes performance metrics
├── drone_altitude_log.csv                 # Logged data from logger script
├── altitude_log.csv                       # Additional log file for visualization
└── README.md                              # Project documentation

⚙️ Setup & Environment
🔧 Requirements
This project uses standard Python libraries.
No external dependencies are required beyond the standard library.

Python ≥ 3.8

Libraries used:

asyncio

random

datetime

csv

matplotlib

pandas

💡 Recommended installation
We recommend using a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install pandas matplotlib
🚀 How to Run
Simulate the altitude system
Run the simulation script to observe time-stamped drone altitude and state transitions:

bash
Copy
Edit
python step1_altitude_guard_simulation.py
Log altitude and states
This script saves the altitude data and states into a CSV file:

bash
Copy
Edit
python step3_logger.py
➤ Output: drone_altitude_log.csv

Plot altitude graph
Generate a plot showing the altitude trend over time:

bash
Copy
Edit
python step2_altitude_graph.py
Analyze results
Run this to compute key performance metrics:

bash
Copy
Edit
python step4_analysis.py
➤ Output includes:

Minimum and maximum altitude

Number of ALERT state triggers

System response metrics

📊 Sample Output
📈 Real-time altitude graph with target threshold

📁 CSV log of drone states and altitudes

📉 Analysis of system stability and state transitions
