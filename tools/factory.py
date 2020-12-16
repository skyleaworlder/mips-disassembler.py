from .utils import hexCat
class Instr_Factory:

    def __init__(
        self, instr: str, OP: int, Rs: int,
        Rt: int, Rd: int, SA: int, FUNCT: int
    ):
        self.instr = instr
        self.OP = OP
        self.Rs = Rs
        self.Rt = Rt
        self.Rd = Rd
        self.SA = SA
        self.FUNCT = FUNCT
        self.__instr_format_calcu(self.instr)

    def __instr_format_calcu(self, instr: str):
        op_instridx =           ["j", "jal"]
        op_rt_rs_immed =        ["beq", "bne"]
        op_rs_rt_immed =        [
                                    "addi", "addiu",
                                    "slti", "sltiu", "andi", "ori", "xori", "clz",
                                    "lb", "lh", "lw", "lbu", "lhu", "sb", "sh", "sw"
                                ]
        op_00_rt_immed =        ["lui"]
        op_rs_rt_rd_00_funct =  ["mul"]

        # only op and funct can figure out instr type
        # but for more details here
        spe_rs_rt_rd_00_funct = [
                                    "sllv", "srlv", "srav", "add", "addu", "sub",
                                    "subu", "and", "or", "xor", "nor", "slt", "sltu"
                                ]
        spe_00_rt_rd_sa_funct = ["sll", "srl", "sra"]
        spe_rs_rt_00_00_funct = ["mult", "multu", "div", "divu"]
        spe_code_funct =        ["syscall", "break"]
        spe_rs_rt_code_funct =  ["teq"]
        spe_rs_00_rd_00_funct = ["jalr"]
        spe_00_00_rd_00_funct = ["mfhi", "mflo"]
        spe_rs_00_00_00_funct = ["jr", "mthi", "mtlo"]

        regimm_rs_rt_offset =   ["bgez"]
        cop0_mtf_rt_fs_0_0 =    ["mfc0", "mtc0"]

        all_need =              ["eret"]

        instr_type_prcs_set = [
            {"set": op_instridx,            "prcs": self.__op_instridx_prcs},
            {"set": op_rt_rs_immed,         "prcs": self.__op_rt_rs_immed_prcs},
            {"set": op_rs_rt_immed,         "prcs": self.__op_rs_rt_immed_prcs},
            {"set": op_00_rt_immed,         "prcs": self.__op_00_rt_immed_prcs},
            {"set": op_rs_rt_rd_00_funct,   "prcs": self.__op_rs_rt_rd_00_funct_prcs},
            {"set": spe_rs_rt_rd_00_funct,  "prcs": self.__spe_rs_rt_rd_00_funct_prcs},
            {"set": spe_00_rt_rd_sa_funct,  "prcs": self.__spe_00_rt_rd_sa_funct_prcs},
            {"set": spe_rs_rt_00_00_funct,  "prcs": self.__spe_rs_rt_00_00_funct_prcs},
            {"set": spe_code_funct,         "prcs": self.__spe_code_funct_prcs},
            {"set": spe_rs_rt_code_funct,   "prcs": self.__spe_rs_rt_code_funct_prcs},
            {"set": spe_rs_00_rd_00_funct,  "prcs": self.__spe_rs_00_rd_00_funct_prcs},
            {"set": spe_00_00_rd_00_funct,  "prcs": self.__spe_00_00_rd_00_funct_prcs},
            {"set": spe_rs_00_00_00_funct,  "prcs": self.__spe_rs_00_00_00_funct_prcs},
            {"set": regimm_rs_rt_offset,    "prcs": self.__regimm_rs_rt_offset_prcs},
            {"set": cop0_mtf_rt_fs_0_0,     "prcs": self.__cop0_mtf_rt_fs_0_0_prcs},
            {"set": all_need,               "prcs": self.__all_need_prcs}
        ]

        for instr_type_prcs in instr_type_prcs_set:
            if self.instr in instr_type_prcs["set"]:
                self.instr_txt = instr_type_prcs["prcs"]()
                break
        else:
            raise Exception("Instruction Parse Failed!", self.instr, self.OP, self.FUNCT)

    # j and jal
    def __op_instridx_prcs(self) -> str:
        # j and jal need << 2 additionally
        target = hexCat(
            {"val": self.Rs, "len": 5},     {"val": self.Rt, "len": 5},
            {"val": self.Rd, "len": 5},     {"val": self.SA, "len": 5},
            {"val": self.FUNCT, "len": 6},  {"val": 0b00, "len": 2}
        )
        return self.instr+" "+target

    # beq and bne
    def __op_rt_rs_immed_prcs(self) -> str:
        immed = immed = hexCat(
            {"val": self.Rd, "len": 5},     {"val": self.SA, "len": 5},
            {"val": self.FUNCT, "len": 6}
        )
        return self.instr+" "+("$"+str(self.Rs))+", "+("$"+str(self.Rt))+", "+(immed)

    # addi addiu slti sltiu andi ori xori lb lh lw lbu lhu sb sh sw
    def __op_rs_rt_immed_prcs(self) -> str:
        immed = hexCat(
        {"val": self.Rd, "len": 5},         {"val": self.SA, "len": 5},
            {"val": self.FUNCT, "len": 6}
        )
        return self.instr+" "+("$"+str(self.Rt))+", "+("$"+str(self.Rs))+", "+(immed)

    # lui
    def __op_00_rt_immed_prcs(self) -> str:
        assert self.Rs == 0
        immed = hexCat(
            {"val": self.Rd, "len": 5},     {"val": self.SA, "len": 5},
            {"val": self.FUNCT, "len": 6}
        )
        return self.instr+" "+("$"+str(self.Rt))+", "+(immed)

    # mul
    def __op_rs_rt_rd_00_funct_prcs(self) -> str:
        assert self.SA == 0
        return self.instr+" "+("$"+str(self.Rd))+", "+("$"+str(self.Rs))+", "+("$"+str(self.Rt))

    # sllv srlv srav add addu sub subu and or xor nor slt sltu
    def __spe_rs_rt_rd_00_funct_prcs(self) -> str:
        assert self.SA == 0 and self.OP == 0
        return self.instr+" "+("$"+str(self.Rd))+", "+("$"+str(self.Rs))+", "+("$"+str(self.Rt))

    # sll srl sra
    def __spe_00_rt_rd_sa_funct_prcs(self) -> str:
        assert self.OP == 0 and self.Rs == 0
        return self.instr+" "+("$"+str(self.Rd))+", "+("$"+str(self.Rt))+", "+str(self.SA)

    # mult multu div divu
    def __spe_rs_rt_00_00_funct_prcs(self) -> str:
        assert self.Rd == 0 and self.SA == 0
        return self.instr+" "+("$"+str(self.Rs))+", "+("$"+str(self.Rt))

    # syscall break
    def __spe_code_funct_prcs(self) -> str:
        assert self.OP == 0
        code = hexCat(
            {"val": self.Rs, "len": 5},     {"val": self.Rt, "len": 5},
            {"val": self.Rd, "len": 5},     {"val": self.SA, "len": 5}
        )
        return self.instr

    # teq
    def __spe_rs_rt_code_funct_prcs(self) -> str:
        assert self.OP == 0
        code = hexCat(
            {"val": self.Rd, "len": 5},     {"val": self.SA, "len": 5}
        )
        return self.instr+" "+("$"+str(self.Rs))+", "+("$"+str(self.Rt))

    # jalr
    def __spe_rs_00_rd_00_funct_prcs(self) -> str:
        assert self.OP == 0 and self.Rt == 0 and self.SA == 0
        return self.instr+" "+("$"+str(self.Rd))+", "+("$"+str(self.Rs))

    # mfhi mflo
    def __spe_00_00_rd_00_funct_prcs(self) -> str:
        assert self.OP == 0 and self.Rs == 0 and self.Rt == 0 and self.SA == 0
        return self.instr+" "+("$"+str(self.Rd))

    # jr mthi mtlo
    def __spe_rs_00_00_00_funct_prcs(self) -> str:
        assert self.OP == 0 and self.Rt == 0 and self.Rd == 0 and self.SA == 0
        return self.instr+" "+("$"+str(self.Rs))

    # bgez
    def __regimm_rs_rt_offset_prcs(self) -> str:
        assert self.OP == 0b000001 # REGIMM
        offset = hexCat(
            {"val": self.Rd, "len": 5},     {"val": self.SA, "len": 5},
            {"val": self.FUNCT, "len": 6}
        )
        return self.instr+" "+("$"+str(self.Rs))+", "+(offset)

    # mfc0 mtc0
    def __cop0_mtf_rt_fs_0_0_prcs(self) -> str:
        assert self.OP == 0b010000 and self.Rs == 0 and self.SA == 0
        return self.instr+" "+("$"+str(self.Rt))+", "+str(self.Rd)

    # eret
    def __all_need_prcs(self) -> str:
        return self.instr
