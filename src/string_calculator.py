import re

def add(numbers: str) -> int:
    if not numbers:
        return 0

    # Check for custom delimiter
    delimiter_pattern = r"//(\[.*?\]|.)\n"
    match = re.match(delimiter_pattern, numbers)
    if match:
        delimiters = match.group(1)
        if delimiters.startswith("["):
            delimiters = re.findall(r"\[(.*?)\]", delimiters)
        else:
            delimiters = [delimiters]
        numbers = numbers[match.end():]
    else:
        delimiters = [',', '\n']

    # Create regex pattern for delimiters
    delimiter_regex = '|'.join(map(re.escape, delimiters))
    split_numbers = re.split(delimiter_regex, numbers)

    # Convert to integers and handle negatives
    int_numbers = []
    negatives = []
    for n in split_numbers:
        if n.strip():
            try:
                num = int(n)
                if num < 0:
                    negatives.append(num)
                elif num <= 1000:
                    int_numbers.append(num)
            except ValueError:
                continue

    if negatives:
        raise ValueError(f"Negatives not allowed: {', '.join(map(str, negatives))}")

    return sum(int_numbers)