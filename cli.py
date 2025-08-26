# nucleus_tensegrity/cli.py

import argparse
from .tensegrity_model import run_isoforms, list_isoforms, get_isoform_info, match_isoforms


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


def main():
    parser = argparse.ArgumentParser(prog="nucleus-tensegrity", description="Tensegrity-Based Nucleus Modeling Tool")

    subparsers = parser.add_subparsers(dest="command")

    # `run` command
    run_parser = subparsers.add_parser("run", help="Run a simulation")
    run_parser.add_argument("--no-plot", action="store_true", help="Disable 3D plot visualization")
    run_parser.add_argument("--save-results", action="store_true", help="Save results to CSV")
    run_parser.add_argument("--isoform", type=str, help="Run specific isoforms (fuzzy name match, comma-separated)")

    # `list` command
    list_parser = subparsers.add_parser("list", help="List available isoforms")

    # `info` command
    info_parser = subparsers.add_parser("info", help="Show info about a specific isoform")
    info_parser.add_argument("name", type=str, help="Name of the isoform (fuzzy matched)")

    args = parser.parse_args()

    if args.command == "list":
        list_isoforms()

    elif args.command == "info":
        match = match_isoforms(args.name)
        if match:
            for m in match:
                get_isoform_info(m)
        else:
            print(f"❌ No matches found for '{args.name}'.")

    elif args.command == "run":
        run_isoforms(
            plot=not args.no_plot,
            save_results=args.save_results,
            isoform_name=args.isoform
        )

    else:
        parser.print_help()



