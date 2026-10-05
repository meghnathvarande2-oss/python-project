import sys
import time
import os

# MAA TUJHE SALAAM — Python Lyrics Timeline

NEON_CYAN = "\033[38;5;51m"
GOLD_GLOW = "\033[38;5;220m"
SOFT_WHITE = "\033[97m"

BOLD = "\033[1m"
RESET = "\033[0m"

CLEAR = "\033[2J\033[H"

# Timing settings
CHAR_SPEED = 0.045
LINE_PAUSE = 0.75
SECTION_PAUSE = 1.4

LYRICS = [
    "yahan wahan sara jahan dekh liya hai",
    "kahin bhi tere jaisa koi nahin hai",
    "assi nahin, sau din duniya ghooma hai",
    "nahin kahin tere jaisa koi nahin",
    "main gaya jahan bhi",
    "bas teri yaad thi",
    "jo mere saath thi",
    "mujhako tadpati, rulati",
    "sabse pyari teri surat",
    "pyar hai bus tera, pyar hi",

    "maa tujhe salam",
    "maa tujhe salam",
    "mamma tujhe salam",

    "vande mataram (vande mataram)",
    "vande mataram (vande mataram)",
    "vande mataram vande mataram",
    "vande mataram vande mataram"
]


def adaptive_typing(text, color, speed=CHAR_SPEED):
    """Print text character-by-character."""
    for char in text:
        sys.stdout.write(f"{BOLD}{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(speed)

    print()


def play_song():
    # Clear terminal
    os.system("cls" if os.name == "nt" else "clear")

    # Title
    print(f"{GOLD_GLOW}{BOLD}IN MAA TUJHE SALAAM{RESET}")
    print(f"{NEON_CYAN}Python Lyrics Timeline{RESET}")
    print()

    # Play lyrics
    for i, line in enumerate(LYRICS):

        # First section
        if i < 10:
            color = SOFT_WHITE

        # Maa tujhe salam section
        elif i < 13:
            color = GOLD_GLOW

        # Vande mataram section
        else:
            color = NEON_CYAN

        adaptive_typing(line, color)

        time.sleep(LINE_PAUSE)

        # Pause before final section
        if i == 12:
            time.sleep(SECTION_PAUSE)


if __name__ == "__main__":
    play_song()