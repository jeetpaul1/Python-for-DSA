#Write a Python program to check if a string of parentheses is balanced. A string is considered balanced if every opening parenthesis has a corresponding closing parenthesis in the correct order.



def is_balanced_parentheses(expression):  #solution
    """
    Check if the given string of parentheses is balanced.

    Args:
        expression (str): The input string containing parentheses.

    Returns:
        bool: True if the parentheses are balanced, False otherwise.
    """
    stack = []
    for char in expression:
        if char in "({[":
            stack.append(char)  # Push opening brackets onto the stack
        elif char in ")}]":
            if not stack:
                return False  # Unmatched closing bracket
            top = stack.pop()
            if not matches(top, char):
                return False  # Mismatched brackets
    return len(stack) == 0  # Stack should be empty if balanced

def matches(opening, closing):
    """
    Check if the opening and closing brackets match.

    Args:
        opening (str): The opening bracket.
        closing (str): The closing bracket.

    Returns:
        bool: True if the brackets match, False otherwise.
    """
    pairs = {"(": ")", "{": "}", "[": "]"}
    return pairs.get(opening) == closing

# Example usage
expression = "{[()()]}"
result = is_balanced_parentheses(expression)
print(f"The expression '{expression}' is balanced: {result}")
