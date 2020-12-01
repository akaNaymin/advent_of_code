import re
from typing import NamedTuple

class Material(NamedTuple):
    count: int
    name: str


def read_reactions(text):
    rows = text.split('\n')
    reactions = {}
    mat = re.compile(r'(\d+) (\w+)')
    for row in rows:
        matches = re.findall(mat, row)
        components = []
        for count, name in matches:
            components.append(Material(int(count), name))
        reactions[components[-1]] = components[:-1]
    return reactions

def make_material(read_reactions, product, ingredients):
    for req in read_reactions[product]:


# with open('input/day14.txt', 'r') as f:
#     text = f.read()

text = '''10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL'''

res = read_reactions(text)
print(res)