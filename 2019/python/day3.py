from sys import stdin

def move(init, direction, amount):
	x,y = init
	if direction == "U":
		return (x,y+amount)
	if direction == "D":
		return (x,y-amount)
	if direction == "L":
		return (x-amount,y)
	if direction == "R":
		return (x+amount,y)

def _range(f,t):
	x0,y0 = f
	x1,y1 = t
	if x0 < x1:
		return [(x,y0) for x in range(x0,x1+1)]
	if x0 > x1:
		return reversed([(x,y0) for x in range(x1,x0+1)])
	if y0 < y1:
		return [(x0,y) for y in range(y0,y1+1)]
	if y0 > y1:
		return reversed([(x0,y) for y in range(y1,y0+1)])

def parse(wire):
	current = (0,0)
	path = []
	for m in wire:
		direction, amount = m[0],int(m[1:])
		next = move(current, direction, amount)
		x0,y0 = current
		x1,y1 = next
		path += list(_range(current, next))[1:]
		current = next
	return path

def part1(wire1,wire2):
	w1 = set(wire1)
	w2 = set(wire2)
	for p in w1.intersection(w2):
		print(f"|{p}| = {abs(p[1]) + abs(p[0])}")

def part2(wire1, wire2):
	i1 = {p:i for i,p in enumerate(wire1)}
	i2 = {p:i for i,p in enumerate(wire2)}
	w1 = set(wire1)
	w2 = set(wire2)
	for p in w1.intersection(w2):
		print(f"steps to {p} = {i1[p] + i2[p] + 2}")

wire1 = parse(stdin.readline().split(','))
wire2 = parse(stdin.readline().split(','))
part2(wire1,wire2)

