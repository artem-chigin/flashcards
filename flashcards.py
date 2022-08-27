import os
import io

import argparse
from random import choice
from enum import Enum
import json

import f_card
import print_and_log


class Commands(Enum):
    ADD = "add"
    REMOVE = "remove"
    IMPORT = "import"
    EXPORT = "export"
    ASK = "ask"
    EXIT = "exit"

    LOG = "log"
    HARDEST_CARD = "hardest card"
    RESET_STATS = "reset stats"


def add_card(term: str, definition: str, cards_values: list) -> list:
    card = f_card.Card(term, definition)
    cards_values.append(card)
    message = f'The pair ("{term}":"{definition}") has been added'
    logger.print_and_log(message)
    return cards_values


def remove_card(card_name_to_delete: str, cards_values: list) -> list:
    for card in cards_values:
        if card_name_to_delete == card.term:
            cards_values.remove(card)
            message = "The card has been removed."
            logger.print_and_log(message)
            return cards_values
    message = f'Can\'t remove "{card_name_to_delete}": there is no such card'
    logger.print_and_log(message)
    return cards_values


def import_card(file_name: str, cards_values: list) -> list:

    file_path = os.path.join(".", file_name)
    if not os.access(file_path, os.F_OK):
        message = "File not found"
        logger.print_and_log(message)
    else:
        with open(file_path, "rt", encoding="utf-8") as file:
            imported_cards = json.load(file)
            added_cards_counter = 0
            for term, definition in imported_cards.items():
                card = f_card.Card(term, definition)
                cards_values.append(card)
                added_cards_counter += 1
        message = f"{added_cards_counter} cards have been loaded."
        logger.print_and_log(message)
        return cards_values


def export_card(file_name: str, cards_values: list):
    file_path = os.path.join(".", file_name)
    dict_fo_save = {}
    for card in cards_values:
        dict_fo_save[card.term] = card.definition
    with open(file_path, "wt", encoding="utf-8") as file:
        json.dump(dict_fo_save, file)
    message = f"{len(cards_values)} cards have been saved."
    logger.print_and_log(message)


def ask_card(card, cards_list):
    message = f'Print the definition of "{card.term}"'
    logger.print_and_log(message)

    answer = logger.input_and_log()
    if answer == card.definition:
        message = "Correct!"
        logger.print_and_log(message)
    else:
        card.mistakes += 1
        flag = f_card.AnswerInDefinitions.NO
        for new_obj in cards_list:
            if answer == new_obj.definition:
                msg = f"""Wrong. The right answer is "{card.definition}", but your definition is correct for "{new_obj.term}\""""
                logger.print_and_log(msg)
                flag = f_card.AnswerInDefinitions.YES
                break
        if flag == f_card.AnswerInDefinitions.NO:
            message = f"Wrong. The right answer is {card.definition}"
            logger.print_and_log(message)


def save_log(file_name):

    file_path = os.path.join(".", file_name)
    with open(file_path, "at", encoding="utf-8") as file:
        file.write(output.getvalue())
    out_msg = "The log has been saved."
    logger.print_and_log(out_msg)


def hard_card(cards_values):
    if not cards_values:
        message = "There are no cards with errors"
        logger.print_and_log(message)
    else:
        max_mistakes = max(card.mistakes for card in cards_values)
        difficult_cards = list(filter(lambda card: card.mistakes == max_mistakes, cards_values))

        if len(difficult_cards) == len(cards_values):
            message = "There are no cards with errors"
            logger.print_and_log(message)
        elif len(difficult_cards) == 1:
            logger.print_and_log(f'The hardest card is "{difficult_cards[0].term}". You have {max_mistakes} errors answering it.')
        else:
            msg = ['The hardest cards are'] + list(map(lambda x: f"{x.term}", difficult_cards)) + [f'You have {max_mistakes} errors answering them.']
            logger.print_and_log(", ".join(msg))


def reset_stats(cards_values):
    for card in card_deck:
        card.mistakes = 0
    logger.print_and_log("Card statistics have been reset.")
    return cards_values


def menu_input_and_check():
    message = "Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats)"
    logger.print_and_log(message)

    command_value = logger.input_and_log()
    for command in Commands:
        if command_value == command.value:
            return command
    msg = "Wrong command"
    logger.print_and_log(msg)
    return menu_input_and_check()


def menu(command_value: Enum, cards: list):

    if command_value == Commands.ADD:
        add_msg_1 = "The card:"
        logger.print_and_log(add_msg_1)

        term = f_card.term_input(logger.input_and_log(), cards, logger)
        add_msg_2 = "The definition of the card:"
        logger.print_and_log(add_msg_2)

        definition = f_card.definition_input(logger.input_and_log(), cards, logger)
        cards = add_card(term, definition, cards)
        return cards
    elif command_value == Commands.REMOVE:
        remove_msg = "Which card?"
        logger.print_and_log(remove_msg)
        cards = remove_card(logger.input_and_log(), cards)
        return cards
    elif command_value == Commands.IMPORT:
        if import_file_name is not None:
            import_card(import_file_name, cards)
        else:
            import_msg = "File name:"
            logger.print_and_log(import_msg)
            import_card(logger.input_and_log(), cards)
    elif command_value == Commands.EXPORT:
        if export_file_name is not None:
            export_card(export_file_name, cards)
        else:
            export_msg = "File name:"
            logger.print_and_log(export_msg)
            export_card(logger.input_and_log(), cards)
    elif command_value == Commands.ASK:
        num = f_card.num_input(logger)
        for _ in range(num):
            random_card = choice(cards)
            ask_card(random_card, cards)
    elif command_value == Commands.LOG:
        input_msg = "File name:"
        logger.print_and_log(input_msg)
        file_name = logger.input_and_log()
        save_log(file_name)
    elif command_value == Commands.HARDEST_CARD:
        hard_card(cards)
    elif command_value == Commands.RESET_STATS:
        reset_stats(cards)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--import_from", nargs="?", default=None)
    parser.add_argument("--export_to", nargs="?", default=None)
    args = parser.parse_args()

    import_file_name = args.import_from
    # print(import_file_name)
    export_file_name = args.export_to

    card_deck = []

    output = io.StringIO()
    logger = print_and_log.Logger(output)

    menu_command = None

    if import_file_name is None:
        menu_command = menu_input_and_check()
    else:
        menu_command = Commands.IMPORT

    while menu_command != Commands.EXIT:
        menu(menu_command, card_deck)
        menu_command = menu_input_and_check()

    message = "Bye bye!"
    logger.print_and_log(message)

    if export_file_name is not None:
        menu(Commands.EXPORT, card_deck)

