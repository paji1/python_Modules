import sys




str = sys.argv[1::]
str = str[::-1]
for i in range (len (str))	:
	str[i] =  str[i][::-1]
str = ' '.join(str).swapcase()
print(str)
