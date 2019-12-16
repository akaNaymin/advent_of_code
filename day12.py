from typing import List
Vector = List[int]
import re
from math import gcd

class Moon:
    def __init__(self, pos: Vector):
        self.base = pos
        self.position = pos
        self.velocity = [0, 0, 0]
        self.gravity = [0, 0, 0]
    
    def calc_grav(self, other_moons):
        gravity = self.velocity.copy()
        for moon in other_moons:
            if self == moon:
                pass
            else:
                for axis, val in enumerate(moon.position):
                    if val > self.position[axis]:
                        gravity[axis] += 1
                    elif val < self.position[axis]:
                        gravity[axis] -= 1
        self.gravity = gravity
    
    def apply_grav(self):
        self.velocity = self.gravity
        self.position = [x + y for x, y in zip(self.position, self.velocity)]

    def cur_energy(self):
        potential = sum([abs(x) for x in self.position])
        kintetic = sum([abs(x) for x in self.velocity])
        return potential * kintetic

    def is_loop(self, axis):
        reset = self.position[axis] == self.base[axis] and self.velocity[axis] == 0
        if reset:
            pass
        return reset

def run_round(moons):
    for moon in moons:
        moon.calc_grav(moons)
    for moon in moons:
        moon.apply_grav()

def axis_loop(moons, axis):
    res = all([moon.is_loop(axis) for moon in moons])
    if res:
        y = 1
    return res

moons = []
with open('inputs/day12.input') as f:
    pat = re.compile(r'<x=(-?\d+), y=(-?\d+), z=(-?\d+)>')
    for res in re.finditer(pat, f.read()):
        coord = [int(x) for x in res.groups()]
        obj = Moon(coord)
        moons.append(obj)

axis_iter = [-1, -1, -1]
for i in range(100):
    run_round(moons)
    for axis in range(3):
        if axis_iter[axis] == -1 and axis_loop(moons, axis):
            axis_iter[axis] = i + 1

system_energy = sum([moon.cur_energy() for moon in moons])
print(system_energy)

axis_iter = [231614, 193052, 60424]
print(axis_iter)

gcd_1 = gcd(axis_iter[0], axis_iter[1])
gcd_2 = gcd(axis_iter[1], axis_iter[2])
print(gcd_1, gcd_2)

optimal_iter = [x//min(gcd_1, gcd_2) for x in axis_iter]
print(optimal_iter)
first_iter = optimal_iter[0] * optimal_iter[1] * optimal_iter[2]
print(first_iter)