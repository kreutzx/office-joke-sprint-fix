import os

# One-Line Office Joke: 24-Hour Sprint (make.fun bounty
# u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162).
# The brief caps each entry at 200 characters; the line is asserted
# against that cap before anything is written.
LINE = "Our CEO said 'we're a family' 14 times this quarter. My layoff email arrived Friday, subject line: 'A difficult family decision.'"
MAX_CHARS = 200


def render():
    """Return the entry line, validated against the bounty's cap."""
    line = LINE.strip()
    assert 1 <= len(line) <= MAX_CHARS, len(line)
    return line


def main():
    line = render()
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(line)
    # Read back what landed on disk: the judged bytes must be the line
    # itself, with no trailing newline or encoding surprise.
    with open(entry_path, encoding="utf-8") as f:
        assert f.read() == line


if __name__ == "__main__":
    main()
