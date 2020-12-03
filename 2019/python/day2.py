from sys import stdin
from intcode import parse, fetch, execute

program = parse()
print(execute((0, program)))
