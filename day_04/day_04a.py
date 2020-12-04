import sys

Fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

def present(P):
    return all(f in P for f in Fields)

L = [line.strip() for line in sys.stdin]
Passports = [dict()]

for line in L:
    if line:
        for w in line.split():
            k, v = w.split(':')
            Passports[-1][k] = v
    else: Passports.append(dict())

print(sum([present(P) for P in Passports]))

# def validate(A):
#     if not 1920 <= int(A["byr"]) <= 2002: return False
#     if not 2010 <= int(A["iyr"]) <= 2020: return False
#     if not 2020 <= int(A["eyr"]) <= 2030: return False
#     if A["hgt"].endswith("cm"):
#         if not 150 <= int(A["hgt"][:-2]) <= 193: return False
#     elif A["hgt"].endswith("in"):
#         if not 59 <= int(A["hgt"][:-2]) <= 76: return False
#     else: return False
#     if (A["hcl"][0] == '#' and len(A["hcl"]) == 7 and len(set(A["hcl"][1::]) - set("0123456789abcdef")) == 0):
#         pass
#     else: return False
#     if not A["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}: return False
#     if not (len(A["pid"]) == 9 and len(set(A["pid"]) - set("0123456789")) == 0): return False
#     return True


# def part_a(L):
#     S = {'eyr', 'byr', 'hcl', 'pid', 'iyr', 'ecl', 'hgt'}
#     valid = 0
#     A = dict()
#     F = set()
#     for line in I:
#         if line != '':
#             for w in line.split():
#                 k, v = w.split(':')
#                 A[k] = v
#             continue
#         print(A)
#         flag = False
#         for s in S:
#             if s not in A.keys():
#                 flag = True
#         if flag == False:
#             if not validate(A):
#                 flag = True
#         if not flag:
#             valid += 1
#         A = dict()
#     return valid


# if __name__ == "__main__":
#     print(part_a())