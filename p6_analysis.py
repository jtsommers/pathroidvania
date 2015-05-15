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
	inspection_point = (i,j)
	prev = ANALYSIS['prev']
	points = ANALYSIS['points']

	for state in points[inspection_point]:
		# Use this state as the basis for a line back to the start
		position, used_abilities = state
		current_state = state
		previous_state = prev[current_state]
		while previous_state:
			src, abilities = current_state
			dst, unused = previous_state
			draw_line(src, dst, used_abilities, used_abilities)
			current_state = previous_state
			previous_state = prev[current_state]
