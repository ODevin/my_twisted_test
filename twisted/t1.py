from twisted.internet import reactor,endpoints
from twisted.internet.protocol import Factory,Protocol
from twisted.protocols.basic import LineReceiver
class Echo(Protocol):
    dis={"a":"you choice a","b":"you choice b"}

    def connectionMade(self):
        self.transport.write(b"hi!")

    def dataReceived(self, data):
        res=data.decode().strip()
        print(res)
        if res in self.dis:
            print("yes,in this")
            self.transport.write(b'enen'+self.dis[res].encode()+b'\r\n')
        else:
            self.transport.write(b'i do not what you mean\r\n')
factory=Factory()
factory.protocol=Echo
reactor.listenTCP(4444,factory)
reactor.run()