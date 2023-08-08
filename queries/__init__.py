from abc import ABC, abstractmethod

class AbstractDatabase(ABC):
    @abstractmethod
    def connect(self):
        pass
