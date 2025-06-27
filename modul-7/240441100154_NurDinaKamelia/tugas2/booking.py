from abc import ABC, abstractmethod

class Booking(ABC):
    @abstractmethod
    def proses_booking(self, usia):
        pass
