
import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __repr__(self) -> str:
        return 

    def __init__(self, file):
        "reading the file input and how many words in the file"
        words = open(file)
        self.word = self.parse(words)
        print(f"{len(self.word)} words read")

    def parse(self, words):
        "pulling each word out from each line"
        return [w.strip() for w in words]
    
    def random(self):
        "returns a random word"
        return random.choice(self.word)


    

        

    
    ...
