from enum import Enum
import flashcard
import os
import json
from random import sample


class Commands(Enum):
    ADD = "add"
    REMOVE = "remove"
    IMPORT = "import"
    EXPORT = "export"
    ASK = "ask"
    EXIT = "exit"


def add_card(term: str, definition: str, cards_values: list) -> list:
    card = flashcard.Card(term, definition)
    cards_values.append(card)
    print(f'The pair ("{term}":"{definition}") has been added')
    return cards_values


def remove_card(card_name_to_delete: str, cards_values: list) -> list:
    for card in cards_values:
        if card_name_to_delete == card.term:
            cards_values.remove(card)
            return cards_values
    print(f'Can\'t remove "{card_name_to_delete}": there is no such card')
    return cards_values


def import_card(file_name: str, cards_values: list) -> list:

    file_path = os.path.join(".", file_name)
    if not os.access(file_path, os.F_OK):
        print("File not found")
    else:
        with open(file_path, "rt", encoding="utf-8") as file:
            cards = json.load(file)
            added_cards_counter = 0
            for term, definition in cards.items():
                card = flashcard.Card(term, definition)
                cards_values.append(card)
                added_cards_counter += 1
        print(f"{added_cards_counter} cards have been loaded.")
        return cards_values


def export_card(file_name: str, cards_values: list):
    file_path = os.path.join(".", file_name)
    dict_fo_save = {}
    for card in cards_values:
        dict_fo_save[card.term] = card.definition
    with open(file_path, "wt", encoding="utf-8") as file:
        json.dump(dict_fo_save, file)
    print(f"{len(cards_values)} cards have been saved.")


def ask_card(cards_values):
    for obj in cards_values:
        print(f'Print the definition of "{obj.term}"')
        answer = input()
        if answer == obj.definition:
            print("Correct!")
        else:
            flag = flashcard.AnswerInDefinitions.NO
            for new_obj in cards:
                if answer == new_obj.definition:
                    msg = f"""Wrong. The right answer is "{obj.definition}", but your definition is correct for "{new_obj.term}\""""
                    print(msg)
                    flag = flashcard.AnswerInDefinitions.YES
                    break
            if flag == flashcard.AnswerInDefinitions.NO:
                print(f"Wrong. The right answer is {obj.definition}")


def menu_input_and_check():
    print("Input the action (add, remove, import, export, ask, exit)")
    command_value = input()
    for command in Commands:
        if command_value == command.value:
            return command
    print("Wrong command")
    return menu_input_and_check()


def menu(command_value, cards_value):

    cards = cards_value

    if command_value == Commands.ADD:
        print("The card:")
        term = cards.term_input(input(), cards)
        print("The definition of the card:")
        definition = cards.definition_input(input(), cards)
        cards = add_card(term, definition, cards)
        return cards
    elif command_value == Commands.REMOVE:
        print("Which card?")
        cards = remove_card(input(), cards)
        return cards
    elif command_value == Commands.IMPORT:
        print("File name:")
        import_card(input(), cards)
    elif command_value == Commands.EXPORT:
        print("File name:")
        export_card(input(), cards)
    elif command_value == Commands.ASK:
        num = int(input())
        random_cards = sample(cards, num)
        ask_card(random_cards)


if __name__ == "__main__":

    cards = []
    menu_command = menu_input_and_check()

    while menu_command != Commands.EXIT:
        menu(menu_command, cards)
        menu_command = menu_input_and_check()

    print("Bye bye!")
