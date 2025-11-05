import re


def add(numbers: str) -> int:
    """Add numbers from a string with various delimiter formats.

    Args:
        numbers: String containing numbers to add

    Returns:
        Sum of numbers in the string

    Raises:
        ValueError: If negative numbers are present
    """
    if not numbers:
        return 0

    # Extract custom delimiters if present
    delimiters = [',', '\n']
    numbers_to_parse = numbers

    if numbers.startswith('//'):
        delimiter_section, numbers_to_parse = numbers.split('\n', 1)
        delimiter_section = delimiter_section[2:]  # Remove '//'

        # Check for bracket syntax: //[delim1][delim2]...
        if delimiter_section.startswith('['):
            # Extract all delimiters from brackets
            delimiters = re.findall(r'\[([^\]]+)\]', delimiter_section)
        else:
            # Single character delimiter
            delimiters = [delimiter_section]

    # Build regex pattern to split by any delimiter
    # Escape special regex characters
    escaped_delimiters = [re.escape(d) for d in delimiters]
    pattern = '|'.join(escaped_delimiters)

    # Split and convert to integers
    parts = re.split(pattern, numbers_to_parse)
    nums = []
    negatives = []

    for part in parts:
        part = part.strip()
        if part:
            num = int(part)
            if num < 0:
                negatives.append(num)
            elif num <= 1000:
                nums.append(num)

    # Check for negative numbers
    if negatives:
        neg_str = ', '.join(map(str, negatives))
        raise ValueError(f"Negative numbers not allowed: {neg_str}")

    return sum(nums)
