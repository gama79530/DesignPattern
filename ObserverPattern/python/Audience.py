import abc

class Audience(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self):
        return NotImplemented
    
    
class TwitchAudience(Audience):
    def __init__(self, accountID, nickname) -> None:
        super().__init__()
        self._accountID= accountID
        self._nickname = nickname

    def update(self, streamInfo):
        print(f'\tAudience {self.nickname} receive the message: {streamInfo}')

    @property
    def accountID(self):
        return self._accountID
    
    @accountID.setter
    def accountID(self, val):
        self._accountID = val
        
    @property
    def nickname(self):
        return self._nickname
    
    @nickname.setter
    def nickname(self, val):
        self._nickname = val
