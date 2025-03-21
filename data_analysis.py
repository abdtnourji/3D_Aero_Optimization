# data_analysis.py

import pandas as pd

def compare_optimizations(std_results, ai_results, hybrid_result):
    """
    Compare maximum altitudes and thrust scaling factors from three optimization cases.
    Return a summary DataFrame.
    """
    summary = pd.DataFrame({
        "Method": ["Standard", "AI-Enhanced", "Hybrid"],
        "Thrust_Scale": [
            std_results.loc[std_results["max_altitude"].idxmax()]["thrust_scale"],
            ai_results["optimal_thrust_scale"],
            hybrid_result["hybrid_thrust_scale"]
        ],
        "Max_Altitude": [
            std_results["max_altitude"].max(),
            ai_results["max_altitude"],
            hybrid_result["max_altitude"]
        ]
    })
    return summary

if __name__ == "__main__":
    from optimization_standard import standard_optimization
    from optimization_ai import ai_optimization_dummy
    from optimization_hybrid import hybrid_optimization
    
    std_opt, std_df = standard_optimization()
    ai_opt, ai_df = ai_optimization_dummy()
    hybrid_opt, _, _ = hybrid_optimization()
    
    summary = compare_optimizations(std_df, ai_opt, hybrid_opt)
    print(summary)
