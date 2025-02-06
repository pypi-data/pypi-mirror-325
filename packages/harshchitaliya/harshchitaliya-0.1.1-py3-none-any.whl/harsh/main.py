# main.py

def reverse_text(text: str) -> str:
    """
    Reverses the given text.
    
    Args:
        text (str): The text to reverse.
    
    Returns:
        str: The reversed text.
    """
    return text[::-1]


def word_count(text: str) -> int:
    """
    Counts the number of words in the given text.
    
    Args:
        text (str): The text to analyze.
    
    Returns:
        int: The word count.
    """
    return len(text.split())


def unique_words(text: str) -> set:
    """
    Finds the unique words in the given text.
    
    Args:
        text (str): The text to analyze.
    
    Returns:
        set: A set of unique words.
    """
    return set(text.split())
