## 	pyhton 3.67
## 	Gedit 
##	116cs0177	
##	Crypto

from Crypto.Cipher import AES
from Crypto import Random
from random import randint,seed,shuffle
import sys

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
	shuffle(key)# shuffle works on list only
	key=''.join(key)
	print(key)
	key=key.encode('utf-8')# linux to win
	## shuffled key is ready
	return key
	

key=key_generator()

# now take the string and prepare it   
print("enter the text to be encoded")
msg=input()

msg_length=len(msg)
space_padding_length=16-(msg_length%16)
print(msg_length)
print(space_padding_length)

#space padding
i=0
for i in range(space_padding_length):
	msg=msg+' '

msg_length=len(msg)
print(msg_length)

if	(msg_length % 16 !=0):
	print("ERROR")
	sys.exit()

#	create the initialization vector
i_vector=Random.new().read(AES.block_size)

# create the ciphering object
cipher=AES.new(key,AES.MODE_CBC,i_vector)
msg=msg.encode('utf-8')
# do the encryption
encrypted=cipher.encrypt(msg)
print(encrypted)
print(type(encrypted))

