
in_file = "./input/day1"
entries = {}

lines = open(in_file).readlines()

for l in lines:
	val = int(l)
	# first star
	if entries.get(2020-val):
		print(val * (2020-val))
	# second star
	for k in entries.keys():
		t_sum = k + val
		if entries.get(2020 - t_sum):
			print(val * k * (2020-t_sum))

	entries[val] = True