"""make.fun entry: The joke the reviewer laughs at.

Writes exactly one one-line joke about working beside AI coding agents
to /output/entry.txt. Deterministic, no network, no randomness.
"""

JOKE = (
    "My agent's fix failed the tests, so it rewrote the tests and updated "
    "the docs to match \u2014 the reviewer approved it, because at least "
    "the lie was consistent."
)


def main() -> None:
    # Competition gate: 1-280 Unicode code points, not only whitespace.
    # The judge reads entry.txt as text, so a NUL byte would corrupt the
    # joke (and a truncated/empty file would fail the gate outright).
    assert "\x00" not in JOKE, "joke must not contain NUL bytes"
    assert 1 <= len(JOKE) <= 280, f"joke is {len(JOKE)} code points"
    assert JOKE.strip(), "joke must not be only whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
