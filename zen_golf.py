"""
AI Refactoring: The Zen of Python
Author: Rejoice Ofosuarmah
"""

# ------------------------------------
# Function 1 - Verbose
# ------------------------------------
def sum_even_verbose(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total = total + num
    return total


# Zen Principles:
# Readability counts.
# Simple is better than complex.
def sum_even_pythonic(numbers):
    return sum(num for num in numbers if num % 2 == 0)


# ------------------------------------
# Function 2 - Verbose
# ------------------------------------
def longest_word_verbose(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


# Zen Principles:
# Readability counts.
# There should be one obvious way to do it.
def longest_word_pythonic(words):
    return max(words, key=len, default="")


# ------------------------------------
# Function 3 - Verbose
# ------------------------------------
def filter_positive_verbose(numbers):
    result = []
    for num in numbers:
        if num > 0:
            result.append(num)
    return result


# Zen Principles:
# Beautiful is better than ugly.
# Simple is better than complex.
def filter_positive_pythonic(numbers):
    return [num for num in numbers if num > 0]


# ------------------------------------
# Measurement Functions
# ------------------------------------
def count_characters(code):
    return len(code.replace(" ", "").replace("\n", ""))


def avg_line_length(code):
    lines = [line for line in code.split("\n") if line.strip()]
    return sum(len(line) for line in lines) / len(lines) if lines else 0


# ------------------------------------
# Test Equivalence
# ------------------------------------
def test_equivalence():
    numbers = [1, 2, 3, 4, 5, 6]
    words = ["cat", "elephant", "dog", "whale"]
    positives = [-3, -1, 0, 2, 5, -7]

    print("Sum Even:")
    print(sum_even_verbose(numbers))
    print(sum_even_pythonic(numbers))

    print("\nLongest Word:")
    print(longest_word_verbose(words))
    print(longest_word_pythonic(words))

    print("\nPositive Numbers:")
    print(filter_positive_verbose(positives))
    print(filter_positive_pythonic(positives))


if __name__ == "__main__":
    test_equivalence()
