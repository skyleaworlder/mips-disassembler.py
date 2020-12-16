from tools.factory import Instr_Factory
from tools.utils import separate, trans
import argparse
from math import log10, ceil

'''
input: file_path
mode: STD | FILE
'''
def main(mode: str, infile_path: str, outfile_path=None):
    assert not (mode == "FILE" and outfile_path is None)

    fin = open(infile_path)
    origin_lines = fin.readlines()
    origin_lines = [int(line.strip('\n'), 16) for line in origin_lines]

    if mode == "FILE":
        fout = open(outfile_path, "w", encoding="utf-8")

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

    if mode == "FILE":
        # add '\n'
        instr_txt_lst = [instr_txt+'\n' for instr_txt in instr_txt_lst]

        # thanks to https://stackoverflow.com/questions/11676864/how-can-i-format-an-integer-to-a-two-digit-hex/11677120
        #       and https://note.nkmk.me/en/python-for-enumerate-zip/
        #       and https://pyformat.info/ (about formats positional arguments)
        instr_num_lg = ceil(log10(len(instr_txt_lst)))
        line_head_len = max(instr_num_lg, len("idx"))
        fout.write(
            "{:{}{}}".format("idx", '>', line_head_len)+"    "
            +"{:{}{}}".format("hex code", '>', 10)+"    "
            +"{:{}}".format("mips-assembly", '<')+'\n'
        )
        # add breakline
        fout.write("-"*40+'\n')
        for idx, (origin_hex, instr_txt) in enumerate(zip(origin_lines, instr_txt_lst)):
            fout.write("{:{}{}}".format(idx, '>', line_head_len)+"    "+"0x{:08x}".format(origin_hex)+"    "+instr_txt)

    elif mode == "STD":
        for origin_hex, instr_txt in zip(origin_lines, instr_txt_lst):
            print(instr_txt)
    else:
        pass

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

    if outfile_path is None:
        main("STD", infile_path)
    else:
        main("FILE", infile_path, outfile_path)
