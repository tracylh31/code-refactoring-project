def process_numbers(numbers):
    """Process numbers by doubling even values and tripling odd values.
    
    Args:
        numbers: A list of numbers to process.
        
    Returns:
        A list containing the processed numbers.
    """
    return [number * 2 if number % 2 == 0 else number * 3 for number in numbers]


def process_strings(strings):
    """Process strings based on their length.
    
    Args:
        strings: A list of strings to process.
        
    Returns:
        A string containing the processed words separated by spaces.
    """
    processed_strings = [
       string.upper() if len(string) > 5 else string.lower()
       for string in strings
   ]
    return " ".join(processed_strings)


def main():
    """Run the program and display the processed numbers and strings."""
    numbers = [1, 2, 3, 4, 5, 6, 7]
    words = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    processed_numbers = process_numbers(numbers)
    processed_strings = process_strings(words)

    print("Processed Numbers:", processed_numbers)
    print("Processed Strings:", processed_strings)


if __name__ == "__main__":
    main()
