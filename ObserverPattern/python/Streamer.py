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
        self._audience = set()
        self._account_info = account_info
        self._is_streaming = False

    def registerObserver(self, observer):
        self._audience.add(observer)
        
    def removeObserver(self, observer):
        self._audience.discard(observer)

    def notifyObserver(self):
        stream_info = f"Streamer {self.account_info} is streaming now." if self.is_streaming else f"Streamer {self.account_info} is off-stream now."
        for observer in self._audience:
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

