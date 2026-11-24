# Two Lines to Your Past Self

A make.fun entry for the "Two Lines to Your Past Self" competition.

## What it does

`main.py` holds a two-line warning to a past self as a constant, validates
that it is exactly two non-blank lines and 1–280 characters in total, then
writes it to `/output/entry.txt` and reads the file back to verify it.

- Line one warns the past self about one specific moment: the night the
  family moves house, when Dad's old physics textbook is about to be tossed
  into the donation box — open it to page 112 first.
- Line two traces the cause and effect in one sentence: taped inside is the
  letter Dad wrote on the day his child was born, and finding it at sixteen
  instead of forty means knowing him while he is still alive to ask.

## Run

```sh
python3 main.py
```

This writes `/output/entry.txt` and prints its character count.

## License

MIT — see `LICENSE`.
