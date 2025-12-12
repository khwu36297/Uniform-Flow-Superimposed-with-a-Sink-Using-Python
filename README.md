##⚙️ README.md: Potential Flow Simulation (Uniform Flow + Sink)```markdown
# 🌊 Potential Flow Simulation: Uniform Flow Superimposed with a Sink

## 📄 Brief Description

[cite_start]This project simulates the two-dimensional (2D) potential flow created by the superposition of a **Uniform Flow** and a **Point Sink** located at the origin[cite: 6, 30]. [cite_start]The analysis relies entirely on exact analytical expressions for the potential function ($\Phi$), stream function ($\Psi$), and the velocity field $(u, v)$[cite: 7, 78]. [cite_start]The simulation is implemented using Python with NumPy and Matplotlib to generate high-resolution flow visualizations, including streamlines, equipotential lines, and velocity quiver plots[cite: 7, 9, 32].

## ✨ Key Features

* [cite_start]**Analytic Formulation:** Utilizes the exact analytic expressions for $\Phi$, $\Psi$, and the velocity components $(u, v)$ of the superimposed flow [cite: 7, 59-64].
* [cite_start]**Singularity Handling:** A masking strategy (masking radius) is applied around the origin to manage the mathematical singularity near the sink, ensuring the visualization remains physically interpretable outside this zone [cite: 8, 73, 85-87, 186].
* [cite_start]**Stagnation Point Identification:** The location of the stagnation point is analytically calculated and successfully identified in the simulation at $x_{stag} = \Lambda / (2\pi U_{\infty})$ on the positive $x$-axis [cite: 10, 66-68, 88].
* [cite_start]**High-Quality Visualization:** Generates visualizations where streamlines are colored by velocity magnitude ($|V|$) and contours of $\Phi$ and $\Psi$ are plotted simultaneously to demonstrate their orthogonality [cite: 9, 92, 182-184].

## 📐 Theoretical Basis and Governing Equations

[cite_start]The total flow is governed by the Superposition Principle[cite: 58].

| Function | Superposition Formula |
| :--- | :--- |
| **Potential Function ($\Phi$)** | [cite_start]$\Phi = \Phi_{uniform} + \Phi_{sink} = U_{\infty}x - \frac{\Lambda}{2\pi}\ln r$ [cite: 59] |
| **Stream Function ($\Psi$)** | [cite_start]$\Psi = \Psi_{uniform} + \Psi_{sink} = U_{\infty}y - \frac{\Lambda}{2\pi}\theta$ [cite: 60] |
| **Velocity Component ($u$)** | [cite_start]$u(x, y) = U_{\infty} - \frac{\Lambda}{2\pi}\frac{x}{r^2}$ [cite: 63] |
| **Velocity Component ($v$)** | [cite_start]$v(x, y) = -\frac{\Lambda}{2\pi}\frac{y}{r^2}$ [cite: 64] |
| **Stagnation Point ($x_{stag}$)** | [cite_start]$x_{stag} = \frac{\Lambda}{2\pi U_{\infty}}$ [cite: 68] |

> **Note:** $U_{\infty}$ is the uniform flow speed, $\Lambda$ is the sink strength, $r = \sqrt{x^2 + y^2}$, and $\theta = \arctan2(y, x)$.

## 💻 How to Run

### Requirements

This project requires Python 3 and the following libraries:
* [cite_start]**NumPy:** For vector and matrix operations[cite: 7].
* [cite_start]**Matplotlib:** For visualization and plotting[cite: 7, 94].

You can install them using pip:

```bash
pip install numpy matplotlib

```

###Running the Script1. Save the complete Python code from **Appendix A** of the report into a file named `potential_flow_full.py`.
2. Open your Terminal or Command Prompt in the same directory as the file.
3. Execute the script with the command:

```bash
python potential_flow_full.py

```

The script will display the flow visualization (streamlines and contours) and save a high-resolution figure named `potential_flow_full.png`.

##🔧 Key Code ParametersThese parameters can be adjusted in the `--- Parameters ---` section of the Python code .

| Variable | Description | Default Value (in code) | Relevant Formula |
| --- | --- | --- | --- |
| `U_inf` | Uniform flow speed (\mathbf{U_{\infty}}) | `1.0` | <br>\Phi_{uniform}=U_{\infty}x 

 |
| `Lambda` | Sink strength (\mathbf{\Lambda}) | `2 * np.pi * 1.0` | <br>\Phi_{sink}=-\frac{\Lambda}{2\pi}\ln r 

 |
| `mask_radius` | Radius used for masking the singularity at the origin | `0.12` | N/A (Computational technique) |

##👤 Author and Affiliation* 
**Proposed by:** Mr. Sorasak Laopraphaiphan 


* 
**Affiliation:** Department of Mechanical and Aerospace Engineering 


* 
**Date:** 13 December 2025 



```

```
