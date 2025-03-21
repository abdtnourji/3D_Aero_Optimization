# optimization_standard.py

import numpy as np
import pandas as pd
from simulation import Aircraft3D, FlightSimulator3D
from config import SIMULATION, AIRCRAFT, ENVIRONMENT, OPTIMIZATION_STANDARD

def standard_optimization():
    thrust_range = np.linspace(OPTIMIZATION_STANDARD["thrust_range"][0], 
                                 OPTIMIZATION_STANDARD["thrust_range"][1], 
                                 OPTIMIZATION_STANDARD["steps"])
    results = []
    
    for scale in thrust_range:
        params = AIRCRAFT.copy()
        params["thrust"] *= scale
        aircraft = Aircraft3D(params)
        simulator = FlightSimulator3D(aircraft, SIMULATION["time_step"], SIMULATION["max_time"], ENVIRONMENT)
        telemetry_df = simulator.run()
        max_altitude = telemetry_df["z"].max()
        results.append({"thrust_scale": scale, "max_altitude": max_altitude})
    
    results_df = pd.DataFrame(results)
    optimal = results_df.loc[results_df["max_altitude"].idxmax()]
    return optimal, results_df

if __name__ == "__main__":
    optimal, df = standard_optimization()
    print("Standard Optimization Optimal:", optimal)
    print(df)
