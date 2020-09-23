from intcode import execute, parse

prog = parse()
part1 = execute(prog.copy(), 12, 2)
part2 = next(100*noun + verb for noun in range(100) for verb in range(100) if execute(prog.copy(), noun, verb) == 19690720)

print(f"part1: {part1}")
print(f"part2: {part2}")
