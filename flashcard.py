import string
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


def num_input ():
    print("Input the number of cards:")
    num = input()
    if not num.isdigit():
        print("Please input a positive, integer number. Like 1, 5, or 154")
        return num_input()
    return int(num)


def term_input(term_value: str, list_of_cards: list) -> str:
    for card_object in list_of_cards:
        if term_value == card_object.term:
            print(f'The term "{term_value}" already exists. Try again')
            return term_input(list_of_cards)
    return term_value


def definition_input(definition_value: str, list_of_cards: list) -> str:
    for card_object in list_of_cards:
        if definition_value == card_object.definition:
            print(f'The definition "{definition_value}" already exists. Try again:')
            return definition_input(list_of_cards)
    return definition_value

#
# def add_card():
#     pass
#

#
# if __name__ == "__main__":
#
#     number_of_cards = num_input()
#     cards = []
#
#     for i in range(number_of_cards):
#         number = i + 1
#
#         print(f"The term for card #{number}:")
#         term = term_input(cards, number)
#
#         print(f"The definition for card #{number}:")
#         definition = definition_input(cards, number)
#
#         card = Card(term, definition)
#         cards.append(card.save_card())
#
#     for obj in cards:
#         print(f'Print the definition of "{obj.term}"')
#         answer = input()
#
#         if answer == obj.definition:
#             print("Correct!")
#         else:
#             flag = AnswerInDefinitions.NO
#             for new_obj in cards:
#                 if answer == new_obj.definition:
#                     msg = f"""Wrong. The right answer is "{obj.definition}", but your definition is correct for "{new_obj.term}\""""
#                     print(msg)
#                     flag = AnswerInDefinitions.YES
#                     break
#             if flag == AnswerInDefinitions.NO:
#                 print(f"Wrong. The right answer is {obj.definition}")
