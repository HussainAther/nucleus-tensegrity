def run_isoforms(plot=True, save_results=False, isoform_name=None):
    isoforms = []

    # --- Define isoforms ---
    nucleons_1 = { ... }  # Hex Prism
    bonds_1 = [ ... ]
    isoforms.append(("Hex Prism", nucleons_1, bonds_1))

    nucleons_2 = { ... }  # Linear Chain
    bonds_2 = [ ... ]
    isoforms.append(("Linear Chain", nucleons_2, bonds_2))

    results = []

    for name, nucleons, bonds in isoforms:
        if isoform_name and name.lower() != isoform_name.lower():
            continue

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

