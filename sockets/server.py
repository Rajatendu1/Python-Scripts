import socket
import time
import pickle

HEADERSIZE = 10#notify user the number of characters they can Send

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#AF_INET refers to the address family ipv4. The SOCK_STREAM means connection oriented TCP protocol.
s.bind((socket.gethostname(), 1234)) #A server has a bind() method which binds it to a specific ip and port so that it can listen to incoming requests on that ip and port
#The Python function socket.gethostname() returns the host name of the current system under which the Python interpreter is executed.
s.listen(5)#Listen for connections made to the socket. The backlog argument specifies the maximum number of queued connections and should be at least 0; the maximum value is system-dependent (usually 5), the minimum value is forced to 0.

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()#Accept a connection. The socket must be bound to an address and listening for connections. The return value is a pair (conn, address) where conn is a new socket object usable to send and receive data on the connection, and address is the address bound to the socket on the other end of the connection.
    print(f"Connection from {address} has been established.")
    d = {1:"hi", 2: "there"}
    msg = pickle.dumps(d)
    #msg = "Welcome to the server!"
    msg = bytes(f"{len(msg):<{HEADERSIZE}}",'utf-8')+msg#<:10 means align the text to the left by 10 characters
    print (msg)
    clientsocket.send(msg)#send(obj) Send an object to the other end of the connection which should be read using recv().

    '''while True:
        time.sleep(3)
        msg = f"The time is {time.time()}"
        msg = f"{len(msg):<{HEADERSIZE}}"+msg

        print(msg)

        clientsocket.send(bytes(msg,"utf-8"))'''
