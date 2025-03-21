# 3D Aircraft Trajectory Simulation & Optimization Platform

![Project Visualization](docs/simulation_demo.gif)

## Table of Contents
1. [Project Overview](#project-overview)
2. [Physics & Equations](#physics--equations)
3. [System Architecture](#system-architecture)
4. [Installation Guide](#installation-guide)
5. [Running the Project](#running-the-project)
6. [Script Documentation](#script-documentation)
7. [Future Work & Contributions](#future-work--contributions)
8. [References & License](#references--license)

## Project Overview <a name="project-overview"></a>
This research-oriented platform simulates 3D aircraft trajectories under realistic aerodynamic conditions and compares three optimization approaches:
1. **Standard Optimization** - Classical control theory methods
2. **AI-Enhanced Optimization** - Reinforcement Learning (RL) approaches
3. **Hybrid Optimization** - Combined classical+AI methods

Key features:
- 6-DOF flight dynamics modeling
- Wind turbulence and gust simulation
- Interactive 3D visualization
- Quantitative performance comparison

## Physics & Equations <a name="physics--equations"></a>

### Core Equations of Motion
```math
\frac{d\mathbf{v}}{dt} = \frac{\mathbf{F}_{\text{total}}}{m} = \frac{1}{m}(\mathbf{T} + \mathbf{L} + \mathbf{D} + \mathbf{W} + m\mathbf{g})
```

### Aerodynamic Forces
**Lift**:
```math
\mathbf{L} = \frac{1}{2}\rho V^2 S C_L \mathbf{\hat{l}}
```

**Drag**:
```math
\mathbf{D} = \frac{1}{2}\rho V^2 S (C_{D_0} + kC_L^2)\mathbf{\hat{d}}
```

**Wind Model** (Dryden Turbulence):
```math
u_g = \sigma_u \sqrt{\frac{2L_u}{\pi V}} \frac{1}{1 + \frac{L_u\omega}{V}}
```

### Optimization Objectives
```math
\min_{\mathbf{u}} \int_0^{t_f} \left[\dot{m}_{\text{fuel}} + \lambda \|\mathbf{r} - \mathbf{r}_{\text{target}}\|^2 \right] dt
```

## System Architecture <a name="system-architecture"></a>
```
3D_Aero_Optimization/
├── config.py                # Aircraft parameters, environment settings
├── simulation.py            # 6-DOF flight dynamics engine
├── optimization_standard.py # Gradient-based methods
├── optimization_ai.py       # RL agent implementation
├── optimization_hybrid.py   # Combined approaches
├── visualization.py         # 3D Plotly/Streamlit interface
├── main.py                  # Main control script
└── data/                    # Simulation outputs
```

## Installation Guide <a name="installation-guide"></a>

### Requirements
- Python 3.8+
- NVIDIA GPU (recommended for AI optimization)
- 8GB+ RAM

### Windows
```powershell
# Clone repository
git clone https://github.com/yourusername/3D_Aero_Optimization.git
cd 3D_Aero_Optimization

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Linux
```bash
# Clone repository
git clone https://github.com/yourusername/3D_Aero_Optimization.git
cd 3D_Aero_Optimization

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Running the Project <a name="running-the-project"></a>

### VS Code Setup
1. Open project folder
2. Select Python interpreter from `venv`
3. Open integrated terminal

### Basic Execution
```bash
# Run main simulation and optimization
python main.py

# Launch interactive dashboard
streamlit run visualization.py
```

### Key Commands
| Command | Description |
|---------|-------------|
| `python main.py --wind 25` | Set wind speed to 25 m/s |
| `streamlit run visualization.py -- --log_level debug` | Debug mode visualization |

## Script Documentation <a name="script-documentation"></a>

### 1. simulation.py
- **Aircraft3D Class**: 6-DOF dynamics model
- **FlightSimulator3D**: Numerical integration core
- **WindField**: Turbulence modeling

### 2. optimization_standard.py
- Gradient-based optimization
- Parameter sweeps for thrust profiles

### 3. optimization_ai.py
- PPO RL agent implementation
- Reward function design:
  ```python
  def calculate_reward(self):
      return -0.1*self.fuel_used + 2.0*self.altitude
  ```

### 4. visualization.py
- Interactive 3D trajectory plotting
- Performance metric dashboards

![Trajectory Visualization](/image/newplot.png)

## Future Work & Contributions <a name="future-work--contributions"></a>

### Priority TODO List
1. [ ] Implement full quaternion-based attitude representation
2. [ ] Add hardware-in-the-loop (HITL) interface
3. [ ] Integrate real weather data API
4. [ ] Develop formal verification module

### Contribution Guidelines
1. Fork the repository
2. Create feature branch:
   ```bash
   git checkout -b feature/new-aeromodel
   ```
3. Submit pull request with:
   - Documentation updates
   - Unit tests
   - Type hints
   - PEP8 compliance

### Research Opportunities
1. Deep reinforcement learning for turbulence mitigation
2. Multi-objective trajectory optimization
3. Digital twin integration

## References & License <a name="references--license"></a>

### Key References
1. Stevens, B. L.: *Aircraft Control and Simulation*
2. Sutton, R. S.: *Reinforcement Learning: An Introduction*
3. NASA Technical Memorandum 104330: *Wind Turbulence Models*

### License
Apache 2.0 License - See [LICENSE](LICENSE)
