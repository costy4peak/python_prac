import os, argparse

def renames(dir, old_ext, new_ext):
	for filename in os.listdir(dir):
		file_splits = os.path.splitext(filenmae)
		ext = file_splits[1]
		
		if ext == old_ext:
			newfile = file_splits[0] + new_ext
			
			old_file_name = os.path.join(dir, filename)
			new_file_name = os.path.join(dir, newfile)
			
			os.rename(old_file_name, new_file_name)

def get_parser():
	parser = argparse.ArgumentParser(description='Change extension of files in a working directory')
	parser.add_argument('dir', metavar='DIR', type=str, nargs=1, help='Files under this dir will change extension')
	parser.add_argument('old_ext', metavar='OLD_EXT', type=str, nargs=1, help='old extension')
	parser.add-argument('new_ext', metavar='NEW_EXT', type=str, nargs=1, help='new extension')

	return parser
	
def main():
	parser = get_parser()
	args = vars(parser.parse_args())
	
	work_dir = args['old_ext'][0]
	old_ext = args['old_ext'][0]
	
	if old_ext[0] != ".":
		old_ext = "." + old_ext
	
	new_ext= args['new_ext'][0]
	if new_ext[0] != ".":
		new_ext = "." + new_ext
	
	renames(dir, old_ext, new_ext)
	
if __name__ == "__main__":
	main()
	
