# word_frequency.py

def count_word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        word = ''.join(char for char in word if char.isalnum())  # Remove punctuation
        if word:
            freq[word] = freq.get(word, 0) + 1
    return freq

if __name__ == "__main__":
    user_input = input("📝 Enter a paragraph: ")
    frequencies = count_word_frequency(user_input)
    print("\n📊 Word Frequencies:")
    for word, count in sorted(frequencies.items(), key=lambda x: x[1], reverse=True):
        print(f"{word} : {count}")
