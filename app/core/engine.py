from abc import ABC, abstractmethod


class Engine(ABC):
    """
    جميع محركات MANARAH ترث من هذا الكلاس.
    """

    @abstractmethod
    def execute(self, session):
        pass