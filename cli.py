# nucleus_tensegrity/cli.py

import argparse
from .tensegrity_model import run_isoforms

def main():
    parser = argparse.ArgumentParser(description="Run Tensegrity Nucleus Isoform Simulations")
    parser.add_argument("command", choices=["run"], help="Command to execute")
    parser.add_argument("--no-plot", action="store_true", help="Disable 3D visualizations")
    parser.add_argument("--save-results", action="store_true", help="Save results to results/energies.csv")
    args = parser.parse_args()

    if args.command == "run":
        run_isoforms(plot=not args.no_plot, save_results=args.save_results)

