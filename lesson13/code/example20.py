from abc import ABC, ABCMeta
class Hero(ABC):
    ...

# или:
class Hero(metaclass=ABCMeta):
    ...