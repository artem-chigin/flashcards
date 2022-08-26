from enum import Enum


class AnswerInDefinitions(Enum):
    YES = "The answer in the definitions"
    NO = "The answer is not in the definitions"


class Card:

    def __init__(self, term, definition):
        self.term = term
        self.definition = definition

    def save_card(self):
        return self


def num_input():
    print("How many times to ask?")
    num = input()
    if not num.isdigit():
        print("Please input a positive, integer number. Like 1, 5, or 154")
        return num_input()
    return int(num)


def term_input(term_value: str, list_of_cards: list) -> str:
    for card_object in list_of_cards:
        if term_value == card_object.term:
            print(f'The term "{term_value}" already exists. Try again')
            return term_input(input(), list_of_cards)
    return term_value


def definition_input(definition_value: str, list_of_cards: list) -> str:
    for card_object in list_of_cards:
        if definition_value == card_object.definition:
            print(f'The definition "{definition_value}" already exists. Try again:')
            return definition_input(input(), list_of_cards)
    return definition_value
