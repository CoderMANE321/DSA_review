from abc import ABC, abstractmethod

class DataStructure(ABC):
    @abstractmethod
    def add_element(self, element):
        pass

    @abstractmethod
    def remove_element(self, element):
        pass

    @abstractmethod
    def access_element(self, element):
        pass
