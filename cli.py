# nucleus_tensegrity/cli.py

import argparse
from .tensegrity_model import run_isoforms

def main():
    parser = argparse.ArgumentParser(description="Run Tensegrity Nucleus Isoform Simulations")
    parser.add_argument("command", choices=["run"], help="Command to execute (e.g., run)")
    args = parser.parse_args()

    if args.command == "run":
        run_isoforms()

