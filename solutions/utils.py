def split_and_map(data: str) -> list[list[int]]:
    """
    We were doing similar transformations to similar data over day 1 and 2
    so moved a small piece of initial logic to this util.

    Splits the input data into lines and converts each line to a list of integers.

    Args:
        data (str): raw input data, multi line string
    Returns:
        list[list[int]]: List of lists of integers from the input
    """

    return [list(map(int, line.split())) for line in data.strip().splitlines()]
