# config.py

# Simulation settings
SIMULATION = {
    "time_step": 0.05,       # seconds
    "max_time": 1200,        # seconds (simulate longer flights)
    "initial_state": {
        "position": [0.0, 0.0, 0.0],  # x, y, z (meters)
        "velocity": [150.0, 0.0, 0.0]   # Vx, Vy, Vz (m/s)
    }
}

# Aircraft properties (3D model)
AIRCRAFT = {
    "name": "Aero3D-X",
    "mass": 15000,         # kg
    "thrust": 1.5e6,       # Newtons
    "drag_coeff": 0.35,    # dimensionless
    "wing_area": 60.0,     # m²
    "lift_coeff": 0.8,     # typical lift coefficient
    "isp": 320             # seconds
}

# Environmental conditions
ENVIRONMENT = {
    "gravity": 9.81,       # m/s²
    "air_density": 1.225,  # kg/m³ (at sea level)
    # Wind field parameters (harsh wind scenario)
    "wind": {
        "speed": 30.0,         # m/s (gust intensity)
        "direction": [1, 0, 0],  # unit vector in x direction
        "variation": 0.3       # variability factor
    }
}

# AI / Optimization parameters
AI_SETTINGS = {
    "episodes": 500,
    "learning_rate": 0.0005,
    "gamma": 0.95,
    "max_steps": 2400       # max simulation steps per episode
}

# Standard optimization settings (for parameter sweep)
OPTIMIZATION_STANDARD = {
    "thrust_range": [0.8, 1.2],  # 80% to 120% of nominal thrust
    "steps": 10
}
