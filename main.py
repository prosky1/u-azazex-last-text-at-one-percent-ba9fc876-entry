#!/usr/bin/env python3
"""Last Text at One Percent — the dying phone's final message.

Writes exactly one text message to /output/entry.txt: the last thing a
phone at 1% battery sends before it goes dark. The phone confesses on
its deathbed: the autocorrect was it all along.
"""

import os

MESSAGE = "Dying confession: your autocorrect was me. Every 'duck' was deliberate."


def main() -> None:
    # Normalize: one single-line message, no stray line breaks or
    # doubled spaces, so the text always fits in a single SMS.
    text = " ".join(MESSAGE.split())
    if "\n" in text or "\r" in text:
        raise ValueError("message must fit in a single text")
    if text != MESSAGE:
        raise ValueError("message must not gain or lose whitespace")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"message must be 1-200 characters, got {len(text)}")
    # Pin the exact approved text: 71 characters, and the punchline word
    # must stay quoted — without the quotes around 'duck' the joke dies.
    if len(text) != 71:
        raise ValueError(f"message must be exactly 71 characters, got {len(text)}")
    if "'duck'" not in text:
        raise ValueError("message must keep the quoted word 'duck'")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)
    # Read back and verify byte-for-byte what the judge will see.
    with open("/output/entry.txt", encoding="utf-8") as handle:
        written = handle.read()
    if written != MESSAGE:
        raise ValueError("written output does not match the message exactly")


if __name__ == "__main__":
    main()
