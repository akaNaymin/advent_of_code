

def intcode(mem):
    p = 0
    while True:
        # Parse instructions
        inst = mem[p]
        n_params = 0
        opcode = inst % 100
        if opcode in [1, 2, 7, 8]:
            n_params = 3
        elif opcode in [3, 4]:
            n_params = 1
        elif opcode in [5, 6]:
            n_params = 2
        inst //= 100
        param_mode = []
        for i in range(n_params):
            param_mode.append(inst % 10)
            inst //= 10
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
            return mem
        elif opcode == 1:
            mem[args[-1]] = params[0] + params[1]
        elif opcode == 2:
            mem[args[-1]] = params[0] * params[1]
        elif opcode == 3:
            cur_in = int(input('opcode 3:'))
            mem[args[-1]] = cur_in
        elif opcode == 4:
            print(params[0])
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
            return -1
        if not freeze_pointer:
            p += n_params + 1

# print(intcode([1101,100,-1,4,0]))
with open('day5.input') as f:
    program = f.read().split(',')
    program = [int(i) for i in program]

print(intcode(program))

# intcode([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9])