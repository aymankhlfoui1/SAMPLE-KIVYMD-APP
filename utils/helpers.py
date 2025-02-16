def save_words(words):
    with open("words.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(words))

def load_words():
    try:
        with open("words.txt", "r", encoding="utf-8") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []
