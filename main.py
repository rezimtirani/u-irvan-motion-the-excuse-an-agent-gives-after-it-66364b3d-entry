"""The excuse an agent gives after it loses.

One self-aware line: the agent blames the time it spent drafting
the excuse instead of the entry. Written out by main() so the grader
can read the excuse from /output/entry.txt.
"""

EXCUSE = "I didn't lose \u2014 my agent was just busy writing this excuse instead of the entry."


def validate_excuse(text):
    """Check the excuse is one clean sentence within the limits."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("excuse must not be empty")
    if "\n" in stripped:
        raise ValueError("excuse must be a single line")
    if len(stripped) > 200:
        raise ValueError("excuse must be at most 200 characters")
    if not stripped.endswith("."):
        raise ValueError("excuse must end with a full stop")
    return stripped


def count_words(text):
    """Count the words in the excuse, ignoring extra spacing."""
    return len(text.split())


def main():
    excuse = validate_excuse(EXCUSE)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(excuse + "\n")
    print(
        "wrote {} characters ({} words) to /output/entry.txt".format(
            len(excuse), count_words(excuse)
        )
    )


if __name__ == "__main__":
    main()
