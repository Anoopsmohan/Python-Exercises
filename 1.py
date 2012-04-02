# Write a Python program which will accept the name of a directory from the command line and recursively print the contents of the directory. (DO NOT run external #Linux commands from Python - solve this completely in Python. Use the functions os.listdir, os.path.exists, os.path.isfile. Be careful about handling "." and ".." #which are two special entries in a directory - "." is another name for the current directory and ".." is another name for the parent directory)

import os,sys

def list_dir(arg):
	filenames=os.listdir(arg)
	for filename in filenames:
		#print filename
		path=os.path.join(arg,filename)
		if os.path.exists(path):
			if os.path.isfile(path):
				print filename
			else:
				list_dir(path)
def main():
	arg=sys.argv[1]
	list_dir(arg)

if __name__ =='__main__':
	main()
