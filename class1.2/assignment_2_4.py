#keep the long words
words = ["ai", "python", "ml", "agent", "rag"]
longer_words = [word.upper() for word in words if len(word) > 2]
print(longer_words)
print(f"{len(longer_words)} words kept")