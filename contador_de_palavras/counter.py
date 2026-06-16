# Program to count words in a text file

# 1. Ask the user for a text file path

# 2. Read the file contents

# 3. Split the text into words (all converted to lowercase)

# 4. Count the total number of words

# 5. Display the 10 most frequent words in a user-friendly format

from collections import Counter
import re

file_path = input("Enter the path of the text file: ")

try:
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
except FileNotFoundError:
    print("The specified file does not exist.")
    exit(1)

# Convert the text to lowercase before extracting words,
# so different cases ("The", "the") are treated as the same word.
words = re.findall(r"\b\w+\b", text.lower())
word_count = len(words)
print(f"Total words: {word_count}")

# Use Counter to efficiently count word frequencies.
word_freq = Counter(words)

# Get the 10 most common words and their counts.
most_frequent_words = word_freq.most_common(10)

print("\n10 most frequent words:")
for idx, (word, freq) in enumerate(most_frequent_words, start=1):
    print(f"{idx}. {word} - {freq} times")
