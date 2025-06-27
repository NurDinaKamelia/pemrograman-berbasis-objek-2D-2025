from abc import ABC, abstractmethod

class Pembayaran (ABC):
    @abstractmethod
    def proses_pembayaran (self,jumlah):
        pass
