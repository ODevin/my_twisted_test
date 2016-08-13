from twisted.internet import reactor,endpoints
from twisted.internet.protocol import Factory,Protocol
from twisted.protocols.basic import LineReceiver

class rece(LineReceiver):
    def lineReceived(self, line, data):
        recedata=line.decode()
        if recedata in data:
            print("yes,in this")
        else:
            self.sendLine(b"i do not what you mean")


class Echo(Protocol):
    dis={"a":"you choice a","b":"you choice b"}

    def connectionMade(self):
        self.transport.write(b"hi!")

    def dataReceived(self, data):
        res=data.decode().strip()
        # res=data.decode().replace("\r\n","").replace("")
        # print(data.decode())
        print(res)
        # print(self.dis.keys())
        print(res == "a")
        # print("a" in self.dis.keys())
        if res in self.dis:
            print("yes,in this")
            self.transport.write(b'enen'+self.dis[res].encode())
        else:
            self.transport.write(b'i do not what you mean')
factory=Factory()
factory.protocol=Echo
reactor.listenTCP(4444,factory)
reactor.run()