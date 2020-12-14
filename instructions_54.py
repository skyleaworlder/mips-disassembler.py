# reference: https://www.cs.cmu.edu/afs/cs/academic/class/15740-f97/public/doc/mips-isa.pdf
instr_set = {
    # 21
    "j":        { "OP": 0b000010, "FUNCT": "unlimited" },
    "jal":      { "OP": 0b000011, "FUNCT": "unlimited" },
    "beq":      { "OP": 0b000100, "FUNCT": "unlimited" },
    "bne":      { "OP": 0b000101, "FUNCT": "unlimited" },
    "addi":     { "OP": 0b001000, "FUNCT": "unlimited" },
    "addiu":    { "OP": 0b001001, "FUNCT": "unlimited" },
    "slti":     { "OP": 0b001010, "FUNCT": "unlimited" },
    "sltiu":    { "OP": 0b001011, "FUNCT": "unlimited" },
    "andi":     { "OP": 0b001100, "FUNCT": "unlimited" },
    "ori":      { "OP": 0b001101, "FUNCT": "unlimited" },
    "xori":     { "OP": 0b001110, "FUNCT": "unlimited" },
    "lui":      { "OP": 0b001111, "RS": 0b00000, "FUNCT": "unlimited" },
    "clz":      { "OP": 0b011100, "FUNCT": "unlimited" },
    "lb":       { "OP": 0b100000, "FUNCT": "unlimited" },
    "lh":       { "OP": 0b100001, "FUNCT": "unlimited" },
    "lw":       { "OP": 0b100011, "FUNCT": "unlimited" },
    "lbu":      { "OP": 0b100100, "FUNCT": "unlimited" },
    "lhu":      { "OP": 0b100101, "FUNCT": "unlimited" },
    "sb":       { "OP": 0b101000, "FUNCT": "unlimited" },
    "sh":       { "OP": 0b101001, "FUNCT": "unlimited" },
    "sw":       { "OP": 0b101011, "FUNCT": "unlimited" },

    # 14
    "mul":      { "OP": 0b011100, "SA": 0b00000, "FUNCT": 0b000010 },
    "sllv":     { "OP": 0b000000, "SA": 0b00000, "FUNCT": 0b000100 },
    "srlv":     { "OP": 0b000000, "SA": 0b00000, "FUNCT": 0b000110 },
    "srav":     { "OP": 0b000000, "SA": 0b00000, "FUNCT": 0b000111 },
    "add":      { "OP": 0b000000, "SA": 0b00000, "FUNCT": 0b100000 },
    "addu":     { "OP": 0b000000, "SA": 0b00000, "FUNCT": 0b100001 },
    "sub":      { "OP": 0b000000, "SA": 0b00000, "FUNCT": 0b100010 },
    "subu":     { "OP": 0b000000, "SA": 0b00000, "FUNCT": 0b100011 },
    "and":      { "OP": 0b000000, "SA": 0b00000, "FUNCT": 0b100100 },
    "or":       { "OP": 0b000000, "SA": 0b00000, "FUNCT": 0b100101 },
    "xor":      { "OP": 0b000000, "SA": 0b00000, "FUNCT": 0b100110 },
    "nor":      { "OP": 0b000000, "SA": 0b00000, "FUNCT": 0b100111 },
    "slt":      { "OP": 0b000000, "SA": 0b00000, "FUNCT": 0b101010 },
    "sltu":     { "OP": 0b000000, "SA": 0b00000, "FUNCT": 0b101011 },

    # 3
    "sll":      { "OP": 0b000000, "RS": 0b00000, "FUNCT": 0b000000 },
    "srl":      { "OP": 0b000000, "RS": 0b00000, "FUNCT": 0b000010 },
    "sra":      { "OP": 0b000000, "RS": 0b00000, "FUNCT": 0b000011 },

    # 4
    "mult":     { "OP": 0b000000, "RD": 0b00000, "SA": 0b00000, "FUNCT": 0b011000 },
    "multu":    { "OP": 0b000000, "RD": 0b00000, "SA": 0b00000, "FUNCT": 0b011001 },
    "div":      { "OP": 0b000000, "RD": 0b00000, "SA": 0b00000, "FUNCT": 0b011010 },
    "divu":     { "OP": 0b000000, "RD": 0b00000, "SA": 0b00000, "FUNCT": 0b011011 },

    # 3
    "syscall":  { "OP": 0b000000, "FUNCT": 0b001100 },
    "break":    { "OP": 0b000000, "FUNCT": 0b001101 }, # SPECIAL code BREAK | BREAK
    "teq":      { "OP": 0b000000, "FUNCT": 0b110100 },

    # 3
    "bgez":     { "OP": 0b000001, "RT": 0b00001, "FUNCT": "unlimited" }, # REGIMM rs BGEZ offset | BGEZ rs, offset
    "jr":       { "OP": 0b000000, "RT": 0b00000, "RD": 0b00000, "SA": 0b00000, "FUNCT": 0b001000 },
    "jalr":     { "OP": 0b000000, "RT": 0b00000, "SA": 0b00000, "FUNCT": 0b001001 }, # SPECIAL rs 0 rd 0 JALR | JALR rs (rd = 31 implied) | JALR rd, rs

    # 7
    "mfc0":     { "OP": 0b010000, "RS": 0b00000, "SA": 0b00000, "FUNCT": 0b000000 },
    "mtc0":     { "OP": 0b010000, "RS": 0b00100, "SA": 0b00000, "FUNCT": 0b000000 },
    "mfhi":     { "OP": 0b000000, "RS": 0b00000, "RT": 0b00000, "SA": 0b00000, "FUNCT": 0b010000 },
    "mflo":     { "OP": 0b000000, "RS": 0b00000, "RT": 0b00000, "SA": 0b00000, "FUNCT": 0b010010 },
    "mthi":     { "OP": 0b000000, "RT": 0b00000, "RD": 0b00000, "SA": 0b00000, "FUNCT": 0b010001 },
    "mtlo":     { "OP": 0b000000, "RT": 0b00000, "RD": 0b00000, "SA": 0b00000, "FUNCT": 0b010011 },

    # 1
    "eret":     { "OP": 0b100000, "RS": 0b10000, "RT": 0b00000, "RD": 0b00000, "SA": 0b00000, "FUNCT": 0b011000 },
}

