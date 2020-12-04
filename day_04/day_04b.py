import sys
from string import hexdigits, digits

Fields = {  "byr": lambda P : 1920 <= int(P["byr"]) <= 2002, 
            "iyr": lambda P : 2010 <= int(P["iyr"]) <= 2020, 
            "eyr": lambda P : 2020 <= int(P["eyr"]) <= 2030, 
            "hgt": lambda P : 150 <= int('0'+P["hgt"][:-2]) <= 193 if P["hgt"].endswith("cm") else 59 <= int('0'+P["hgt"][:-2]) <= 76, 
            "hcl": lambda P : P["hcl"][0] == '#' and not set(P["hcl"][1:])-set(hexdigits), 
            "ecl": lambda P : P["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}, 
            "pid": lambda P : len(P["pid"]) == 9 and not set(P["pid"]) - set(digits)
        }

def present(P):
    return all(f in P for f in Fields)


def valid(P):
    return all(func(P) for func in Fields.values())

L = [line.strip() for line in sys.stdin]
Passports = [dict()]

for line in L:
    if line:
        for w in line.split():
            k, v = w.split(':')
            Passports[-1][k] = v
    else: Passports.append(dict())

print(sum([present(P) and valid(P) for P in Passports]))
