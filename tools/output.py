from math import ceil, log10

class Output:
    def __init__(self, mode):
        '''
        if sb. would like to add output pattern:
            add k-v in mode_func_map
            put your output_method into this class
                && your method param: (self, origin_lines, instr_txt_lst, output_file_path)
        '''
        mode_func_map = {
            "FILE": self.__FILE_output,
            "STD": self.__STD_output
        }
        self.mode = mode
        assert self.mode in mode_func_map
        self.method = mode_func_map[mode]

    def __FILE_output(self, addr_lst, origin_lines, instr_txt_lst, output_file_path):
        '''
        origin_lines:       instructions_input(list) in hex
        output_file_path:   balabala
        '''
        fout = open(output_file_path, "w", encoding="utf-8")
        # add '\n'
        instr_txt_lst = [instr_txt+'\n' for instr_txt in instr_txt_lst]

        # thanks to https://stackoverflow.com/questions/11676864/how-can-i-format-an-integer-to-a-two-digit-hex/11677120
        #       and https://note.nkmk.me/en/python-for-enumerate-zip/
        #       and https://pyformat.info/ (about formats positional arguments)
        instr_num_lg = ceil(log10(len(instr_txt_lst)))
        line_head_len = max(instr_num_lg, len("idx"))
        fout.write(
            "{:{}{}}".format("idx", '>', line_head_len)
            +"    "+"{:{}{}}".format("address", '>', 10)
            +"    "+"{:{}{}}".format("hex code", '>', 10)
            +"    "+"{:{}}".format("mips-assembly", '<')+'\n'
        )
        # add breakline
        fout.write("-"*60+'\n')
        for idx, (addr, origin_hex, instr_txt) in enumerate(zip(addr_lst, origin_lines, instr_txt_lst)):
            fout.write(
                "{:{}{}}".format(idx, '>', line_head_len)
                +"    "+"0x{:08x}".format(int(addr, 16))
                +"    "+"0x{:08x}".format(origin_hex)
                +"    "+instr_txt
            )

    def __STD_output(self, addr_lst, origin_lines, instr_txt_lst, output_file_path=None):
        instr_num_lg = ceil(log10(len(instr_txt_lst)))
        line_head_len = max(instr_num_lg, len("idx"))
        print(
            "{:{}{}}".format("idx", '>', line_head_len)
            +"    "+"{:{}{}}".format("address", '>', 10)
            +"    "+"{:{}{}}".format("hex code", '>', 10)
            +"    "+"{:{}}".format("mips-assembly", '<')+'\n'
        )
        print("-"*60+'\n')
        for idx, (addr, origin_hex, instr_txt) in enumerate(zip(addr_lst, origin_lines, instr_txt_lst)):
            print(
                "{:{}{}}".format(idx, '>', line_head_len)
                +"    "+"0x{:08x}".format(int(addr, 16))
                +"    "+"0x{:08x}".format(origin_hex)
                +"    "+instr_txt)
