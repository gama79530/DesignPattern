"""
    Each function performs a kind of quack behavior of duck and accept 2 arguments - *args and **kwargs.
"""
def quack(*args, **kwargs):
    print('Quack!')
    
def squack(*args, **kwargs):
    print('Squack!')

def mute_quack(*args, **kwargs):
    print('<<Silence>>!')