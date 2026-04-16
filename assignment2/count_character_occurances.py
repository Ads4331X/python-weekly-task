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


sentence = input("Enter a Sentence: ")
result = key_value(sentence)
print(result)