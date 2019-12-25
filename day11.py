from intcode import IntCode
import numpy as np

'''
        0
    3       1
        2

'''
DIRS = {0: [0, -1],
        1: [1, 0],
        2: [0, 1],
        3: [-1, 0]}

class PaintingBot:

    def __init__(self, code, start=0):
        self.brain = IntCode(code)
        # size = self.estimate_size(code)
        size = 1000
        self.pos = np.array([size, size])
        self.canvas = np.ones((size*2, size*2)) * -1
        self.dir = 0
        self.brain.input.append(start)
    
    
    def move(self, color, turn):
        self.canvas[self.pos[0], self.pos[1]] = color
        if turn == 0:
            self.dir -= 1
        else:
            self.dir += 1
        self.dir = self.dir % 4
        self.pos += DIRS[self.dir]
        col = self.canvas[self.pos[0], self.pos[1]]
        if col == -1:
            col = 0
        self.brain.input.append(col)

    def start(self):
        counter = 0
        opcode = -1
        while opcode != 99:
            opcode, output = self.brain.run([4])
            counter += 1
            if counter == 2:
                outs = self.brain.output[-2:]
                self.move(outs[0], outs[1])
                counter = 0

bot = PaintingBot('input/day11.txt')
bot.start()

print((bot.canvas != -1).sum())

bot2 = PaintingBot('input/day11.txt', start=1)
bot2.start()

def view_canvas(arr):
    coords = np.where(arr != -1)
    # print(coords)
    x, y = coords
    res = arr[x.min():x.max()+1, y.min(): y.max()+1]
    for row in res:
        img = [' ' if tile in [-1, 0] else 'X' for tile in row]
        print(''.join(img))

view_canvas(bot2.canvas)
