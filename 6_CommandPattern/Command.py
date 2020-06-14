"""
    # All concrete classes should extend Command and overide the following methods
    def execute(self) :
    def undo(self) :
"""

class Command :
    def execute(self) :
        assert False, 'This method should be overrided.'

    def undo(self) :
        assert False, 'This method should be overrided.'

class NoCommand(Command) :
    def execute(self) :
        pass

    def undo(self) :
        pass
