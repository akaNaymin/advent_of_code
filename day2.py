

test1 = [1,0,0,0,99]
test2 = [1,1,1,4,99,5,6,0,99]
test3 = [2,4,4,5,99,0]
test4 = [1,1,1,4,99,5,6,0,99]

def intcode(arr):
    for i in range(0, len(arr), 4):
        opcode = arr[i]
        if opcode == 99:
            return arr
        elif opcode == 1:
            prod = arr[arr[i+1]] + arr[arr[i+2]]
        elif opcode == 2:
            prod = arr[arr[i+1]] * arr[arr[i+2]]
        else:
            return -1
        arr[arr[i+3]] = prod
    print('hmm')
    
def init_comp(mem, noun, verb):
    mem_adj = mem
    mem_adj[1] = noun
    mem_adj[2] = verb
    run = intcode(mem_adj)
    return run


with open('input/day2.txt') as f:
        inp = f.read().split(',')
        inp = [int(i) for i in inp]


def find_product():
    for noun in range(100):
        for verb in range(100):
            new_in = [i for i in inp]
            res = init_comp(new_in, noun, verb)
            if res != -1:
                if res[0] == 19690720:
                    return noun, verb

print(find_product())