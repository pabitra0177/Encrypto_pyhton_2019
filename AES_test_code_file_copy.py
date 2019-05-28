## now try to do the same but read the  string from a file


from Crypto.Cipher import AES
from Crypto import Random
from random import randint,seed,shuffle
import sys,os,struct

padd=['#','@','!','$','%','&','?','>','<','+',]


def key_generator():
	print('Enter the alpha-numeric key')
	key=input()
	####  key = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
	# standard  key length is 12+4;; 4 is the size of fixed padding
	key_length=len(key)
	# if nothing is inserted prompt again
	if	(key_length==0):
		print('Enter the key')
		key=input()
	
	key_length=len(key)
	if	(key_length>12): 
		key=key[:12] # if input key length crosses 12 truncate it
		key_length=12

	#print(key)
	padding_length=16-key_length;
	i=0
	## randomness generator  seed()
	seed()
	for i in range(padding_length):
		x=randint(0,9)
		key=key+padd[x]

	#print(key)  # now the 16 byte key is ready
	# shufflling
	key=list(key)
	shuffle(key)
	key=''.join(key)
	print(key)
	## shuffled key is ready
	return key

def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
	if not out_filename:
		out_filename = in_filename + '.enc'

	iv =Random.new().read(AES.block_size)
	encryptor = AES.new(key, AES.MODE_CBC, iv)
	filesize = os.path.getsize(in_filename)

	with open(in_filename, 'r') as infile:
		with open(out_filename, 'ab') as outfile:
			outfile.write(struct.pack('<Q', filesize))
			outfile.write(iv)

			while True:
				chunk = infile.read(chunksize)
				print(type(chunk))
				if len(chunk) == 0:
					break
				elif len(chunk) % 16 != 0:
					chunk += ' ' * (16 - len(chunk) % 16)

				outfile.write(encryptor.encrypt(chunk))
	outfile.close()
			

	
key=key_generator()
encrypt_file(key,'mice.txt')


