
in_file = "./input/day3"

with open(in_file) as f:
	lines = f.read().splitlines()


def count_trees(lines, right, down):
	pos = 0
	row = 0
	width = len(lines[0])
	count = 0
	while row < len(lines):
		column = pos % width
		if lines[row][column] == '#':
			count += 1
		pos += right
		row += (down)
	return count

# p1
print(count_trees(lines, 3, 1))

# p2
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

mul = 1
for right, down in slopes:
	trees = count_trees(lines, right, down)
	mul *= trees

print(mul)