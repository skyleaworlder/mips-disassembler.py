from instructions_54 import instr_set

'''
  OP    RS    RT    RD    SA   FUNCT
000000 00000 00000 00000 00000 000000

separate an Integer into several parts:
    OP, RS, RT, RD, SA, FUNCT

'''
def separate(input: int) -> dict:
    OP_bit, RS_bit, RT_bit, RD_bit, SA_bit, FUNCT_bit = 6, 5, 5, 5, 5, 6
    OP    = (input & 0b11111100000000000000000000000000) >> (RS_bit + RT_bit + RD_bit + SA_bit + FUNCT_bit)
    RS    = (input & 0b00000011111000000000000000000000) >> (RT_bit + RD_bit + SA_bit + FUNCT_bit)
    RT    = (input & 0b00000000000111110000000000000000) >> (RD_bit + SA_bit + FUNCT_bit)
    RD    = (input & 0b00000000000000001111100000000000) >> (SA_bit + FUNCT_bit)
    SA    = (input & 0b00000000000000000000011111000000) >> (FUNCT_bit)
    FUNCT = (input & 0b00000000000000000000000000111111)
    return { "OP": OP, "RS": RS, "RT": RT, "RD": RD, "SA": SA, "FUNCT": FUNCT }

'''
trans an dict { "OP", "RS", "RT", "RD", "SA", "FUNCT" }
to an dict about { "intro", ... }

this function aims to find instruction type of input
'''
def trans(instr_sepa: dict) -> dict:
    OP, FUNCT, SA = instr_sepa["OP"], instr_sepa["FUNCT"], instr_sepa["SA"]
    RS, RT, RD = instr_sepa["RS"], instr_sepa["RT"], instr_sepa["RD"]

    res_instr = []
    for instr in instr_set:
        # OP == 0, FUNCT can figure... such as "sllv", "srlv"...
        # almost all instrs that enjoy the same "OP" 0b000000
        # but clz and mul enjoy the same "OP" 0b011100 instead of 0b000000
        flag1 = (instr_set[instr]["OP"] == OP and OP != 0 and OP != 0b011100)

        # OP and FUNCT must be able to figure out instruction type
        flag2 = (instr_set[instr]["OP"] == OP and instr_set[instr]["FUNCT"] == FUNCT)

        if flag1 or flag2:
            res_instr.append({
                "instr": instr, "Rs": instr_sepa["RS"], "Rt": instr_sepa["RT"],
                "Rd": instr_sepa["RD"], "SA": instr_sepa["SA"], "FUNCT": instr_sepa["FUNCT"]
            })
    else:
        if len(res_instr) != 1:
            raise Exception("Instruction parse failed!", instr_set[instr])

    return res_instr