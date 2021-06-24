import pandas as pd
import argparse


# bom = "D:/Tillo/Documents/Projects/hardware/safematic/CCU-010/CCU_Glimmprint/Project Outputs for CCU_Glimmprint/Rev03/Assembly Default/BOM/5000039_03_Glimmprint-BM.xls"
# pp = "D:/Tillo/Documents/Projects/hardware/safematic/CCU-010/CCU_Glimmprint/Project Outputs for CCU_Glimmprint/Rev03/Assembly Default/5000039_03_Glimmprint-PP/5000039_03_Glimmprint.csv"

parser = argparse.ArgumentParser()

parser.add_argument('--bom', '-b', type=str, help="Path to BOM")
parser.add_argument('--pp', '-p', type=str, help="Path to PP")

args = parser.parse_args()

bom = pd.read_excel(args.bom, sheet_name="B-Stückliste", skiprows=range(0, 20))
debom = bom[["Designator", "Comment"]]
boms = set()
for i in range(len(debom["Designator"])):
    val = debom["Comment"][i]
    for p in debom["Designator"][i].split(","):
        boms.add(p.strip()+":"+val)

pp = pd.read_csv(args.pp, skiprows=range(0, 12))
depp = pp[["Designator", "Comment"]]
pps = set()
for i in range(len(depp["Designator"])):
    val = depp["Comment"][i]
    key = depp["Designator"][i]
    pps.add(key+":"+val)

not_in_bom = pps.difference(boms)
not_in_pp = boms.difference(pps)

print("Not in PP:", "\t", sorted(not_in_pp))
print("Not in BOM", "\t", sorted(not_in_bom))
