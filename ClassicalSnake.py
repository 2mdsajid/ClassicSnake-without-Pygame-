import time
import random
import sys, select

def clear():
	import os
	os.system( 'clear' )

def items():
	global l,r,n,m,times, op
	times=1
	l="__"*times
	r="|"
	n=random.randint(1,360)
	op=random.randint(1,360)
items()


def score():
	global n,op, times
	if n==op:
		times+=1
		op=random.randint(op,360)
	get_move()


def right():
	global n,m, times,op
	m="d"
	n+=1
	print(l.rjust(n))
	object()


def left():
	global n,m, times,op
	m="a"
	n-=1
	print(l.rjust(n))
	object()


def up():
	global n,m,times,op
	m="w"
	n-=60
	if n%op<60 or n%op>60:
		op+=60
	print(r.rjust(n))
	for turn in range(times-1):
		print(r.rjust(n%60))
		n-=60
	object()


def down():
	global n,m,times,op
	m="s"
	n+=60
	if n%op<60 or n%op>60:
		op-=60
	print(r.rjust(n))
	for turn in range(times-1):
		print(r.rjust(n%60))
		n+=60
	object()


def object():
	global op,n
	print("$".rjust(op))
	score()



def move():
	global di,n,times
	clear()
	if n<1 or n>2400:
		print("Oopps ! Hit The Boundary")
		exit()
	if m=="w":
		up()
	elif m=="s":
		down()
	elif m=="d":
		right()
	elif m=="a":
		left()
	else:
		print("SORRY WRONG MOVE")
		exit()


def get_move():
	global m,times
	i, o, e = select.select( [sys.stdin], [], [], 0.5)
	if (i):
		m=sys.stdin.readline().strip()
		move()
	else:
		move()

m="d"
right()



