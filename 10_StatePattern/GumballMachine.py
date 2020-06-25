import State

class GumballMachine:
    def __init__(self, number_gumballs):
        self.sold_out_state = State.SoldOutState(self)
        self.no_quarter_state = State.NoQuarterState(self)
        self.has_quarter_state = State.HasQuarterState(self)
        self.sold_state = State.SoldState(self)
        self.winner_state = State.WinnerState(self)
        self.count = number_gumballs
        if number_gumballs:
            self.state = self.no_quarter_state
        else:
            self.state = self.sold_out_state
        
    def insertQuarter(self):
        self.state.insertQuarter()
        
    def ejectQuarter(self):
        self.state.ejectQuarter()
        
    def turnCrank(self):
        self.state.turnCrank()
        self.state.dispense()
        
    def releaseBall(self):
        print("A gumball comes rolling out the slot...")
        if self.count:
            self.count -= 1

    def refill(self, count):
        self.count += count
        print("The gumball machine was just refilled; it's new count is: {}".format(str(self.count)))
        self.state.refill()
        
    def __str__(self):
        single_str = 's' if self.count != 1 else ''
        result = "\nMighty Gumball, Inc.\nPython-enabled Standing Gumball Model #2004\nInventory: {} gumball{}\nMachine is {}\n".format(
            str(self.count), single_str, str(self.state)
        )
        return result