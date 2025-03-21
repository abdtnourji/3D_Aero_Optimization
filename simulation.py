# simulation.py

import numpy as np
import pandas as pd
from config import SIMULATION, AIRCRAFT, ENVIRONMENT

class Aircraft3D:
    def __init__(self, params):
        self.name = params["name"]
        self.mass = params["mass"]  # dry mass (kg)
        self.thrust = params["thrust"]
        self.drag_coeff = params["drag_coeff"]
        self.lift_coeff = params["lift_coeff"]
        self.wing_area = params["wing_area"]
        self.isp = params["isp"]
        
        # State: position and velocity (3D vectors)
        self.position = np.array(SIMULATION["initial_state"]["position"], dtype=float)
        self.velocity = np.array(SIMULATION["initial_state"]["velocity"], dtype=float)
        self.time = 0.0

        # New: Fuel properties
        self.fuel = 5000.0  # initial fuel in kg
        # For simplicity, assume fuel consumption rate: thrust / (isp * g)
        self.g0 = ENVIRONMENT["gravity"]

    def update_state(self, dt, env):
        g = env["gravity"]
        
        # Fuel consumption: compute mass flow (kg/s)
        fuel_flow = self.thrust / (self.isp * g)
        delta_fuel = fuel_flow * dt
        
        # Update fuel and adjust thrust if fuel is exhausted
        if self.fuel <= 0:
            self.fuel = 0
            self.thrust = 0
        else:
            self.fuel -= delta_fuel
            if self.fuel < 0:
                self.fuel = 0
                self.thrust = 0

        # Compute aerodynamic forces with wind effect
        rho = env["air_density"]
        # Wind: add variability
        wind_direction = np.array(env["wind"]["direction"], dtype=float)
        wind_speed = env["wind"]["speed"] * (1 + np.random.uniform(-env["wind"]["variation"], env["wind"]["variation"]))
        wind_vector = wind_direction * wind_speed

        # Relative velocity (aircraft velocity relative to wind)
        rel_velocity = self.velocity - wind_vector
        v_rel = np.linalg.norm(rel_velocity)

        # Drag force: F_drag = 0.5 * rho * v_rel^2 * C_D * A
        drag_mag = 0.5 * rho * v_rel**2 * self.drag_coeff * self.wing_area
        drag = -drag_mag * (rel_velocity / (v_rel + 1e-6))
        
        # Lift force (simplified): perpendicular to relative velocity
        lift_mag = 0.5 * rho * v_rel**2 * self.lift_coeff * self.wing_area
        if v_rel > 1e-3:
            perp = np.cross(rel_velocity, np.array([0, 0, 1]))
            if np.linalg.norm(perp) < 1e-3:
                perp = np.cross(rel_velocity, np.array([0, 1, 0]))
            lift_direction = np.cross(perp, rel_velocity)
            lift_direction /= np.linalg.norm(lift_direction)
        else:
            lift_direction = np.array([0, 0, 1])
        lift = lift_mag * lift_direction
        
        # Thrust vector: assume aligned with current velocity if available, else default along x-axis
        if np.linalg.norm(self.velocity) > 1e-3:
            thrust_vector = (self.velocity / np.linalg.norm(self.velocity)) * self.thrust
        else:
            thrust_vector = np.array([self.thrust, 0, 0])
        
        # Gravity force
        gravity_vector = np.array([0, 0, -g * self.mass])
        
        # Total force
        total_force = thrust_vector + drag + lift + gravity_vector
        
        # Compute acceleration
        acceleration = total_force / self.mass
        
        # Update velocity and position (Euler integration)
        self.velocity += acceleration * dt
        self.position += self.velocity * dt
        self.time += dt
        
        return {
            "time": self.time,
            "position": self.position.copy(),
            "velocity": self.velocity.copy(),
            "acceleration": acceleration.copy(),
            "fuel": self.fuel
        }

class FlightSimulator3D:
    def __init__(self, aircraft, dt, max_time, env):
        self.aircraft = aircraft
        self.dt = dt
        self.max_time = max_time
        self.env = env
        self.telemetry = []

    def run(self):
        while self.aircraft.time < self.max_time:
            data = self.aircraft.update_state(self.dt, self.env)
            self.telemetry.append(data)
            # Terminate simulation if altitude falls below zero (crash)
            if self.aircraft.position[2] < 0:
                break
            # Optionally, also break if fuel is exhausted and altitude is dropping
            if self.aircraft.fuel <= 0 and self.aircraft.position[2] < 100:
                break
        # Flatten telemetry for 3D plotting
        rows = []
        for d in self.telemetry:
            row = {
                "time": d["time"],
                "x": d["position"][0],
                "y": d["position"][1],
                "z": d["position"][2],
                "vx": d["velocity"][0],
                "vy": d["velocity"][1],
                "vz": d["velocity"][2],
                "ax": d["acceleration"][0],
                "ay": d["acceleration"][1],
                "az": d["acceleration"][2],
                "fuel": d["fuel"]
            }
            rows.append(row)
        return pd.DataFrame(rows)

if __name__ == "__main__":
    # Quick test run for 3D simulation with fuel consumption
    from config import SIMULATION, AIRCRAFT, ENVIRONMENT
    aircraft = Aircraft3D(AIRCRAFT)
    simulator = FlightSimulator3D(aircraft, SIMULATION["time_step"], SIMULATION["max_time"], ENVIRONMENT)
    telemetry_df = simulator.run()
    print(telemetry_df.head())
