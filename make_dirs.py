import os, argparse

def make_dir(wanted_dir):
	if os.path.exists(wanted_dir):
		print("Info: directory %s already exists!“ % wanted_dir)
	else:
		os.makedir(wanted_dir)

def parse_paras():
	parser = argparse.ArgumentParser(description='make a dir if not exists')
	parser.add_argument('d', type=str, nargs=1, help='wanted directory name')
	
	return parser

def main():
	parser = parse_paras()
	args = vars(parser.parse_args())
	wanted_dir = args['d'][0]
	
	make_dir(wanted_dir)

if __name__ == '__main__':
	main()
