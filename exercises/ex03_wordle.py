"""Structured wordle game."""

__author__ = "730389944"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word_to_search: str, char: str) -> bool:
    """Given a word and a single character, deterimine if the character is in the word."""
    assert len(char) == 1
    i: int = 0
    while i < len(word_to_search):
        if word_to_search[i] == char:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Print an emoji str showing the user how their guess matches up to secret."""
    assert len(guess) == len(secret)
    i: int = 0
    res_str: str = ""
    while i < len(guess):
        if contains_char(secret, guess[i]):
            if secret[i] == guess[i]:
                res_str += GREEN_BOX
            else:
                res_str += YELLOW_BOX
        else: 
            res_str += WHITE_BOX
        i += 1
    return res_str


def input_guess(length_expected: int) -> str:
    """Makes sure the user's input is the right length, and doesn't stop until it is."""
    guess: str = input(f"Enter a {length_expected} character word: ")
    while len(guess) != length_expected:
        guess = input(f"That wasn't {length_expected} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turns_done: int = 0
    won: bool = False
    while turns_done < 6 and won is not True:
        print(f"=== Turn {turns_done + 1}/6 ===")
        guess: str = input_guess(5)
        print(emojified(guess, secret))
        turns_done += 1
        if guess == secret:
            won = True
    if won is True:
        print(f"You won in {turns_done}/6 turns!")
    else: 
        print("X/6 - Sorry, try again tomorrow!")
    return None


if __name__ == "__main__":
    main()