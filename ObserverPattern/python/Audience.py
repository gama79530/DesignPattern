import abc

class Audience(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self):
        return NotImplemented
    
    
class TwitchAudience(Audience):
    def __init__(self, accountID, nickname) -> None:
        super().__init__()
        self.accountID= accountID
        self.nickname = nickname

    def update(self, streamInfo):
        print(f'\tAudience {self.nickname} receive the message: {streamInfo}')

