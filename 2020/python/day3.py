from sys import stdin
from typing import List, Tuple

Grid = List[List[bool]]
Pos = Tuple[int,int]

def move(p: Pos) -> Pos:
	x,y = p
	return (x+3,y+1)

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


def part(trees: Grid) -> int:
	h = height(trees)
	current = zeroPos()
	hits = 0
	for _ in range(h):
		print(f"{current}: {position(trees, current)}")
		hits += 1 if position(trees, current) else 0
		current = move(current)
	return hits

def parse(line: str) -> List[bool]:
	return [t == '#' for t in line.replace('\n','')]

trees = [parse(l) for l in stdin.readlines()]
print(part(trees))
