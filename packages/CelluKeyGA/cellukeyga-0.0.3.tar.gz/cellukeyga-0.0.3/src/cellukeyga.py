def add_two_digits(a, b):
    """
    Adds two single-digit numbers and returns the result.
    
    Parameters:
    a (int): The first single-digit number.
    b (int): The second single-digit number.
    
    Returns:
    int: The sum of the two single-digit numbers.
    """
    if 0 <= a <= 9 and 0 <= b <= 9:
        return a + b
    else:
        raise ValueError("Both numbers must be single-digit integers (0-9).")