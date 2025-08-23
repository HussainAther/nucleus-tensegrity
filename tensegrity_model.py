from fuzzywuzzy import process

AVAILABLE_ISOFORMS = [
    ("Hex Prism", {...}, [...]),
    ("Linear Chain", {...}, [...]),
    ("Trigonal Dipyramid", {...}, [...]),
]

def list_isoforms():
    print("📦 Available isoforms:")
    for name, *_ in AVAILABLE_ISOFORMS:
        print(f" - {name}")

def match_isoforms(input_string):
    targets = [name for name, *_ in AVAILABLE_ISOFORMS]
    requested = [s.strip() for s in input_string.split(",")]

    matched = []
    for r in requested:
        best, score = process.extractOne(r, targets)
        if score >= 60:
            matched.append(best)
        else:
            print(f"⚠️ No good match for '{r}' (score={score})")
    return matched

def run_isoforms(plot=True, save_results=False, isoform_name=None):
    isoforms = AVAILABLE_ISOFORMS
    results = []

    if isoform_name:
        matched_names = match_isoforms(isoform_name)
        if not matched_names:
            print("❌ No isoform matches found.")
            return
        isoforms = [x for x in AVAILABLE_ISOFORMS if x[0] in matched_names]

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

