import datetime, errno, optparse, select, socket

def connect(address):
    """Connect to the given server and return a non-blocking socket."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    sock.setblocking(0)
    a=[sock]
    poems = dict.fromkeys(a, '')
    # return sock
    print(poems)

# connect(("192.168.4.10",807))
class a():
    def __init__(self):
        self.aa="abc"

p=a()
print(p.aa)
p.cc="123"
print(p.cc)