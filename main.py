from factory import Instr_Factory
from utils import separate, trans
import argparse

'''
input: file_path
mode: STD | FILE
'''
def main(mode: str, infile_path: str, outfile_path=None):
    assert not (mode == "FILE" and outfile_path is None)

    fin = open(infile_path)
    lines = fin.readlines()
    lines = [int(line.strip('\n'), 16) for line in lines]

    if mode == "FILE":
        fout = open(outfile_path, "w", encoding="utf-8")

    sepa_lst = [separate(line) for line in lines]
    trans_lst = [trans(line) for line in sepa_lst]
    instr_txt_lst = []
    for line in trans_lst:
        instr = line[0]
        instr_fact = Instr_Factory(
            instr["instr"], instr["OP"], instr["Rs"],
            instr["Rt"], instr["Rd"], instr["SA"], instr["FUNCT"]
        )
        instr_txt_lst.append(instr_fact.instr_txt)

    if mode == "FILE":
        # add '\n'
        instr_txt_lst = [instr_txt+'\n' for instr_txt in instr_txt_lst]
        fout.writelines(instr_txt_lst)
    elif mode == "STD":
        for instr_txt in instr_txt_lst:
            print(instr_txt)
    else:
        pass

parser = argparse.ArgumentParser()

choices = [
    { "method": "-d", "vmethod": "--dsasmb", "help": "disassemble *.txt" },
    { "method": "-o", "vmethod": "--output", "help": "output to *.txt" }
]

for choice in choices:
    parser.add_argument(
        choice["method"], choice["vmethod"], type=str,
        help=choice["help"]
    )

args = parser.parse_args()

if __name__ == "__main__":
    infile_path = args.dsasmb
    outfile_path = args.output

    assert infile_path is not None

    if outfile_path is None:
        main("STD", infile_path)
    else:
        main("FILE", infile_path, outfile_path)