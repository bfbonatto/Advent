from sys import stdin
from typing import List,Tuple
from graphics import *

def move(init, direction, amount):
	x,y = init
	if direction == "U":
		return (x,y+amount)
	if direction == "D":
		return (x,y-amount)
	if direction == "L":
		return (x-amount,y)
	if direction == "R":
		return (x+amount,y)

def draw_wire(line: List[Tuple[str,int]], color, window):
	current = (320,240)
	for d,a in line:
		next = move(current, d, a)
		p1 = Point(current[0], current[1])
		p2 = Point(next[0], next[1])
		line_draw = Line(p1,p2)
		line_draw.setFill(color)
		line_draw.setWidth(1)
		line_draw.draw(window)
		current = next

wire1 = [(s[0],int(s[1])) for s in stdin.readline().split(',')]
wire2 = [(s[0],int(s[1])) for s in stdin.readline().split(',')]

win = GraphWin("Test", 640, 480)
win.setBackground(color_rgb(0,0,0))

draw_wire(wire1, color_rgb(255,0,0), win)
draw_wire(wire2, color_rgb(0,0,255), win)
win.getMouse()
win.close()

