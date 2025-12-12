"""
===========================================================
Potential Flow Simulation: Uniform Flow + Sink (Full Version)
Author      : Sorasak Laopraphaiphan
Created     : 13 December 2025
Description :
    This Python script computes and visualizes a 2D potential flow
    consisting of a uniform flow superimposed with a sink at the origin.
    The code includes analytic expressions for the potential function,
    stream function, and velocity field, and provides high-quality
    visualizations similar to CFD post-processing.

Main Features:
    - Analytic potential (Φ) and stream function (Ψ)
    - Analytic velocity field (u, v) from ∂Φ/∂x and ∂Φ/∂y
    - Streamlines colored by speed magnitude (|V|)
    - Potential lines (red dashed) and streamfunction lines (blue)
    - Quiver vector field (downsampled)
    - Automatic stagnation point calculation
    - Singularity handling with epsilon + masking radius
    - Physically consistent aspect ratio and domain control

Notes:
    Φ_uniform = U_inf * x
    Ψ_uniform = U_inf * y
    Φ_sink    = - Λ/(2π) ln(r)
    Ψ_sink    = - Λ/(2π) θ

This script can be extended to:
    - Source, doublet, vortex, cylinder flow
    - Rankine oval and flow past bodies
    - Interactive sliders (Λ, U∞)
    - CFD validation dataset generation
===========================================================
"""

import numpy as np
import matplotlib.pyplot as plt

# --- Parameters ---
U_inf = 1.0                  # Uniform flow velocity
Lambda = 2 * np.pi * 1.0     # Sink strength (positive = sink)
eps = 1e-6                   # To prevent log(0)
mask_radius = 0.12           # Mask near singularity

# --- Grid ---
x_range = np.linspace(-5, 5, 400)
y_range = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x_range, y_range)

# --- Polar helpers ---
R = np.sqrt(X**2 + Y**2)
R_safe = R.copy()
R_safe[R_safe < eps] = eps    # avoid singularity
Theta = np.arctan2(Y, X)

# --- Potential & Stream function (Analytic) ---
Phi_uniform = U_inf * X
Psi_uniform = U_inf * Y

Phi_sink = - (Lambda / (2*np.pi)) * np.log(R_safe)
Psi_sink = - (Lambda / (2*np.pi)) * Theta

Phi = Phi_uniform + Phi_sink
Psi = Psi_uniform + Psi_sink

# --- Velocity field (Analytic derivative of Phi) ---
u = U_inf - (Lambda / (2*np.pi)) * (X / (R_safe**2))
v = - (Lambda / (2*np.pi)) * (Y / (R_safe**2))

V = np.sqrt(u**2 + v**2)   # Speed magnitude

# --- Mask near singularity ---
mask = R < mask_radius
Phi_masked = Phi.copy()
Psi_masked = Psi.copy()
V_masked = V.copy()

Phi_masked[mask] = np.nan
Psi_masked[mask] = np.nan
V_masked[mask] = np.nan

# --- Stagnation point ---
stagnation_x = Lambda / (2 * np.pi * U_inf)
stagnation_point = (stagnation_x, 0.0)

# --- Plotting ---
fig, ax = plt.subplots(figsize=(9, 9))

# Streamplot colored by speed
strm = ax.streamplot(
    X, Y, u, v, color=V,
    cmap='viridis', linewidth=1, density=2
)

# Potential & Streamfunction contours
levels_psi = np.linspace(np.nanmin(Psi_masked), np.nanmax(Psi_masked), 40)
levels_phi = np.linspace(np.nanmin(Phi_masked), np.nanmax(Phi_masked), 40)

ax.contour(X, Y, Psi_masked, levels=levels_psi, colors='blue', linewidths=0.8, alpha=0.7)
ax.contour(X, Y, Phi_masked, levels=levels_phi, colors='red', linestyles='--', linewidths=0.7, alpha=0.6)

# Quiver plot (sparse)
skip = (slice(None, None, 20), slice(None, None, 20))
ax.quiver(X[skip], Y[skip], u[skip], v[skip], scale=40, width=0.0025)

# Mark sink and stagnation point
ax.plot(0, 0, 'ko', markersize=6, label='Sink (0,0)')
ax.plot(stagnation_point[0], stagnation_point[1], 'r*', markersize=12,
        label=f'Stagnation ({stagnation_point[0]:.3f}, 0)')

# Figure settings
ax.set_xlim(x_range.min(), x_range.max())
ax.set_ylim(y_range.min(), y_range.max())
ax.set_aspect('equal', adjustable='box')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Potential Flow: Uniform Flow + Sink\nStreamlines colored by velocity magnitude')
ax.grid(True)
ax.legend(loc='upper right')

# Colorbar
cbar = fig.colorbar(strm.lines, ax=ax)
cbar.set_label('Speed magnitude |V|')

plt.tight_layout()
plt.show()

# --- Save figure ---
fig.savefig("potential_flow_full.png", dpi=300, bbox_inches='tight')
plt.close(fig)
