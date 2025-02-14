# libraries used
import random

# this class generates a random word from our 500 word txt file
class Generator:
    def __init__(self, filename="words.txt"):
        try:
            with open(filename, "r") as file:
                # reads the words from the txt file and removes all white spaces for each line in the txt file
                self.words = [line.strip() for line in file.readlines()]

            for word in self.words:
                if len(word) != 5:
                    raise ValueError(f"Invalid word length: {word}. Ensure all words are 5 letters")

        except FileNotFoundError:
            raise FileNotFoundError(f"File: '{filename}' not found")
        except Exception as e:
            raise Exception(f"Something went wrong when reading the file: {e}")

    def generate_word(self):
        return random.choice(self.words)