import abc

class Streamer(metaclass=abc.ABCMeta):
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
    @abc.abstractmethod
    def account_info(self):
        return NotImplemented
    
    @account_info.setter
    @abc.abstractmethod
    def account_info(self):
        return NotImplemented
    
    @property
    @abc.abstractmethod
    def is_streaming(self):
        return NotImplemented
    
    @is_streaming.setter
    @abc.abstractmethod
    def is_streaming(self):
        return NotImplemented
    

class TwitchStreamer(Streamer):
    def __init__(self, account_info) -> None:
        # super().__init__()
        self._audience = dict()
        self._account_info = account_info
        self._is_streaming = False

    def registerObserver(self, observer):
        if not observer.accountID in self._audience:
            self._audience[observer.accountID] = observer
        
    def removeObserver(self, observer):
        if observer.accountID in self._audience:
            del self._audience[observer.accountID]

    def notifyObserver(self):
        stream_info = f"Streamer {self.account_info} is streaming now." if self.is_streaming else f"Streamer {self.account_info} is off-stream now."
        for _, observer in self._audience.items():
            observer.update(stream_info)

    @property
    def account_info(self):
        return self._account_info
    
    @account_info.setter
    def account_info(self, val):
        self._account_info = val

    @property
    def is_streaming(self):
        return self._is_streaming
    
    @is_streaming.setter
    def is_streaming(self, val):
        if val != self._account_info:
            self._is_streaming = val
            self.notifyObserver()

