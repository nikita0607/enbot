from abc import ABC, abstractmethod

from enum import Enum
from typing import Union


class QuestionTypes(Enum):
    SELECTOR = SelectorParser
    
    @classmethod
    def find_type(cls, string: str) -> Union[None, QuestionParser]:
        for s in string.split():
            for _type in cls:
                if _type.value.type == s.lower().strip():
                    return _type.value


class ABCQuestion(ABC):
    def __init__(self):
        self.attachments = []


    @abstractmethod
    def send_to_chat(self, chat_id):
        pass


class SelectorQuestion:
    def send_to_chat(self, cl, chat_id: int):
        pass
