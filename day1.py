
def calc_fuel(m):
    m = int(m)
    m = m // 3
    m = m - 2
    return m

with open('input/day1.txt') as f:
    modules = f.readlines()



def calc_fuel_fuel(fuel):
    add_fuel = calc_fuel(fuel)
    if add_fuel > 0:
        total_fuel = fuel + calc_fuel_fuel(add_fuel)
        return total_fuel
    else:
        return fuel


fuels = [calc_fuel_fuel(calc_fuel(m)) for m in modules]
total_fuel = sum(fuels)
print(total_fuel)


