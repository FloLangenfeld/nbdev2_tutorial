# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/main_package.ipynb.

# %% auto 0
__all__ = ['say_hello', 'HelloSayer']

# %% ../nbs/main_package.ipynb 3
def say_hello(
    to:str="Florent",  # A qui dit-on bonjour?
    fake:float=4.5):
    "Say hello to somebody"
    return f'Hello {to}!'

# %% ../nbs/main_package.ipynb 5
class HelloSayer:
    "Say hello to `to` using `say_hello`"
    def __init__(
        self,
        to: str = "Florent") -> None:  # À qui dit-on bonjour?
        self.to = to
        
    def say(self) -> str:  # string
        "Do the saying"
        return say_hello(self.to)
