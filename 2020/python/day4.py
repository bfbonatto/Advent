from sys import stdin
from typing import Dict, Optional

class Passport:
	def __init__(self, data: Dict[str,str]):
		self.birth_year = data["byr"]
		self.issue_year = data["iyr"]
		self.expiration_year = data["eyr"]
		self.height = data["hgt"]
		self.hair_color = data["hcl"]
		self.eye_color = data["ecl"]
		self.passport_id = data["pid"]
		self.country_id = data["cid"] if "cid" in data else None

def parse(entries: str) -> Optional[Passport]:
	data = { k:v for k,v in map(lambda e: e.split(':'), entries.split()) }
	return Passport(data) if isValid(data) else None

def isValid(data: Dict[str,str]) -> bool:
	byr = "byr" in data and len(data["byr"]) == 4 and (int(data["byr"]) >= 1920 and int(data["byr"]) <= 2002)
	iyr = "iyr" in data and len(data["iyr"]) == 4 and (int(data["iyr"]) >= 2010 and int(data["iyr"]) <= 2020)
	eyr = "eyr" in data and len(data["eyr"]) == 4 and (int(data["eyr"]) >= 2010 and int(data["eyr"]) <= 2020)

	return True

allInputs = stdin.read()
possible_passports = allInputs.split("\n\n")
passports = map(lambda p: parse(p), possible_passports)
print(sum([ 1 if p is not None else 0 for p in passports ]))
