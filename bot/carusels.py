from question import Question

from typing import Dict, Tuple

from telebot import Telebot


class Carusel(ABC):
    step_num = 0

    def __init__(self, bot):
        self.bot = bot

    @abstractmethod
    def step(self, message: types.Message) -> Union[Tuple[str, types.ReplyKeyboardMarkup], None]:
        pass

    @property
    @abstractmethod
    def is_ready(self) -> bool:
        pass


class QuestionCarusel(Carusel):
    question = None


class SelectorCarusel(QuestionCarusel):
    def step(self, message: types.Message) -> Union[Tuple[str, types.ReplyKeyboardMarkup], None]:
        if step_num == 0:
            pass

    def is_ready(self) -> bool:
        return self.step_num == 5
