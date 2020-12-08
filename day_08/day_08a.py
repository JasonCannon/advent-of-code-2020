import sys
from copy import deepcopy

class Instruction:
    def __init__(self, op, params):
        self.op = op
        self.params = params

    def __repr__(self):
        return f"(I) op = {self.op}, params = {self.params}"

    def __str__(self):
        return f"(Instruction) op = {self.op}, params = {self.params}"

class Code:
    def __init__(self, filename):
        self.__tape = []
        with open(filename, 'r') as file:
            for line in map(lambda x : x.strip(), file.readlines()):
                In = line.split()
                self.__tape.append(Instruction(op = In[0], params = In[1:]))
        self.tape_len = len(self.__tape)

        self.reset()

    def reset(self):
        self.L = deepcopy(self.__tape)
        self.i = 0
        self.accumlator = 0

    def get_curr_instruct(self):
        return self.L[self.i]

    def set_instruct_pointer(self, idx, rel = False):
        self.i = (self.i + idx) if rel else idx

    def inc_instruct_pointer(self):
        self.set_instruct_pointer(1, rel = True)

    def step(self):
        # Get the instruction type.
        I = self.get_curr_instruct()
        curr_op, curr_params = I.op, I.params
        # Find corresponding instruction.
        if curr_op == 'acc':
            p1 = curr_params[0]
            self.accumlator += int(p1)
            self.inc_instruct_pointer()

        elif curr_op == 'jmp':
            self.set_instruct_pointer(int(curr_params[0]), rel = True)

        elif curr_op == 'nop':
            self.inc_instruct_pointer()

        else:
            print(f"{I} | is not a valid instruction.")
            sys.exit(1)

        return 0 <= self.i < len(self.L)

C = Code("day_08.in")
S = set()

while C.i not in S:
    S.add(C.i)
    C.step()

print(C.accumlator)
