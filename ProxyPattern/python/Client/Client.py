import Pyro5.api
import Pyro5.errors
import sys

if __name__ == "__main__":
    sys.excepthook = Pyro5.errors.excepthook

    host = "127.0.0.1"
    nameServerPort = 8090 
    daemonPort = 8091

    nameserver = Pyro5.api.locate_ns(host=host, port=nameServerPort)
    uri = nameserver.lookup("accountProxy")
    stub = Pyro5.api.Proxy(uri)

    amount = 1000
    print(f"Add Balance Account: {amount}")
    stub.addBalanceAccount(amount)
    print(f"Current balance account: {stub.balanceAccount}")

    amount = 100
    print(f"Subtract Balance Account: {amount}")
    stub.subtractBalanceAccount(amount)
    print(f"Current balance account: {stub.balanceAccount}")
