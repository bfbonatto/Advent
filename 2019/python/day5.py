from intcode import *

with open('input', 'r') as infile:
	prog = parse(infile.readline())
	execute((0, prog))
