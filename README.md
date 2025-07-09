# 🧬 Nucleus Tensegrity Model

A novel approach to modeling atomic nuclei based on **tensegrity structures**—spatially constrained 3D graphs representing protons and neutrons as nodes, with physical interactions as edges.

This model extends classical proton-neutron (Z/N) nuclear charts by introducing **geometric isoforms**: distinct configurations of a nucleus with the same atomic numbers but different spatial layouts and energetic profiles.

Inspired by theoretical biologist **Richard Gordon** and developed in collaboration with **Hussain Ather**, this project explores:
- Structural isoforms of nuclei
- Binding energy estimation via pairwise nucleon interactions
- Visualization and simulation of graph-based nuclear configurations
- Quantum-mechanical integration (future)

---

## ✨ Features

- 🔁 Multiple isoform simulations for light nuclei (e.g. ⁶Li)
- ⚛️ Pairwise energy calculation (P-N, P-P, N-N)
- 📉 Coulomb repulsion modeling
- 📐 Graph + spatial visualizations of 3D tensegrity layouts
- 🔭 Framework for expanding to large nuclei and quantum models

---

## 🧪 Example: Lithium-6 Isoforms

Two isoforms of 6Li are modeled:
- Hexagonal prism structure (3 protons + 3 neutrons on stacked triangles)
- Linear chain configuration

Each isoform has different binding energy and spatial tension—hypothesized to correspond to observable or short-lived nuclear variants.

---

## 🔧 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/HussainAther/nucleus-tensegrity.git
cd nucleus-tensegrity
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the model

```bash
python tensegrity_model.py
```

---

## 📂 Project Structure

```
.
├── tensegrity_model.py        # Core simulation + visualization
├── requirements.txt           # Python dependencies
├── notebooks/                 # (Coming soon) Jupyter explorations
├── data/                      # Sample configurations or templates
└── results/                   # Energy logs, outputs, etc.
```

---

## 🔮 Next Steps

* Extend to other isotopes (e.g., ⁴He, ¹⁶O, ²⁸O)
* Parameter tuning from experimental data
* Implement quantum corrections (tunneling, superposition)
* Develop web app visualizer or Jupyter dashboard
* Prepare for arXiv or bioRxiv preprint

---

## 📜 License

MIT License — open for scientific collaboration and research.

---

## 👥 Contributors

* **Hussain Ather** — [@HussainAther](https://github.com/HussainAther)
* **Richard Gordon** — Gulf Specimen Marine Laboratory

Special thanks to the broader RBYRCT and OREL communities for support and inspiration.

---

## 📫 Contact & Collaboration

Interested in contributing, testing, or building on this model?
Feel free to open an issue, fork the repo, or reach out via GitHub.

Let’s rethink nuclear physics, one structure at a time.

