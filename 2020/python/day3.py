from sys import stdin
from typing import List, Tuple

Grid = List[List[bool]]
Pos = Tuple[int,int]

def move(p: Pos, slope: Tuple[int, int]) -> Pos:
	x,y = p
	dx,dy = slope
	return (x+dx,y+dy)

def posY(p: Pos) -> int:
	_,y = p
	return y

def zeroPos() -> Pos:
	return (0,0)

def size(trees: Grid) -> int:
	return len(trees[0])

def height(trees: Grid) -> int:
	return len(trees)

def position(trees: Grid, pos: Pos) -> bool:
	n = size(trees)
	x,y = pos
	return trees[y][x % n]


def part(trees: Grid, slope: Tuple[int,int]) -> int:
	h = height(trees)
	current = zeroPos()
	hits = 0
	while(current[1] < len(trees)):
		print(f"{current}: {position(trees, current)}")
		hits += 1 if position(trees, current) else 0
		current = move(current, slope)
	return hits

def parse(line: str) -> List[bool]:
	return [t == '#' for t in line.replace('\n','')]

def part1(trees):
	return part(trees, (3,1))

trees = [parse(l) for l in stdin.readlines()]
slope1 = part(trees, (1,1))
print(slope1)
print("*"*7)
slope2 = part(trees, (3,1))
print(slope2)
print("*"*7)
slope3 = part(trees, (5,1))
print(slope3)
print("*"*7)
slope4 = part(trees, (7,1))
print(slope4)
print("*"*7)
slope5 = part(trees, (1,2))
print(slope5)
print("-"*7)
print(slope1*slope2*slope3*slope4*slope5)
