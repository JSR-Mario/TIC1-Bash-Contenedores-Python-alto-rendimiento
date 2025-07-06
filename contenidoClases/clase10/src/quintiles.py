#!/usr/bin/env python 
import argparse
import pandas as pd

# Create CLI interface
parser= argparse.ArgumentParser(
    prog="quintile.py",
    description="Calculate either quintiles or deciles for a given csv dataset",
    epilog="Created by: TICs + Sudo + JSR-Mario in 2025"
)

# Adding arguments to the parser
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
parser.add_argument(
    "-D", "--data",
    help="Path to data",
    default="../data/clean/pob_mitad_clean.csv"
)
args= parser.parse_args() 


# Reading Data  
# TODO: entidad as CLI args.entidad

df = pd.read_csv(args.data)
year=args.year
entidad='República Mexicana'

# Processing: 
## We start by obtaining the population given a year and a entity   
total = df.loc[(df['AÑO']==year) & (df['ENTIDAD']==entidad), 'POBLACION'].sum()

# Quintiles: add the quintiles in 5 year groups. 
# Tails (0 and 100+) years follow different rules
## TODO: Segregate by gender
qt=[]

qt.append(df.loc[(df['AÑO']==year) & (df['ENTIDAD']==entidad) & (df['EDAD']==0), 'POBLACION'].sum())

for i in range(19):
    qt.append(df.loc[(df['AÑO']==year)
                    & (df['ENTIDAD']==entidad)
                    & (df['EDAD']>=5*i+1)
                    & (df['EDAD']<=5*i+5),
                    'POBLACION'].sum())

qt.append(df.loc[(df['AÑO']==year) & (df['ENTIDAD']==entidad) & (100<df['EDAD']), 'POBLACION'].sum())


# Results: 
## If deciles print option
## TODO: change calculation type
if args.decile:
    print("Will calculate deciles")

## Result of population
print(f"MX total population in the year {year} is {total}")

for e in qt:
    print(int(e))