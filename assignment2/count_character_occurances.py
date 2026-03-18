"""
Write a function key_value(sentence) that takes a sentence as input and returns a dictionary
showing how many times each character (excluding spaces) occurs.
"""

def key_value(sentence):
    character_count = {}
    for char in sentence:
        if char != " ":
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1


    return character_count


# Example usage:
sentence = "hello world"
result = key_value(sentence)
print(result)  # Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}