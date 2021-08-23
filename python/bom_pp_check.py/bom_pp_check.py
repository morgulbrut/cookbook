import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import argparse
from colorama import Fore, init
from pprint import pprint

# bom = "D:/Tillo/Documents/Projects/hardware/safematic/CCU-010/CCU_Glimmprint/Project Outputs for CCU_Glimmprint/Rev03/Assembly Default/BOM/5000039_03_Glimmprint-BM.xls"
# pp = "D:/Tillo/Documents/Projects/hardware/safematic/CCU-010/CCU_Glimmprint/Project Outputs for CCU_Glimmprint/Rev03/Assembly Default/5000039_03_Glimmprint-PP/5000039_03_Glimmprint.csv"

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--bom', '-b', type=str, help="Path to BOM")
    parser.add_argument('--pp', '-p', type=str, help="Path to PP")

    args = parser.parse_args()

    bom = pd.read_excel(args.bom, sheet_name="B-Stückliste",
                        skiprows=range(0, 20))
    debom = bom[["Designator", "Comment"]]
    boms = set()
    for i in range(len(debom["Designator"])):
        val = debom["Comment"][i]
        for p in debom["Designator"][i].split(","):
            boms.add(p.strip()+":"+str(val))

    # set file_encoding to the file encoding (utf8, latin1, etc.)
    with open(args.pp, encoding='utf8', errors='replace') as input_fd:
        # with open(args.pp, encoding=file_encoding, errors='backslashreplace') as input_fd:
        pp = pd.read_csv(input_fd, skiprows=range(0, 12))

    depp = pp[["Designator", "Comment"]]
    pps = set()
    for i in range(len(depp["Designator"])):
        val = depp["Comment"][i]
        key = depp["Designator"][i]
        pps.add(key+":"+str(val))

    not_in_bom = pps.difference(boms)
    not_in_pp = boms.difference(pps)

    init(autoreset=True)
    print(Fore.YELLOW+"Not in PP:")
    pprint(sorted(not_in_pp))
    print(Fore.YELLOW+"Not in BOM")
    pprint(sorted(not_in_bom))
