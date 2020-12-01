class IntCode:
    def __init__(self, mem, pointer=0):
        if type(mem) == list:
            self.mem = [i for i in mem]
        if type(mem) == str:
            with open(mem) as f:
                program = f.read().split(',')
            self.mem = [int(i) for i in program]
        self.pointer = pointer
        self.relative_base = 0
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
        elif opcode in [3, 4, 9]:
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

    def increase_mem(self, new_size):
        # new_mem = [self.mem[i] if i < len(self.mem) else 0 for i in range(new_max)]
        new_mem = [0 for i in range(new_size + 1 - len(self.mem))]
        self.mem = self.mem + new_mem

    def fetch_args(self, modes, w_param):
        args = []
        address = self.mem[self.pointer+1:self.pointer+len(modes)+1]
        for val, mode in zip(address, modes):
            if mode == 0:
                if val >= len(self.mem):
                    self.increase_mem(val)
                args.append(self.mem[val])
            elif mode == 1:
                args.append(val)
            elif mode == 2:
                if self.relative_base + val >= len(self.mem):
                    self.increase_mem(self.relative_base + val)
                args.append(self.mem[self.relative_base + val])
            else:
              raise Exception  
        if w_param:
            if mode == 0:
                args[-1] = address[-1]
            elif mode == 2:
                args[-1] = self.relative_base + address[-1]
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
        elif opcode == 9:
            self.relative_base += args[0]
        else:
            raise Exception
        if not freeze_pointer:
            self.pointer += len(args) + 1
        return opcode, out

    def run(self, return_codes=[]):
        while True:
            opcode, modes, w_param = self.parse_inst(self.mem[self.pointer])
            args = self.fetch_args(modes, w_param)
            op_return, op_out = self.excecute_op(opcode, args)
            if op_return in [99] + return_codes:
                return (op_return, op_out)
    
    def step(self):
        opcode, modes, w_param = self.parse_inst(self.mem[self.pointer])
        args = self.fetch_args(modes, w_param)
        op_return, op_out = self.excecute_op(opcode, args)
        return (op_return, op_out)  
