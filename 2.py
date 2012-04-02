# Write a Python program which will accept the name of a directory from the command line and it will print names of only those files whose size is greater than 1000 #bytes (hint: use os.stat)


import os,sys
from stat import *

def list_dir(arg):
	filenames=os.listdir(arg)
	for filename in filenames:
		#print filename
		path=os.path.join(arg,filename)
		if os.path.exists(path):
			if os.path.isfile(path):
				size=os.stat(path)
				s=size[ST_SIZE]
				print s
				if s>=1000:	print filename
			else:
				list_dir(path)
def main():
	arg=sys.argv[1]
	list_dir(arg)

if __name__ =='__main__':
	main()
