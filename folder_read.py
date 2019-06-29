import os

path = 'E:\INTERNSHIP\Encryption_pyhton_2019-master'

file_list = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
	for file in f:
		file_list.append(os.path.join(r, file))

for f in file_list:
	print(f.split('\\'))
	print(f)
