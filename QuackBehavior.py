# e22mcag0011
# Kunal Nirankari
from abc import ABC, abstractmethod


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass
