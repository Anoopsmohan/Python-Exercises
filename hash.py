# Write a program which will discover files whose contents are exactly the same ("duplicate files"). Your program accepts a directory name as command line parameter #and checks files in that directory only.

import os,sys, hashlib
dic={}

def hash_value(arg):
	filenames=os.listdir(arg)
	for filename in filenames:
		path=os.path.join(arg,filename)
		if os.path.exists(path):
			if os.path.isfile(path):
				m=hashlib.md5()
		       		f=open(path,'r')
		     		m.update(f.read())
			        value=m.digest()
				if value not in dic:
					dic[value]=list()		
				dic[value].append(filename)
	return dic
					
def duplicates(files):
	for file in files:
		if len(files[file])>1:
			print files[file]

def main():
	arg=sys.argv[1]
        a=hash_value(arg)
	duplicates(a)
	
if __name__ =='__main__':
	main()
