# reference: https://www.cs.cmu.edu/afs/cs/academic/class/15740-f97/public/doc/mips-isa.pdf
instr_set = {
    # 2
    "j":        { "OP": 0b000010, "FUNCT": "unlimited" }, # J instr_index | J target
    "jal":      { "OP": 0b000011, "FUNCT": "unlimited" }, # JAL instr_index | JAL target

    # 2
    "beq":      { "OP": 0b000100, "FUNCT": "unlimited" }, # BEQ rs rt immed | BEQ rs, rt, offset
    "bne":      { "OP": 0b000101, "FUNCT": "unlimited" }, # BNE rs rt immed | BNE rs, rt, offset

    # 16
    "addi":     { "OP": 0b001000, "FUNCT": "unlimited" }, # OP rs rt immed | OP rt, rs, offset
    "addiu":    { "OP": 0b001001, "FUNCT": "unlimited" }, # OP rs rt immed | OP rt, rs, offset
    "slti":     { "OP": 0b001010, "FUNCT": "unlimited" }, # OP rs rt immed | OP rt, rs, offset
    "sltiu":    { "OP": 0b001011, "FUNCT": "unlimited" }, # OP rs rt immed | OP rt, rs, offset
    "andi":     { "OP": 0b001100, "FUNCT": "unlimited" }, # OP rs rt immed | OP rt, rs, offset
    "ori":      { "OP": 0b001101, "FUNCT": "unlimited" }, # OP rs rt immed | OP rt, rs, offset
    "xori":     { "OP": 0b001110, "FUNCT": "unlimited" }, # OP rs rt immed | OP rt, rs, offset
    "clz":      { "OP": 0b011100, "FUNCT": "unlimited" },
    "lb":       { "OP": 0b100000, "FUNCT": "unlimited" }, # OP rs rt immed | OP rt, offset(rs)
    "lh":       { "OP": 0b100001, "FUNCT": "unlimited" }, # OP rs rt immed | OP rt, offset(rs)
    "lw":       { "OP": 0b100011, "FUNCT": "unlimited" }, # OP rs rt immed | OP rt, offset(rs)
    "lbu":      { "OP": 0b100100, "FUNCT": "unlimited" }, # OP rs rt immed | OP rt, offset(rs)
    "lhu":      { "OP": 0b100101, "FUNCT": "unlimited" }, # OP rs rt immed | OP rt, offset(rs)
    "sb":       { "OP": 0b101000, "FUNCT": "unlimited" }, # OP rs rt immed | OP rt, offset(rs)
    "sh":       { "OP": 0b101001, "FUNCT": "unlimited" }, # OP rs rt immed | OP rt, offset(rs)
    "sw":       { "OP": 0b101011, "FUNCT": "unlimited" }, # OP rs rt immed | OP rt, offset(rs)

    # 1
    "lui":      { "OP": 0b001111, "RS": 0b00000, "FUNCT": "unlimited" }, # LUI 0 rt immed | LUI rt, offset

    # 1
    "mul":      { "OP": 0b011100, "SA": 0b00000, "FUNCT": 0b000010 }, # MUL rs rt rd 0 MUL | MUL rd, rs, rt

    # 13
    "sllv":     { "OP": 0b000000, "SA": 0b00000, "FUNCT": 0b000100 }, # SPECIAL rs rt rd 0 SLLV | SLLV rd, rt, rs
    "srlv":     { "OP": 0b000000, "SA": 0b00000, "FUNCT": 0b000110 }, # SPECIAL rs rt rd 0 SRLV | SRLV rd, rt, rs
    "srav":     { "OP": 0b000000, "SA": 0b00000, "FUNCT": 0b000111 }, # SPECIAL rs rt rd 0 SRAV | SRAV rd, rt, rs
    "add":      { "OP": 0b000000, "SA": 0b00000, "FUNCT": 0b100000 }, # SPECIAL rs rt rd 0 ADD | ADD rd, rs, rt
    "addu":     { "OP": 0b000000, "SA": 0b00000, "FUNCT": 0b100001 }, # SPECIAL rs rt rd 0 ADDU | ADDU rd, rs, rt
    "sub":      { "OP": 0b000000, "SA": 0b00000, "FUNCT": 0b100010 }, # SPECIAL rs rt rd 0 SUB | SUB rd, rs, rt
    "subu":     { "OP": 0b000000, "SA": 0b00000, "FUNCT": 0b100011 }, # SPECIAL rs rt rd 0 SUBU | SUBU rd, rs, rt
    "and":      { "OP": 0b000000, "SA": 0b00000, "FUNCT": 0b100100 }, # SPECIAL rs rt rd 0 AND | AND rd, rs, rt
    "or":       { "OP": 0b000000, "SA": 0b00000, "FUNCT": 0b100101 }, # SPECIAL rs rt rd 0 OR | OR rd, rs, rt
    "xor":      { "OP": 0b000000, "SA": 0b00000, "FUNCT": 0b100110 }, # SPECIAL rs rt rd 0 XOR | XOR rd, rs, rt
    "nor":      { "OP": 0b000000, "SA": 0b00000, "FUNCT": 0b100111 }, # SPECIAL rs rt rd 0 NOR | NOR rd, rs, rt
    "slt":      { "OP": 0b000000, "SA": 0b00000, "FUNCT": 0b101010 }, # SPECIAL rs rt rd 0 SLT | SLT rd, rs, rt
    "sltu":     { "OP": 0b000000, "SA": 0b00000, "FUNCT": 0b101011 }, # SPECIAL rs rt rd 0 SLTU | SLTU rd, rs, rt

    # 3
    "sll":      { "OP": 0b000000, "RS": 0b00000, "FUNCT": 0b000000 }, # SPECIAL 0 rt, rd, sa, SLL | SLL rd, rt, sa
    "srl":      { "OP": 0b000000, "RS": 0b00000, "FUNCT": 0b000010 }, # SPECIAL 0 rt, rd, sa, SRL | SRL rd, rt, sa
    "sra":      { "OP": 0b000000, "RS": 0b00000, "FUNCT": 0b000011 }, # SPECIAL 0 rt, rd, sa, SRA | SRA rd, rt, sa

    # 4
    "mult":     { "OP": 0b000000, "RD": 0b00000, "SA": 0b00000, "FUNCT": 0b011000 }, # SPECIAL rs rt 10{0} MULTU | MULTU rs, rt
    "multu":    { "OP": 0b000000, "RD": 0b00000, "SA": 0b00000, "FUNCT": 0b011001 }, # SPECIAL rs rt 10{0} MULTU | MULTU rs, rt
    "div":      { "OP": 0b000000, "RD": 0b00000, "SA": 0b00000, "FUNCT": 0b011010 }, # SPECIAL rs rt 10{0} DIV | DIV rs, rt
    "divu":     { "OP": 0b000000, "RD": 0b00000, "SA": 0b00000, "FUNCT": 0b011011 }, # SPECIAL rs rt 10{0} DIVU | DIVU rs, rt

    # 2
    "syscall":  { "OP": 0b000000, "FUNCT": 0b001100 }, # SPECIAL code SYSCALL | SYSCALL
    "break":    { "OP": 0b000000, "FUNCT": 0b001101 }, # SPECIAL code BREAK | BREAK

    # 1
    "teq":      { "OP": 0b000000, "FUNCT": 0b110100 }, # SPECIAL rs rt code TEQ | TEQ rs, rt

    # 1
    "jalr":     { "OP": 0b000000, "RT": 0b00000, "SA": 0b00000, "FUNCT": 0b001001 }, # SPECIAL rs 0 rd 0 JALR | JALR rs (rd = 31 implied) | JALR rd, rs

    # 2
    "mfhi":     { "OP": 0b000000, "RS": 0b00000, "RT": 0b00000, "SA": 0b00000, "FUNCT": 0b010000 }, # SPECIAL 10{0} rd 0 MFHI | MFHI rd
    "mflo":     { "OP": 0b000000, "RS": 0b00000, "RT": 0b00000, "SA": 0b00000, "FUNCT": 0b010010 }, # SPECIAL 10{0} rd 0 MFLO | MFLO rd

    # 3
    "jr":       { "OP": 0b000000, "RT": 0b00000, "RD": 0b00000, "SA": 0b00000, "FUNCT": 0b001000 }, # SPECIAL rs 15{0} JR | JR rs
    "mthi":     { "OP": 0b000000, "RT": 0b00000, "RD": 0b00000, "SA": 0b00000, "FUNCT": 0b010001 }, # SPECIAL rs 15{0} MTHI | MTHI rs
    "mtlo":     { "OP": 0b000000, "RT": 0b00000, "RD": 0b00000, "SA": 0b00000, "FUNCT": 0b010011 }, # SPECIAL rs 15{0} MTLO | MTLO rs

    # 2
    "mfc0":     { "OP": 0b010000, "RS": 0b00000, "SA": 0b00000, "FUNCT": 0b000000 }, # COP0 MF rt fs 11{0} | MFC0 rt, fs
    "mtc0":     { "OP": 0b010000, "RS": 0b00100, "SA": 0b00000, "FUNCT": 0b000000 }, # COP0 MT rt fs 11{0} | MTC0 rt, fs

    # 1
    "bgez":     { "OP": 0b000001, "RT": 0b00001, "FUNCT": "unlimited" }, # REGIMM rs rt(BGEZ) offset | BGEZ rs, offset

    # 1
    "eret":     { "OP": 0b100000, "RS": 0b10000, "RT": 0b00000, "RD": 0b00000, "SA": 0b00000, "FUNCT": 0b011000 },
}

