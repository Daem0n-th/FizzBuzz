#!/usr/bin/python3

rules={'3':'fizz','5':'buzz'}

def main():
	for n in range(100):
		i=n
		for key in rules:
			if (n % int(key) == 0):
				try:
					i+=rules[key]
				except TypeError:
					i=rules[key]
		print(i)

if __name__ == '__main__':
	main()
