"""One shot wordle for the win!"""

__author__ = "730389944"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret: str = "python"

guess: str = input(f"What is your {len(secret)}-letter guess? ")

while len(guess) != len(secret):
    guess = input(f"That was not {len(secret)} letters! Try again: ")

i: int = 0
emoji_res: str = ""

while i < len(secret):
    if guess[i] == secret[i]:
        emoji_res += GREEN_BOX
    else:
        char_present: bool = False
        alt_index: int = 0
        while (not char_present and alt_index < len(secret)):
            if guess[i] == secret[alt_index]:
                char_present = True
            else:
                alt_index += 1
        if char_present:
            emoji_res += YELLOW_BOX
        else:
            emoji_res += WHITE_BOX
    i += 1

print(emoji_res)

if guess == secret: 
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")