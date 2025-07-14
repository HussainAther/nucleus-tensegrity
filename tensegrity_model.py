# tensegrity_model.py

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from fuzzywuzzy import process
from mpl_toolkits.mplot3d import Axes3D

# Energy constants (arbitrary units)
EPS_PN = -3.0
EPS_NN = -2.0
EPS_PP = -1.5
COULOMB_CONST = 1.0

def calculate_energy(nucleons, bonds):
    energy = 0
    G = nx.Graph()
    for i, j in bonds:
        type_i, pos_i = nucleons[i]
        type_j, pos_j = nucleons[j]
        dist = np.linalg.norm(pos_i - pos_j)
        pair = ''.join(sorted([type_i, type_j]))

        if pair == 'PN':
            energy += EPS_PN
        elif pair == 'NN':
            energy += EPS_NN
        elif pair == 'PP':
            energy += EPS_PP + COULOMB_CONST / dist
        G.add_edge(i, j)

    # Unbonded proton-proton Coulomb repulsion
    protons = [i for i, (t, _) in nucleons.items() if t == 'P']
    for i in range(len(protons)):
        for j in range(i + 1, len(protons)):
            if not G.has_edge(protons[i], protons[j]):
                pos_i = nucleons[protons[i]][1]
                pos_j = nucleons[protons[j]][1]
                dist = np.linalg.norm(pos_i - pos_j)
                energy += COULOMB_CONST / dist

    return energy

def visualize_isoform(nucleons, bonds, title="Isoform"):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    colors = {'P': 'red', 'N': 'blue'}

    for idx, (ptype, pos) in nucleons.items():
        ax.scatter(*pos, c=colors[ptype], label=ptype if idx == 0 else "", s=100)
        ax.text(*pos, f'{ptype}{idx}', fontsize=9)

    for i, j in bonds:
        p1, p2 = nucleons[i][1], nucleons[j][1]
        ax.plot(*zip(p1, p2), color='gray')

    ax.set_title(title)
    ax.set_xlim([-1, 2])
    ax.set_ylim([-1, 2])
    ax.set_zlim([-1, 2])
    plt.legend()
    plt.show()

def run_isoforms():
    isoforms = []

    # Isoform 1: Triangular base with parallel top (hex prism-like)
    nucleons_1 = {
        0: ('P', np.array([0, 0, 0])),
        1: ('P', np.array([1, 0, 0])),
        2: ('P', np.array([0.5, 0.866, 0])),
        3: ('N', np.array([0, 0, 1])),
        4: ('N', np.array([1, 0, 1])),
        5: ('N', np.array([0.5, 0.866, 1]))
    }
    bonds_1 = [(0, 3), (1, 4), (2, 5), (0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3)]
    isoforms.append(("Hex Prism", nucleons_1, bonds_1))

    # Isoform 2: Linear chain
    nucleons_2 = {
        0: ('P', np.array([0, 0, 0])),
        1: ('N', np.array([1, 0, 0])),
        2: ('P', np.array([2, 0, 0])),
        3: ('N', np.array([3, 0, 0])),
        4: ('P', np.array([4, 0, 0])),
        5: ('N', np.array([5, 0, 0]))
    }
    bonds_2 = [(0,1), (1,2), (2,3), (3,4), (4,5)]
    isoforms.append(("Linear Chain", nucleons_2, bonds_2))

    # Evaluate and visualize
    for name, nucleons, bonds in isoforms:
        energy = calculate_energy(nucleons, bonds)
        print(f"{name} Energy: {energy:.2f}")
        visualize_isoform(nucleons, bonds, title=name)
 
    results = []

    for name, nucleons, bonds in isoforms:
        energy = calculate_energy(nucleons, bonds)
        print(f"{name} Energy: {energy:.2f}")
        if plot:
            visualize_isoform(nucleons, bonds, title=name)
        results.append((name, energy))

    if save_results:
        os.makedirs("results", exist_ok=True)
        with open("results/energies.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Isoform", "Energy"])
            writer.writerows(results)
        print("✅ Results saved to results/energies.csv")

from fuzzywuzzy import process

def run_isoforms(plot=True, save_results=False, isoform_name=None):
    isoforms = []

    # --- Define isoforms ---
    isoforms.append(("Hex Prism", {...}, [...]))
    isoforms.append(("Linear Chain", {...}, [...]))
    isoforms.append(("Trigonal Dipyramid", {...}, [...]))  # Example third

    all_names = [name for name, _, _ in isoforms]

    # Fuzzy match if isoform_name is given
    if isoform_name:
        match, score = process.extractOne(isoform_name, all_names)
        if score < 60:
            print(f"❌ No close match found for isoform '{isoform_name}'.")
            print("👉 Available isoforms:", ", ".join(all_names))
            return
        print(f"🔍 Interpreting isoform '{isoform_name}' as '{match}' (score={score})")
        isoforms = [item for item in isoforms if item[0] == match]

    results = []
    for name, nucleons, bonds in isoforms:
        energy = calculate_energy(nucleons, bonds)
        print(f"{name} Energy: {energy:.2f}")
        if plot:
            visualize_isoform(nucleons, bonds, title=name)
        results.append((name, energy))

    if save_results:
        os.makedirs("results", exist_ok=True)
        with open("results/energies.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Isoform", "Energy"])
            writer.writerows(results)
        print("✅ Results saved to results/energies.csv")


if __name__ == "__main__":
    run_isoforms()

