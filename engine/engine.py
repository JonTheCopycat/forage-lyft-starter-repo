from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def __init__(self):
        #self.last_service_date = last_service_dates
        pass
    
    @abstractmethod
    def needs_service(self):
        pass