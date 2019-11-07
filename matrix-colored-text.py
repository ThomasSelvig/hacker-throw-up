import random, time, argparse
from lorem.text import TextLorem
from colorama import init, Fore, Back, Style

availible = {
	"fore": ["BLACK", "RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "WHITE", "RESET"],
	"back": ["BLACK", "RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "WHITE", "RESET"],
	"style": ["DIM", "NORMAL", "BRIGHT", "RESET_ALL"]
}

def getColors():
	fore = getattr(Fore, random.choice(availible["fore"]))
	back = getattr(Back, random.choice(availible["back"]))
	style = getattr(Style, random.choice(availible["style"]))

	return fore + back + style

def pause(mod=1):
	time.sleep(random.random()*mod)

def main(args):
	init()
	lorem = TextLorem(srange=(1, args.length))
	while True:
		print(getColors() + lorem.sentence().lower().replace(".", ""), end="")
		if args.time > 0:
			pause(args.time)


if __name__ == '__main__':
	try:
		parser = argparse.ArgumentParser()
		parser.add_argument("-t", "--time", type=float, default=0)
		parser.add_argument("-l", "--length", type=int, default=1)

		main(parser.parse_args())

	except KeyboardInterrupt:
		pass