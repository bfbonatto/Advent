from sys import stdin

def part1(modules):
	return sum(filter(lambda v: v > 0, [int(value/3) - 2 for value in modules]))

def additional(fuel):
	add = int(fuel/3 - 2)
	if add <= 0:
		return 0
	return add + additional(add)

def part2(modules):
	return sum([additional(m) for m in modules])

modules = [int(m) for m in stdin.readlines()]
print(f"part1: {part1(modules)}")
print(f"part2: {part2(modules)}")
