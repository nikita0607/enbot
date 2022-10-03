import docx2txt

from enum import Enum
from typing import IO, List, Union, Tuple
from abc import ABC, abstractmethod


class QuestionParser(ABC):
    type = ''

    @classmethod
    @abstractmethod
    def parse(cls, text: str) -> Tuple['Question', str]:
        pass


class SelectorParser(QuestionParser):
    type = 'selector'

    @classmethod
    def parse(cls, text: str) -> Tuple['Question', str]:
        pass


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


class QuestionStringParser:
    @classmethod
    def parse_questions(cls, text: str) -> List[Question]:
        questions = []

        while (parser := QuestionTypes.find_type(text)) is not None:
            quest, text = parser.parse(text)
            questions.append(quest)

        return questions


class QuestionDocxParser:
    @classmethod
    def parse_questions(cls, file_name: str) -> List[Question]:
        text = docx2txt.process(file_name, '/images')
        return QuestionStringParser.parse_questions(text)
