from enum import Enum
import print_and_log


class AnswerInDefinitions(Enum):
    YES = "The answer in the definitions"
    NO = "The answer is not in the definitions"


class Card:

    def __init__(self, term, definition, mistakes=0):
        self.term = term
        self.definition = definition
        self.mistakes = mistakes

    # def save_card(self):
    #     return self


def num_input(logger):
    message = "How many times to ask?"
    logger.print_and_log(message)
    # print()

    num = logger.input_and_log()
    if not num.isdigit():
        message = "Please input a positive, integer number. Like 1, 5, or 154"
        logger.print_and_log(message)
        # print()
        return num_input(logger)
    return int(num)


def term_input(term_value: str, list_of_cards: list, logger: print_and_log.Logger) -> str:
    for card_object in list_of_cards:
        if term_value == card_object.term:
            message = f'The term "{term_value}" already exists. Try again'
            logger.print_and_log(message)
            # print()
            return term_input(logger.input_and_log(), list_of_cards, logger)
    return term_value


def definition_input(definition_value: str, list_of_cards: list, logger: print_and_log.Logger) -> str:
    for card_object in list_of_cards:
        if definition_value == card_object.definition:
            message = f'The definition "{definition_value}" already exists. Try again:'
            logger.print_and_log(message)
            # print()
            return definition_input(logger.input_and_log(), list_of_cards, logger)
    return definition_value
