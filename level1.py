def process_line(line):
	i = 0
	saw_first = False
	while True:
		byte = int(line[i:i+8], base=2)
		if byte > len(line) / 8:
			if saw_first:
				return chr(byte)
			else:
				i += 8
		else:
			saw_first = True
			i = byte * 8

def solve(challenge):
	return ''.join([process_line(line) for line in challenge.split()])
