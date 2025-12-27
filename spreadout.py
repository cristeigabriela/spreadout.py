import math

def get_spread_length(lst):
	if len(lst) == 0:
		return math.inf

	return max(lst) - min(lst)

def get_best_match(lhs, rhs):
	if lhs == [] and rhs == []:
		return []
	
	lhs_spread = get_spread_length(lhs)
	rhs_spread = get_spread_length(rhs)
	if lhs_spread < rhs_spread:
		return lhs

	# the case for >=
	return rhs

def find_spread_out(haystack, needle):
	# get rid of spaces
	needle = needle.replace(' ', '')

	# get sizes of needle and haystack as they will be reused
	needle_size, haystack_size = len(needle), len(haystack)
	
	# range should be limited to a minimum of sentence being
	# found in spread == needle_len
	search_range = haystack_size - needle_size

	# best present match, begins as empty list
	# contains the indices for each character in needle
	best_match = []

	# for each iteration, attempt to begin looking for a spreadout
	for i in range(0, search_range):
		# store how many characters of needle were found, in sequence
		matched_chars = 0

		# store the current match
		# contains the indices for each character in needle
		curr_match = []
		
		# match for this iteration (case-insensitive)
		for j in range(i, haystack_size):
			# get current haystack character
			hc = haystack[j].lower()

			# get current needle character at match cursor
			nc = needle[matched_chars].lower()
			
			if hc == nc:
				matched_chars += 1
				curr_match.append(j)
			
			# check if we finished a sequence
			if matched_chars == needle_size:
				# update best match if we found a better one
				best_match = get_best_match(best_match, curr_match)
				break

	if best_match == []:
		print('debug: no matches for ', needle)
	return best_match


def get_args():
	import sys
	
	args = sys.argv
	if len(args) != 3:
		print('zoinks dude! not enough arguments!')
		print(f'example usage: python {args[0]} <file> <needle>')
		sys.exit(1)

	file, needle = args[1], args[2]
	file_contents = ''
	with open(file) as f:
		file_contents = f.read()

	return file_contents, needle

if __name__ == '__main__':
	import sys
	from colorama import Fore
	from colorama import Back
	from colorama import Style
	from colorama import init

	# init colorama
	init()

	# get file as string and needle
	file, needle = get_args()

	# get best match
	spreadout = find_spread_out(file, needle)

	if spreadout == []:
		print(f'zoinks, dude! cant find "{needle}" in your file!')
		sys.exit(1)

	for i in range(0, len(file)):
		if i not in spreadout:
			# print it with a white background and black foreground
			print(f'{Back.WHITE}{Fore.BLACK}{file[i]}{Style.RESET_ALL}', end = '')
		else:
			# print it normal
			print(file[i], end = '')
