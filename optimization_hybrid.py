# optimization_hybrid.py

from optimization_standard import standard_optimization
from optimization_ai import ai_optimization_dummy

def hybrid_optimization():
    # Run standard optimization to get a baseline
    standard_optimal, standard_results = standard_optimization()
    
    # Run the AI routine for fine-tuning (dummy example)
    ai_optimal, training_df = ai_optimization_dummy()
    
    # Combine results (for demonstration, simply average the thrust scales)
    hybrid_thrust_scale = (standard_optimal["thrust_scale"] + ai_optimal["optimal_thrust_scale"]) / 2
    # Assume hybrid max altitude is the better of the two (dummy logic)
    hybrid_max_altitude = max(standard_optimal["max_altitude"], ai_optimal["max_altitude"])
    
    hybrid_result = {
        "hybrid_thrust_scale": hybrid_thrust_scale,
        "max_altitude": hybrid_max_altitude
    }
    
    return hybrid_result, standard_results, training_df

if __name__ == "__main__":
    hybrid_result, std_results, ai_training = hybrid_optimization()
    print("Hybrid Optimization Result:", hybrid_result)
