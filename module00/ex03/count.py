# The text contains 143 character(s):
# - 2 upper letter(s)
# - 113 lower letter(s)
# - 4 punctuation mark(s)
# - 18 space(s)

import sys
def text_analyzer(str):
	print("# The text contains {} character(s):".format(len(str)))
	print("# - {} upper letter(s)".format(sum(1 for c in str if c.isupper())))
	print("# - {} lower letter(s)".format (sum(1 for c in str if c.islower())))
	print("# - {} punctuation mark(s)".format(sum(1 for c in str if  (".,?!".find(c)) != -1)))
	print("# - {} lower letter(s)".format (sum(1 for c in str if c.isspace())))



if __name__ == "__main__" and len (sys.argv) == 2:
	text_analyzer(sys.argv[1])