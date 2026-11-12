"""Duration parsing (synthetic sandbox code)."""


def parse_duration(text: str) -> int:
    """Return the number of seconds in a duration such as "1h30m" or "45s".

    Format: optional hours, then optional minutes, then optional seconds, in that
    order, each written as a non-negative integer followed by "h", "m" or "s",
    each unit at most once, no spaces. At least one unit is required.
    Anything else (empty string, unknown unit, wrong order, repeated unit,
    spaces, signs, decimals) raises ValueError.
    """
    raise NotImplementedError
