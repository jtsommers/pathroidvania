from p6_game import Simulator
from collections import defaultdict

try:
	import Queue as Q  # ver. < 3.0
except ImportError:
	import queue as Q

import astar

ANALYSIS = {}

def analyze(design):
	sim = Simulator(design)

	# Setup for the start state
	init = sim.get_initial_state()
	
	# Define graph traversal
	all_moves = sim.get_moves()
	def graph(state):
		for move in all_moves:
			next_state = sim.get_next_state(state, move)
			# Make sure the mantis didn't die
			if next_state:
				yield (move, next_state, 1)

	# prev = dictionary saving out the previous state mapping
	# cost = dictionary saving out cost to get to a state
	# points = dictionary saving out the position to state mappings
	prev, cost, points = astar.single_source_search(graph, init)

	ANALYSIS['prev'] = prev
	ANALYSIS['points'] = points

def inspect((i,j), draw_line):
	# TODO: use ANALYSIS and (i,j) draw some lines
	raise NotImplementedError