import os

EMOJI = "\U0001F5FB"


def main():
    # Gate: exactly one emoji, 1-8 chars, not whitespace-only.
    assert 1 <= len(EMOJI) <= 8 and EMOJI.strip()
    out = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
