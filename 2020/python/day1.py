from sys import stdin
from typing import List


def part1(values: List[int]) -> int:
	for i in values:
		for j in values:
			for k in values:
				if i != j and i != k and j != k and i+j+k == 2020:
					return i*j*k
	return -1

values = [int(n.replace('\n','')) for n in stdin.readlines()]
print(part1(values))
