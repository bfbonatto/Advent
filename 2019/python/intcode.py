from sys import stdin
from typing import List

def execute(program: List[int], noun: int, verb: int) -> int:
	pc = 0
	program[1] = noun
	program[2] = verb
	while program[pc] != 99:
		if program[pc] == 1:
			v1 = program[pc+1]
			v2 = program[pc+2]
			v3 = program[pc+3]
			program[v3] = program[v1] + program[v2]
		elif program[pc] == 2:
			v1 = program[pc+1]
			v2 = program[pc+2]
			v3 = program[pc+3]
			program[v3] = program[v1] * program[v2]
		pc += 4
	return program[0]

def parse() -> List[int]:
	input = stdin.readline()
	return [int(v) for v in input.split(',')]
