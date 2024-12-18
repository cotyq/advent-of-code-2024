with open("input17") as file:
    register = {
        4: int(file.readline().split()[-1]),
        5: int(file.readline().split()[-1]),
        6: int(file.readline().split()[-1]),
    }
    file.readline()
    program = [int(p) for p in file.readline().split()[-1].split(",")]

i = 0
while i < len(program):
    opcode = program[i]
    operand = program[i + 1]
    combo = register.get(operand, operand)

    if opcode == 0:
        register[4] = register[4] // (1 << combo)
    elif opcode == 1:
        register[5] = register[5] ^ operand
    elif opcode == 2:
        register[5] = combo % 8
    elif opcode == 3:
        if register[4]:
            i = operand - 2
    elif opcode == 4:
        register[5] = register[5] ^ register[6]
    elif opcode == 5:
        print(combo % 8, end=",")
    elif opcode == 6:
        register[5] = register[4] // (1 << combo)
    elif opcode == 7:
        register[6] = register[4] // (1 << combo)
    i += 2

print("\n2,4,1,1,7,5,0,3,1,4,4,0,5,5,3,0")
