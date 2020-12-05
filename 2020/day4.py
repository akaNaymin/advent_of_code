
import re

in_file = "./input/day4"

with open(in_file) as f:
	f_content = f.read()


FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
PATTERNS = [r'(\d{4})', r'(\d{4})', r'(\d{4})', r'(\d+)(cm|in)\b',
			r'#[0-9a-f]{6}', r'(?:amb|blu|brn|gry|grn|hzl|oth)', r'\b[0-9]{9}\b']
field_dict = dict(zip(FIELDS, PATTERNS))

passports = [w for w in f_content.split('\n\n')]

def check_pass(passport, validation=False):
	count = 1
	found = {}
	for match in re.finditer(r'(\w{3}):(\S*)', passport):
		field, content = match.groups()
		if field != 'cid':
			value = content
			if validation:
				value = data_check(field, content)
				found[field] = (value, content)
			if value:
				count += 1

	if count < len(FIELDS):
		return False
	return True

def data_check(f, content):
	res = re.match(field_dict[f], content)
	if not res:
		return False
	if f == 'byr':
		val = int(res.group())
		return val in range(1920, 2003) 
	if f == 'iyr':
		val = int(res.group())
		return val in range(2010, 2021)
	if f == 'eyr':
		val = int(res.group())
		return val in range(2020, 2031)
	if f == 'hgt':
		height, units = res.groups()
		height = int(height)
		if units == 'cm':
			return height in range(150, 194)
		elif units == 'in':
			return height in range(59, 77)
	return True
				
print_list = []
count = 0
idx = 0
for passport in passports:
	if idx == 152:
		print('flag')
	valid = check_pass(passport, True)
	if valid:
		print_list.append(idx)
		count += 1
	idx += 1
print(count)

with open('day4_org.txt', 'w+') as f:
	f.write('\n'.join([str(x) for x in print_list]))
