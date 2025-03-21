# main.py

import pandas as pd
from simulation import Aircraft3D, FlightSimulator3D
from config import SIMULATION, AIRCRAFT, ENVIRONMENT
from optimization_standard import standard_optimization
from optimization_ai import ai_optimization_dummy
from optimization_hybrid import hybrid_optimization
from data_analysis import compare_optimizations

def main():
    # Run baseline simulation for visualization
    aircraft = Aircraft3D(AIRCRAFT)
    simulator = FlightSimulator3D(aircraft, SIMULATION["time_step"], SIMULATION["max_time"], ENVIRONMENT)
    telemetry_df = simulator.run()
    telemetry_df.to_csv("3d_flight_data.csv", index=False)
    
    # Run Standard Optimization
    std_opt, std_results = standard_optimization()
    
    # Run AI-Enhanced Optimization (dummy)
    ai_opt, ai_training = ai_optimization_dummy()
    
    # Run Hybrid Optimization
    hybrid_opt, _, _ = hybrid_optimization()
    
    # Compare results
    summary = compare_optimizations(std_results, ai_opt, hybrid_opt)
    print("Optimization Comparison Summary:")
    print(summary)
    summary.to_csv("optimization_comparison.csv", index=False)
    
    print("Simulation and optimization completed.")
    print("Launch the 3D visualization dashboard with: streamlit run visualization.py")
    
if __name__ == "__main__":
    main()
# In this script, we import the necessary functions from the other modules and run them sequentially. We save the results and summary data to CSV files for further analysis or visualization. The final message provides instructions on how to launch the Streamlit dashboard for 3D visualization.