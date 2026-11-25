"""Fortune Cookie Wisdom for Developers -- round 2 entry.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt. The line is checked against the 1-120 character gate.
Pure standard library only, so it runs on the grader's python:3.13-slim.
"""

ENTRY = "The fortune you seek is in the log file you cleared this morning."


def main():
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 120, "entry must be 1-120 characters"
    data = text.encode("utf-8")
    assert len(data) <= 120, "entry must be 1-120 bytes"
    assert not data.endswith(b"\n"), "no trailing newline"
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    print(f"wrote {len(data)} bytes / {len(text)} chars")


if __name__ == "__main__":
    main()
