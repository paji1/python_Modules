# ArithmeticError
import sys

if len (sys.argv) != 3:
	exit()
try :
	try :
		print("Sum:        {}".format(int(sys.argv[1]) + int(sys.argv[2])))
	except ArithmeticError as err:
		print("impossible! : " , err)
	try :
		print("Difference: {}".format(int(sys.argv[1]) - int(sys.argv[2])))
	except ArithmeticError as err:
		print("impossible! : " , err)
	try :
		print("Product:    {}".format(int(sys.argv[1]) * int(sys.argv[2])))
	except ArithmeticError as err:
		print("impossible! : " , err)
	try :
		print("Quotient:   {}".format(int(sys.argv[1]) / int(sys.argv[2])))
	except ArithmeticError as err:
		print("impossible! : " , err)
	try :
		print("Remainder:  {}".format(int(sys.argv[1]) % int(sys.argv[2])))
	except ArithmeticError as err:
		print("impossible! : " , err)
except ValueError as err:
	print("not integer! : "  , err)
	
    
	