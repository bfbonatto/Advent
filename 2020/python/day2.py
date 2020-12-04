from sys import stdin

class Policy:
	def __init__(self, minN: int, maxN: int, char: str):
		self.minN = minN
		self.maxN = maxN
		self.char = char

	def validate(self, password: str) -> bool:
		count = password.count(self.char)
		return count >= self.minN and count <= self.maxN

	def validate2(self, password: str) -> bool:
		first_position = password[self.minN -1]
		second_position = password[self.maxN -1]
		return first_position != second_position and (first_position == self.char or second_position == self.char)

def parse(line):
	policy, password = line.split(':')
	minimax,char = policy.split()
	password = password.replace(' ','')
	minN,maxN = minimax.split('-')
	return (Policy(int(minN), int(maxN), char), password)

lines = [parse(l) for l in stdin.readlines()]
print( sum( [ 1 if p.validate2(ps) else 0 for (p,ps) in lines ] ) )
