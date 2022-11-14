from abc import ABC, abstractmethod
class Hero(ABC):
    @abstractmethod
    def attack(self):
        pass