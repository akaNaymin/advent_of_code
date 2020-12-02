
import re

def sled_rule(first, second, letter, pw):
	letter_count = 0

	for char in pw:
		if char == letter:
			letter_count += 1
	if (letter_count < first) or (letter_count > second):
		return False
	return True

def tobogann_rule(first, second, letter, pw):
	# found a way to put xor in the most reduntant way nice
	if (pw[first-1] == letter) ^ (pw[second-1] == letter):
		return True
	return False


in_file = "./input/day2"
sled_corrupt = 0
tobogann_corrupt = 0

lines = open(in_file).readlines()

for l in lines:
	pat = r"(\d+)-(\d+) (\w): (\w+)"
	match = re.match(pat, l)
	first, second, letter, pw = match.groups()
	first = int(first)
	second = int(second)

	if not sled_rule(first, second, letter, pw.strip()):
		sled_corrupt += 1
	if not tobogann_rule(first, second, letter, pw.strip()):
		tobogann_corrupt += 1

print("Sled pass - {}".format(len(lines) - sled_corrupt))
print("Tobogann pass - {}".format(len(lines) - tobogann_corrupt))

