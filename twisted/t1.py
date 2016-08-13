from twisted.internet import reactor,endpoints
from twisted.internet.protocol import Factory,Protocol

class Echo(Protocol):
    def connectionMade(self):
        self.transport.write(b"hi!")

    def dataReceived(self, data):
        print(data.decode())
        self.transport.write(b'enen'+data)

factory=Factory()
factory.protocol=Echo
reactor.listenTCP(4444,factory)
reactor.run()