from collections import defaultdict

def calculate_letter_frequencies(data, prefix=''):
	frequencies = defaultdict(int)
	for i in range(0, len(data)-len(prefix)):
		if data[i:i+len(prefix)] == prefix:
			frequencies[data[i+len(prefix)]] += 1
	return frequencies

def solve(challenge):
	result = ''
	while not result or result[-1] != ';':
		freq = calculate_letter_frequencies(challenge, result[-1] if result else '')
		result += sorted(freq.items(), key=lambda x: x[1])[-1][0]
	return result[:-1]
