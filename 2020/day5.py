

in_file = "./input/day5"

with open(in_file) as f:
	lines = f.read().splitlines()


def seat_partition(string):
	row_r = [0 ,128]
	seat_r = [0, 8]
	for char in string[:7]:
		mid = sum(row_r)//2
		if char == 'F':
			row_r[1] = mid
		else:
			row_r[0] = mid
	for char in string[7:]:
		mid = sum(seat_r)//2
		if char == 'L':
			seat_r[1] = mid
		else:
			seat_r[0] = mid
	
	return (row_r[0]*8 + seat_r[0])

max_id = 0
filled_seats = [False for i in range(1023)]

for line in lines:
	idx = seat_partition(line)
	filled_seats[idx] = True
	if idx > max_id:
		max_id = idx

print(max_id)

for i, full in enumerate(filled_seats):
	if not full:
		if filled_seats[i-1] and filled_seats[i-1]:
			print(i)
			break


