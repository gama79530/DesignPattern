import abc

class Streamer(metaclass=abc.ABCMeta):
    def __init__(self) -> None:
        self.accountInfo = None
        self._isStreaming = False

    @abc.abstractmethod
    def registerObserver(self):
        return NotImplemented
        
    @abc.abstractmethod
    def removeObserver(self):
        return NotImplemented

    @abc.abstractmethod
    def notifyObserver(self):
        return NotImplemented
    
    @property
    def isStreaming(self):
        return self._isStreaming
    
    @isStreaming.setter
    def isStreaming(self, val):
        if self._isStreaming != val:
            self._isStreaming = val
            self.notifyObserver()
    

class TwitchStreamer(Streamer):
    def __init__(self, accountInfo) -> None:
        super().__init__()
        self._audience = set()
        self.accountInfo = accountInfo

    def registerObserver(self, observer):
        self._audience.add(observer)
        
    def removeObserver(self, observer):
        self._audience.discard(observer)

    def notifyObserver(self):
        stream_info = f"Streamer {self.accountInfo} is streaming now." if self.isStreaming else f"Streamer {self.accountInfo} is off-stream now."
        for observer in self._audience:
            observer.update(stream_info)


