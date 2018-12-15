import numpy as np
from time import time

MAX_STEPS = 2250
SIZE = 5

def esperance(size, max_steps):
	esperance = 0
	pos = size * size // 2 
	hold_seed = '0'
	grid = '0' * ((size-1) * size) + '1' * size
	final_state = '1' * size + '0' * ((size-1) * size)
	probas = {grid + ',' + str(pos) + hold_seed: 1.0}

	for step in xrange(1, MAX_STEPS+1):
		new_probas = {}
		for key, prev_p in probas.iteritems():
			grid, X = key.split(',')
			pos = int(X[:-1])
			hold_seed = X[-1]
			moves = []
			if pos>=size: moves.append(pos - size)
			if pos<size*(size-1): moves.append(pos + size)
			if pos % size != 0 : moves.append(pos - 1)
			if pos % size != size-1: moves.append(pos + 1)

			p = 1. / len(moves)

			for move in  moves:
				new_grid = str(grid)
				new_hold_seed = hold_seed
				if hold_seed=='1' and move<size and new_grid[move]=='0':
					new_grid = new_grid[:move] + '1' + new_grid[move+1:]
					new_hold_seed = '0'
				elif hold_seed=='0' and move>=size*(size-1) and new_grid[move]=='1':
					new_grid = new_grid[:move] + '0' + new_grid[move+1:]
					new_hold_seed = '1'

				if move<size and new_hold_seed=='0' and new_grid==final_state:
					esperance += step * prev_p * p
				else:
					new_key = new_grid + ',' + str(move) + new_hold_seed
					if new_key in new_probas.keys():
						new_probas[new_key] += prev_p * p
					else:
						new_probas[new_key] = prev_p * p

		probas = dict(new_probas)
		print "Esperance at step %d is : %f" % (step, esperance)

	return esperance

t = time()
print "ANSWER IS : %f" % esperance(SIZE, MAX_STEPS)
print "Total time %f" % (time() - t)