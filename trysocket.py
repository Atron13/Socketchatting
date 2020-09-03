import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket successfully created")
link='192.168.56.1'
serv.bind((link, 8081))
print("socket connected to 8081 on ip 192.168.56.1")

serv.listen(5)
print("socket is in the listing state")
print("waiting for connection")
print('')
print('')

ran=1

while True:
    conn, addr = serv.accept()
    from_client = ''
    clientname=conn.recv(1024)
    clientname=clientname.decode()
    print(">>>>",clientname,"as client has connected to the server")
    print('')
    while True:
        data = conn.recv(4096)
        if not data: break
        tempdata=data.decode() #from_client += tempdata
        print(link," ",clientname," >>>> ",tempdata)
        print('data received---------')
        if tempdata =='bye':
        	print(clientname," has left the server")
        	break
        print('')
        if ran == 1:
        	print(">>>> enter data for the client")
        	print('')
        ran=2 #I am SERVER<br> 
        #print()
        t=input('server >>>> ')
        print('data send-------------')
        if t== 'bye':
        	print("server connection disconnected from your side")
        	break
        print('')
        tr=t.encode()
        conn.send(tr)
        

    conn.close()
    print ('client disconnected')