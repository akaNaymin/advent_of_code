import itertools

class IntCode:
    def __init__(self, mem, pointer=0):
        self.mem = [i for i in mem]
        self.pointer = pointer
        self.input = []
        self.output = []
    
    def __repr__(self):
        return f'IntCode(input={self.input}, out={self.output}, p={self.pointer}), {self.mem})'

    def parse_inst(self, inst):
        n_params = 0
        opcode = inst % 100
        if opcode == 99:
            n_params = 0
        elif opcode in [1, 2, 7, 8]:
            n_params = 3
        elif opcode in [3, 4]:
            n_params = 1
        elif opcode in [5, 6]:
            n_params = 2
        else:
            raise Exception
        write_param = False
        if opcode in [1, 2, 3, 7, 8]:
            write_param = True
        inst //= 100
        modes = []
        for p in range(n_params):
            modes.append(inst % 10)
            inst //= 10
        return opcode, modes, write_param

    def fetch_args(self, modes, w_param):
        args = []
        address = self.mem[self.pointer+1:self.pointer+len(modes)+1]
        for val, mode in zip(address, modes):
            if mode == 1:
                args.append(val)
            else:
                args.append(self.mem[val])
        if w_param:
            args[-1] = address[-1]
        return args

    def excecute_op(self, opcode, args):
        freeze_pointer = False
        out = None
        if opcode == 99:
            pass
        elif opcode == 1:
            self.mem[args[2]] = args[0] + args[1]
        elif opcode == 2:
            self.mem[args[2]] = args[0] * args[1]
        elif opcode == 3:
            if len(self.input) > 0:
                cur_in = self.input[0]
                self.input = self.input[1:]
            else:
                cur_in = int(input('opcode 3:'))
            self.mem[args[0]] = cur_in
        elif opcode == 4:
            self.output.append(args[0])
            out = args[0]
        elif opcode == 5:
            if args[0] != 0:
                self.pointer = args[1]
                freeze_pointer = True
        elif opcode == 6:
            if args[0] == 0:
                self.pointer = args[1]
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
            self.pointer += len(args) + 1
        return opcode, out

    def run(self, return_codes=[99]):
        while True:
            opcode, modes, w_param = self.parse_inst(self.mem[self.pointer])
            args = self.fetch_args(modes, w_param)
            op_return, op_out = self.excecute_op(opcode, args)
            if op_return in return_codes:
                return (op_return, op_out)

def test_run(mem):
    machine = IntCode(mem)
    machine.run()

def chain_max(software):
    max_perm = 0
    max_out = 0
    for phase_perm in itertools.permutations(range(0, 5)):
        amps = [IntCode(software) for i in range(len(phase_perm))]
        next_input = 0
        for amp, phase in zip(amps, phase_perm):
            amp.input.append(phase)
            amp.input.append(next_input)
            op_return, op_out = amp.run(return_codes=[99, 4])
            next_input = op_out
        if op_out > max_out:
            max_out = op_out
            max_perm = phase_perm
    print(max_out, max_perm)


# chain_max([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0])

def chain_loop(software):
    max_perm = 0
    max_out = 0
    for phase_perm in itertools.permutations(range(5, 10)):
        amps = [IntCode(software) for i in range(len(phase_perm))]
        [amp.input.append(phase) for amp, phase in zip(amps, phase_perm)]
        next_input = 0
        op_return = 0
        while op_return != 99:
            for idx, amp in enumerate(amps):
                amp.input.append(next_input)
                op_return, op_out = amp.run(return_codes=[99,4])
                # print(op_return, op_out)
                next_input = op_out
        if amp.output[-1] > max_out:
            max_out = amp.output[-1]
            max_perm = phase_perm
    print(max_out, max_perm)


with open('input/day7.txt') as f:
    program = f.read().split(',')
    program = [int(i) for i in program]
    chain_loop(program)