from sys import argv ; from os.path import exists ; script, from_file, to_file = argv ;result_file = open(to_file,'w').write(open(from_file).read())

#print(f"copying from {from_file} to {to_file}")

#data = open(from_file).read()

#print(f"The input file is {len(data)} bytes long")

#print(f"Does the output file exist ? {exists(to_file)}")
#print("Ready, hit RETURN to continue, CTRL-C to abort.")
#input()

#out_file = open(to_file,'w').write(data)
#print("Alright, all done.")

