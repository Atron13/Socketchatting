import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
link='192.168.56.1'
client.connect((link, 8081))

name=input('Enter the client name:')
print('')
print('')
name=name.encode()
client.send(name)

print(">>>> enter data to send to server")
print('')

while True:
	
	
	#print()
	sendclient=input("client >>>> ")
	tempsend=sendclient.encode()
	print('data send-------------')
	if tempsend == 'bye':
		print(name," you have disconnected")
		break
	client.send(tempsend)
	print('')
	tempreceive=client.recv(4096)
	from_server = tempreceive.decode()
	print(link," server >>>>",from_server)
	print('data received---------')
	if from_server =='bye':
		print("server has left no connection")
		break
	print('')
	

client.close()
