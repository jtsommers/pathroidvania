from p6_game import Simulator
from collections import defaultdict

ANALYSIS = {}

def analyze(design):
	sim = Simulator(design)
	# Dictionary saving out the previous state mapping
	prev = {}
	# Dictionary saving out the position to state mappings
	points = defaultdict(lambda: [])

	# Setup for the start state
	init = sim.get_initial_state()
	position, abilities = init

	prev[init] = None;
	points[position].append(init)

	### Sample usage of state traversal
	# moves = sim.get_moves()
	# next_state = sim.get_next_state(init, moves[0])

	# position, abilities = next_state # or None if character dies
	# i, j = position



	# TODO: fill in this function, populating the ANALYSIS dict
	ANALYSIS['prev'] = prev
	ANALYSIS['points'] = points
	raise NotImplementedError

def inspect((i,j), draw_line):
	# TODO: use ANALYSIS and (i,j) draw some lines
	raise NotImplementedError