"""Write one office joke to /output/entry.txt.

make.fun bounty: Make the AI Judge Laugh: Office Jokes.
One line about office life, under 200 characters, nothing else.
"""

import os

JOKE = (
    "The reply-all thread has outlived three managers and two reorgs "
    "\u2014 the intern who started it just asking for the Wi-Fi password "
    "is the admin now."
)


def main() -> None:
    # Gate check from the kit rules: 1-199 UTF-8 characters, one line.
    text = JOKE.strip()
    assert 1 <= len(text) <= 199, f"joke is {len(text)} chars, must be 1-199"
    assert "\n" not in text, "joke must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
