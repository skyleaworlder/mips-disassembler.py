from tools.factory import Instr_Factory
from tools.utils import separate, trans
from tools.output import Output
import argparse
from math import log10, ceil

def main(mode: str, infile_path: str, outfile_path=None):
    '''
    input: file_path
    mode: STD | FILE
    '''
    assert not (mode == "FILE" and outfile_path is None)

    fin = open(infile_path)
    origin_lines = fin.readlines()
    origin_lines = [int(line.strip('\n'), 16) for line in origin_lines]

    # get instruction type
    sepa_lst = [separate(line) for line in origin_lines]
    trans_lst = [trans(line) for line in sepa_lst]
    instr_txt_lst = []

    # process instructions input
    for line in trans_lst:
        instr = line[0]
        instr_fact = Instr_Factory(
            instr["instr"], instr["OP"], instr["Rs"],
            instr["Rt"], instr["Rd"], instr["SA"], instr["FUNCT"]
        )
        instr_txt_lst.append(instr_fact.instr_txt)

    # output result
    out = Output(mode)
    out.method(origin_lines, instr_txt_lst, outfile_path)


if __name__ == "__main__":

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

    infile_path = args.dsasmb
    outfile_path = args.output

    assert infile_path is not None
    mode = "STD" if outfile_path is None else "FILE"

    main(mode, infile_path, outfile_path)
