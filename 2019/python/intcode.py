from sys import stdin
from typing import List, Tuple

ProgramState = Tuple[int, List[int]]

class ErrorException(Exception):
	def __init__(self, state):
		self.expression = state
		self.message = f"bad Instruction at {state[0]}"

class HaltException(Exception):
	pass

class Instruction:
	def __init__(self, state: ProgramState):
		self.state = state

	def execute(self) -> ProgramState:
		pass

class Error(Instruction):
	def __init__(self, s):
		super().__init__(s)
	def execute(self):
		raise(ErrorException(self.state))

class Halt(Instruction):
	def __init__(self, s):
		super().__init__(s)
	def execute(self):
		raise(HaltException())

class Add(Instruction):
	def __init__(self, state, a, b, c):
		self.a = a
		self.b = b
		self.c = c
		super().__init__(state)


	def execute(self):
		pc, mem = self.state
		mem[self.c] = self.a + self.b
		return (pc+4, mem)

class Mult(Instruction):
	def __init__(self, state, a, b, c):
		self.a = a
		self.b = b
		self.c = c
		super().__init__(state)

	def execute(self):
		pc, mem = self.state
		mem[self.c] = self.a * self.b
		return (pc+4, mem)

class Output(Instruction):
	def __init__(self, state, a):
		self.a = a
		super().__init__(state)

	def execute(self):
		pc, mem = self.state
		print(self.a)
		return (pc+2, mem)

class Input(Instruction):
	def __init__(self, state, a):
		self.a = a
		super().__init__(state)

	def execute(self):
		pc, mem = self.state
		mem[self.a] = input()
		return (pc+2, mem)

def fetch(s: ProgramState) -> Instruction:
	"""TODO"""
	pass

def parse(program: str) -> List[int]:
	return [int(v) for v in program.split(',')]

def execute(s: ProgramState) -> ProgramState:
	try:
		s = fetch(s).execute()
	except HaltException:
		return s
	return s
