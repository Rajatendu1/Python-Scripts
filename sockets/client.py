import socket
import pickle#pickle — Python object serialization


HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))#socket.connect(address)

while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16)#socket.recv(bufsize[, flags]) Receive data from the socket. The return value is a bytes object representing the data received. The maximum amount of data to be received at once is specified by bufsize.
        if new_msg:
            print("new msg len:",msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        print(f"full message length: {msglen}")

        full_msg += msg
#bytes.decode Return a string decoded from the given bytes
        print(len(full_msg))


        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])
            print(pickle.loads(full_msg[HEADERSIZE:]))#Read a pickled object hierarchy from a bytes object and return the reconstituted object hierarchy specified therein.
            new_msg = True
            full_msg = b''
