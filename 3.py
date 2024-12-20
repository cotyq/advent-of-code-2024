import re

with open("input3") as file:
    linea = "".join(line.strip() for line in file)
    patron = r"don't\(\).*?do\(\)"
    coincidencias = re.findall(patron, linea)
    print(len(coincidencias))
