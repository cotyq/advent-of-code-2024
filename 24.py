from collections import deque


values = {}
rules = deque()


with open("input24") as file:
    for line in file:
        if not line.strip():
            break

        name, value = line.strip().split(": ")
        values[name] = bool(value == "1")

    for line in file:
        operation, result = line.strip().split(" -> ")
        op1, symbol, op2 = operation.split()
        rules.append((op1, symbol, op2, result))


while rules:
    op1, symbol, op2, result = rules.popleft()
    if op1 in values and op2 in values:
        if symbol == "XOR":
            r = values[op1] != values[op2]
        elif symbol == "OR":
            r = values[op1] or values[op2]
        else:
            r = values[op1] and values[op2]
        values[result] = r
    else:
        rules.append((op1, symbol, op2, result))


bits = sorted([(k, v) for k, v in values.items() if k.startswith("z")], reverse=True)
n = 0
for b in bits:
    n = n << 1
    if b[1]:
        n += 1

print(n)
