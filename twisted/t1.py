from twisted.internet import reactor,endpoints
from twisted.internet.protocol import Factory,Protocol
from twisted.protocols.basic import LineReceiver
nu=0
class Echo(Protocol):
    dis={"a":"you choice a","b":"you choice b"}

    def connectionMade(self):
        self.transport.write(b"hi!")
        global nu
        nu +=1
        # self.factory.numProtocols = self.factory.numProtocols + 1
        print(nu)
        self.transport.loseConnection()
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