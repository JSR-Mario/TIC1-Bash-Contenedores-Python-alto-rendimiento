#!/usr/bin/env python 
import argparse

# Create CLI interface
parser= argparse.ArgumentParser(
    prog="quintile.py",
    description="Calculate either quintiles or deciles for a given csv dataset",
    epilog="Created by: TICs + Sudo + JSR-Mario in 2025"
)

parser.add_argument(
    "year", 
    help="Year for which quintiles will be calculated", 
    type=int
)
parser.add_argument(
    "-d", "--decile",
    help="Calculate deciles",
    action="store_true"
)
args= parser.parse_args() 

if args.decile:
    print("Will calculate deciles")