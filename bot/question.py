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


class Question:
    def __init__(self, _type=None):
        self.type = _type

