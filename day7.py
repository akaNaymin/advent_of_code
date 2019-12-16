import itertools

class IntCode:
    def __init__(self, mem, pointer=0):
        self.mem = mem
        self.pointer = pointer
    
    def parse_inst(self, inst):
        n_params = 0
        opcode = inst % 100
        if opcode in [1, 2, 7, 8]:
            n_params = 3
        elif opcode in [3, 4]:
            n_params = 1
        elif opcode in [5, 6]:
            n_params = 2
        else:
            raise Exception
        inst //= 100
        modes = []
        for p in range(n_params):
            modes.append(inst % 10)
            inst //= 10
        return opcode, modes

    def excecute_op(self, opcode, args):
        if opcode == 99:
            return
        elif opcode == 1:
            self.mem[args[2]] = args[0] + args[1]
        elif opcode == 2:
            self.mem[args[2]] = args[0] * args[1]
        elif opcode == 3:
            if len(inputs) > 0:
                cur_in = inputs[0]
                inputs = inputs[1:]
            else:
                cur_in = int(input('opcode 3:'))
            self.mem[self.args[2]] = cur_in
        elif opcode == 4:
            cur_out.append(params[0])
            return (4, p, cur_out)
        elif opcode == 5:
            if args[0] != 0:
                self.pointer = args[1]
                freeze_pointer = True
        elif opcode == 6:
            if args[0] == 0:
                self.poiinter = args[1]
                freeze_pointer = True
        elif opcode == 7:
            if args[0] < args[1]:
                self.mem[args[2]] = 1
            else:
                self.mem[args[2]] = 0
        elif opcode == 8:
            if args[0] == args[1]:
                self.mem[args[2]] = 1
            else:
                self.mem[args[2]] = 0
        else:
            raise Exception
        if not freeze_pointer:
            p += n_params + 1

    def run(self):
        while True:
            opcode, modes = self.parse_inst(self.mem[self.pointer])

            op_return = self.excecute_op(opcode, args)

def intcode(mem, p=0, inputs=[]):
    cur_out = []
    while True:

        # Set params
        params = []
        args = mem[p:p+n_params+1]
        for param, mode in zip(args[1:], param_mode):
            if mode == 1:
                params.append(param)
            else:
                params.append(mem[param])
        freeze_pointer = False
        # Commands
        if opcode == 99:
            # return mem
            return (99, p, cur_out)
        elif opcode == 1:
            mem[args[-1]] = params[0] + params[1]
        elif opcode == 2:
            mem[args[-1]] = params[0] * params[1]
        elif opcode == 3:
            if len(inputs) > 0:
                cur_in = inputs[0]
                inputs = inputs[1:]
            else:
                cur_in = int(input('opcode 3:'))
            mem[args[-1]] = cur_in
        elif opcode == 4:
            cur_out.append(params[0])
            return (4, p, cur_out)
            # print(cur_out)
        elif opcode == 5:
            if params[0] != 0:
                p = params[1]
                freeze_pointer = True
        elif opcode == 6:
            if params[0] == 0:
                p = params[1]
                freeze_pointer = True
        elif opcode == 7:
            if params[0] < params[1]:
                mem[args[-1]] = 1
            else:
                mem[args[-1]] = 0
        elif opcode == 8:
            if params[0] == params[1]:
                mem[args[-1]] = 1
            else:
                mem[args[-1]] = 0
        else:
            return (-1) * 3
        if not freeze_pointer:
            p += n_params + 1



def thrusters_max(software, t_min=0, t_max=4):
    max_perm = 0
    max_out = 0
    for phase_perm in itertools.permutations(range(t_min, t_max+1)):
        inp = 0
        out_code = -1
        mem = [software for i in phase_perm]
        pointers = [0 for i in phase_perm]
        while out_code != 99:
            for i, phase in enumerate(phase_perm):
                out_code, pointers[i], out_val = intcode(mem[i], p=pointers[i], inputs=[phase, inp])
                inp = out_val
        if inp > max_out:
            max_out = inp
            max_perm = phase
    print(max_out, max_perm)

thrusters_max([3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5], 5,9)

# with open('inputs/day7.input') as f:
#     program = f.read().split(',')
#     program = [int(i) for i in program]
#     thrusters_max(program)