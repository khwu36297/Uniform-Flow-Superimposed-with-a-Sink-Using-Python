# Potential Flow Simulation: Uniform Flow Superimposed with a Sink

## 📋 Overview
This project implements a two-dimensional potential flow simulation combining a uniform flow with a point sink at the origin. The simulation is built using Python with analytical formulations from classical potential flow theory, providing an exact mathematical representation of the flow field.

## 🎯 Key Features
- **Analytical Solution**: Exact expressions for potential function (Φ), stream function (Ψ), and velocity field (u, v)
- **Comprehensive Visualization**:
  - Streamlines colored by velocity magnitude
  - Equipotential lines (red dashed)
  - Stream function contours (blue)
  - Sparse quiver plot showing velocity vectors
- **Stagnation Point Analysis**: Automatic calculation and visualization of the stagnation point
- **Singularity Handling**: Numerical masking near the sink to ensure stability
- **High-Resolution Output**: Publication-quality figures (PNG format, 300 DPI)

## 📊 Flow Configuration
The simulation models the superposition of:
- **Uniform Flow**: Constant velocity U∞ in the positive x-direction
- **Point Sink**: Located at the origin with strength Λ

### Mathematical Formulation
- **Potential Function**: Φ = U∞x - (Λ/2π) ln(r)
- **Stream Function**: Ψ = U∞y - (Λ/2π)θ
- **Velocity Components**:
  - u = U∞ - (Λ/2π)(x/r²)
  - v = -(Λ/2π)(y/r²)
- **Stagnation Point**: x_stag = Λ/(2πU∞), y_stag = 0

## 🛠️ Installation & Requirements

### Dependencies
- Python 3.7+
- NumPy
- Matplotlib

### Installation
```bash
pip install numpy matplotlib
```

## 🚀 Usage
Run the simulation script:
```bash
python Chapter03_UniformSink.py
```

### Key Parameters (Adjustable in Code)
```python
U_inf = 1.0          # Uniform flow velocity
Lambda = 2 * np.pi   # Sink strength
mask_radius = 0.12   # Masking radius around sink
```

## 📈 Output
The script generates:
1. **Interactive Plot**: Displays during execution with:
   - Color-mapped streamlines
   - Potential and stream function contours
   - Velocity vectors
   - Marked sink and stagnation points
2. **Saved Figure**: `potential_flow_full.png` (300 DPI)

## 🧪 Validation
- Stagnation point location matches theoretical prediction
- Orthogonality between potential and stream function lines
- Symmetry about x-axis
- Velocity magnitude proportional to 1/r near sink

## 📚 Educational Value
This project serves as an excellent educational tool for:
- Understanding potential flow theory fundamentals
- Learning superposition principles in fluid mechanics
- Visualizing harmonic conjugate functions (Φ and Ψ)
- Preparing for advanced CFD studies

## 🔮 Future Extensions
The code can be extended to model:
- Sources, doublets, and vortices
- Flow past cylinders and airfoils
- Rankine oval formation
- Interactive parameter sliders
- Lattice Boltzmann Method validation

## 👨‍💻 Author
**Sorasak Laopraphaiphan**  
- Undergraduate student, Department of Mechanical and Aerospace Engineering  
- King Mongkut's University of Technology North Bangkok  
- Concurrent Computer Science student, Ramkhamhaeng University  

**Research Interests**: Analytical/Computational Fluid Dynamics, Potential Flow Theory, Numerical Methods, Aerodynamics

## 📄 License
This project is provided for educational and research purposes. Please cite appropriately if used in academic work.

## 📚 References
- Anderson, J. D. (2010). *Fundamentals of Aerodynamics*
- Batchelor, G. K. (2000). *An Introduction to Fluid Dynamics*
- Kundu, P. K., Cohen, I. M., & Dowling, D. R. (2016). *Fluid Mechanics*
- Milne-Thomson, L. M. (1968). *Theoretical Hydrodynamics*
```
