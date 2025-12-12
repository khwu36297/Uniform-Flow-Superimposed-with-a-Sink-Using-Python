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
