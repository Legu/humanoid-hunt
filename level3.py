from collections import defaultdict

import sys
sys.setrecursionlimit(1000000) # One MILLION coz why not

def solve(challenge):
	maze = defaultdict(lambda: defaultdict(str))
	for line in challenge.split('\n'):
		if ' ' in line:
			coord, moves = line.split(' ')
		else:
			coord = line
			moves = ''
		x, y = (int(a) for a in coord.split(','))
		maze[x][y] = 'N'
		for move in moves.split(','):
			if move == 'X' or move == 'S' or move == 'F':
				if move == 'S':
					start = (x, y)
				maze[x][y] = move
				break
			if move == 'U': y -= 1
			if move == 'D': y += 1
			if move == 'L': x -= 1
			if move == 'R': x += 1
			maze[x][y] = 'N'
	return solve_maze(maze, start[0], start[1], '')

def solve_maze(maze, x, y, moves):
	if not maze[x][y] or maze[x][y] == 'X' or maze[x][y] == 'V':
		return None
	if maze[x][y] == 'F':
		return moves
	maze[x][y] = 'V'
	solution = solve_maze(maze, x, y - 1, moves + 'U') or \
		solve_maze(maze, x, y + 1, moves + 'D') or \
		solve_maze(maze, x - 1, y, moves + 'L') or \
		solve_maze(maze, x + 1, y, moves + 'R')
	return solution
