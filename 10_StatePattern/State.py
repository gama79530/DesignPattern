"""
    # All concrete classes should extend State.

    # All concrete classes should implement the following methods.
    def insertQuarter(self):
    def ejectQuarter(self):
    def turnCrank(self):
    def dispense(self):
    def refill(self):
"""
import random

class State :
    def insertQuarter(self):
        assert False, 'This method should be overrided.'
        
    def ejectQuarter(self):
        assert False, 'This method should be overrided.'
        
    def turnCrank(self):
        assert False, 'This method should be overrided.'
        
    def dispense(self):
        assert False, 'This method should be overrided.'
        
    def refill(self):
        assert False, 'This method should be overrided.'

class HasQuarterState(State):
    def __init__(self, gumball_machine):
        self.random_winner = random.randrange
        self.gumball_machine = gumball_machine

    def insertQuarter(self):
        print("You can't insert another quarter")
        
    def ejectQuarter(self):
        print("Quarter returned")
        self.gumball_machine.state = self.gumball_machine.no_quarter_state
        
    def turnCrank(self):
        print("You turned...")
        winner = (self.random_winner(10) == 0)
        if winner and self.gumball_machine.count > 1:
            self.gumball_machine.state = self.gumball_machine.winner_state
        else:
            self.gumball_machine.state = self.gumball_machine.sold_state
        
    def dispense(self):
        print("No gumball dispensed")
        
    def refill(self):
        pass

    def __str__(self):
        return "waiting for turn of crank"

class NoQuarterState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insertQuarter(self):
        print("You inserted a quarter")
        self.gumball_machine.state = self.gumball_machine.has_quarter_state
        
    def ejectQuarter(self):
        print("You haven't inserted a quarter")
        
    def turnCrank(self):
        print("You turned, but there's no quarter")
        
    def dispense(self):
        print("You need to pay first")
        
    def refill(self):
        pass

    def __str__(self):
        return "waiting for quarter"
        
class SoldOutState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine
        
    def insertQuarter(self):
        print("You can't insert a quarter, the machine is sold out")
        
    def ejectQuarter(self):
        print("You can't eject, you haven't inserted a quarter yet")
        
    def turnCrank(self):
        print("You turned, but there are no gumballs")
        
    def dispense(self):
        print("No gumball dispensed")
        
    def refill(self):
        self.gumball_machine.state = self.gumball_machine.no_quarter_state
    
    def __str__(self):
        return "sold out"

class SoldState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insertQuarter(self):
        print("Please wait, we're already giving you a gumball")
        
    def ejectQuarter(self):
        print("Sorry, you already turned the crank")
        
    def turnCrank(self):
        print("Turning twice doesn't get you another gumball!")
        
    def dispense(self):
        self.gumball_machine.releaseBall()
        if self.gumball_machine.count > 0:
            self.gumball_machine.state = self.gumball_machine.no_quarter_state
        else:
            self.gumball_machine.state = self.gumball_machine.sold_out_state

    def refill(self):
        pass

    def __str__(self):
        return "dispensing a gumball"

class WinnerState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insertQuarter(self):
        print("Please wait, we're already giving you a Gumball")
        
    def ejectQuarter(self):
        print("Please wait, we're already giving you a Gumball")
        
    def turnCrank(self):
        print("Turning again doesn't get you another gumball!")
        
    def dispense(self):
        self.gumball_machine.releaseBall()
        if self.gumball_machine.count == 0:
            self.gumball_machine.state = self.gumball_machine.sold_out_state
        else:
            self.gumball_machine.releaseBall()
            print("YOU'RE A WINNER! You got two gumballs for your quarter")
            if self.gumball_machine.count > 0:
                self.gumball_machine.state = self.gumball_machine.no_quarter_state
            else:
                self.gumball_machine.state = self.gumball_machine.sold_out_state

    def refill(self):
        pass

    def __str__(self):
        return "despensing two gumballs for your quarter, because YOU'RE A WINNER!"