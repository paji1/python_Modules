import sys



if len (sys.argv) == 1:
	exit()
if len (sys.argv) > 2:
	print('AssertionError: more than one argument are provided')
	exit()
try:
	if (int(sys.argv[1]) % 2) == 0:
		print ("I'm Even.")
	else :
		print ("I'm Odd.")
except ValueError:
	print('AssertionError: argument is not an integer')