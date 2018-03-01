from generator import generate
import argparse
import random
import string
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--seed",default="random")
	parser.add_argument("--maxlen",default=50,type=int)
	parser.add_argument("--numnames",default=1,type=int)
	args = parser.parse_args()
	seed = args.seed#"Q"
	maxlen = args.maxlen#50
	number_of_names = args.numnames#1
	for i in range(number_of_names):
		if args.seed == "random":
			seed = random.choice(list(string.ascii_uppercase))
		name = generate.sample(seed,maxlen)
		print(name)


if __name__ == "__main__":
	main()

