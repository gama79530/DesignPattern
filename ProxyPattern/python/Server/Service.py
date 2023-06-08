import Pyro5.api
import threading
from Proxy import Proxy

class Account:
    def __init__(self) -> None:
        self._balance:int = 0

    @property
    def balance(self) -> int:
        return self._balance
    
    def addBalanceAccount(self, amount:int):
        self._balance += amount
    
    def subtractBalanceAccount(self, amount:int):
        self._balance -= amount

@Pyro5.api.expose
class Skeletons(Proxy):
    def __init__(self, account:Account) -> None:
        self._account = account

    def addBalanceAccount(self, balanceAccount: int):
        print(f"Proxy add balance account {balanceAccount}")
        self._account.addBalanceAccount(balanceAccount)

    def subtractBalanceAccount(self, balanceAccount: int):
        print(f"Proxy subtract balance account {balanceAccount}")
        self._account.subtractBalanceAccount(balanceAccount)

    @property
    def balanceAccount(self) -> int:
        return self._account.balance
        

class Service:
    def __init__(self, host:str, nameServerPort:int, daemonPort:int) -> None:
        self._host = host
        self._nameServerPort = nameServerPort
        self._daemonPort = daemonPort

        self._nameServerUri, self._nameServerDaemon, self._broadcastServer = Pyro5.api.start_ns(host=self._host, port=self._nameServerPort)
        self._daemon = Pyro5.api.Daemon(host=self._host, port=self._daemonPort)
        threading.Thread(target=lambda:self._nameServerDaemon.requestLoop()).start()
        threading.Thread(target=lambda:self._daemon.requestLoop()).start()
        self._nameServer = Pyro5.api.locate_ns(host=self._host, port=self._nameServerPort)

    @property
    def host(self):
        return self._host
    
    @property
    def nameServerPort(self):
        return self._nameServerPort
    
    @property
    def daemonPort(self):
        return self._daemonPort
    
    @property
    def nameServerDaemon(self):
        return self._nameServerDaemon

    @property
    def daemon(self):
        return self._daemon
    
    def bind(self, name, skeleton):
        uri = self._daemon.register(skeleton)
        self._nameServer.register(name, uri)
    
    def __del__(self):
        self._daemon.close()
        self._nameServerDaemon.close()


if __name__ == "__main__":
    account = Account()
    skeleton = Skeletons(account)

    host = "127.0.0.1"
    nameServerPort = 8090 
    daemonPort = 8091
    service = Service(host, nameServerPort, daemonPort)

    name = "accountProxy"
    service.bind(name, skeleton)
    print("Service Start")
    print("======================================================")


