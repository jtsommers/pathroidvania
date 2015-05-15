try:
	import Queue as Q  # ver. < 3.0
except ImportError:
	import queue as Q
from collections import defaultdict

verbose = True
def debug(*args):
	if (verbose):
		print ''.join([str(arg) for arg in args])

# Trivial heuristic
def null_heuristic(state):
	return 0

# Generic A* search
def single_source_search(graph, initial, heuristic=null_heuristic):
	# Initialization
	frontier = Q.PriorityQueue()
	# Save out a sequence of states to the goal
	previous = {}
	previous[initial] = None
	# Save the actions taken to get to that state
	action_to_state = {}
	# Store the cost of the path so far
	cost_so_far = {}
	cost_so_far[initial] = 0
	frontier.put((0, initial))

	# 
	# DOMAIN SPECIFIC
	points = defaultdict(lambda:[])
	position, abilities = initial
	points[position].append(initial)
	# 
	# 

	while not frontier.empty():
		priority, current_state = frontier.get()

		# Traverse the adjacent nodes
		for action, next_state, cost in graph(current_state):
			new_cost = cost_so_far[current_state] + cost
			if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
				cost_so_far[next_state] = new_cost
				previous[next_state] = current_state
				action_to_state[next_state] = action
				priority = new_cost + heuristic(next_state)
				frontier.put((priority, next_state))

				# 
				# DOMAIN SPECIFIC
				position, abilities = next_state
				points[position].append(next_state)
				# 
				# 

	return previous, cost_so_far, points
