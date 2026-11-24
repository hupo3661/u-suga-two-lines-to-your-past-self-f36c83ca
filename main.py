"""Two Lines to Your Past Self - make.fun entry.

Writes exactly two lines (1-280 characters total) to /output/entry.txt.
Line one warns a past self about one specific moment; line two says,
in one sentence, why that moment mattered and what changed because of it.
"""

from pathlib import Path

ENTRY_TEXT = (
    "Don't toss Dad's old physics textbook into the donation box on moving night "
    "\u2014 open it to page 112 first.\n"
    "Taped inside is the letter he wrote the day you were born; finding it at "
    "sixteen, not forty, lets you know him while he's still alive to ask."
)

OUTPUT_PATH = Path("/output/entry.txt")


def validate(text: str) -> None:
    """Raise ValueError unless text is exactly two lines, 1-280 chars.

    Each line must also be a single sentence: it ends with a period and
    contains no other sentence-ending punctuation, as the brief requires
    one sentence per line.
    """
    if not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError(f"entry must be exactly two lines, got {len(lines)}")
    for line in lines:
        if not line.strip():
            raise ValueError("neither line may be blank")
        if line != line.strip():
            raise ValueError("lines must not have leading or trailing spaces")
        if not line.endswith(".") or line.count(".") != 1:
            raise ValueError(f"each line must be one sentence ending in '.': {line!r}")
        if "!" in line or "?" in line:
            raise ValueError(f"each line must be a single plain sentence: {line!r}")
    if not 1 <= len(text) <= 280:
        raise ValueError(f"entry must be 1-280 characters, got {len(text)}")


def main() -> None:
    validate(ENTRY_TEXT)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    validate(written)
    if written != ENTRY_TEXT:
        raise ValueError("read-back does not match the entry text")
    print(f"Wrote {OUTPUT_PATH} ({len(written)} characters, 2 lines)")


if __name__ == "__main__":
    main()
