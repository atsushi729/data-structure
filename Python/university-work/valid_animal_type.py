import nltk
from nltk.corpus import wordnet

# wordnet is a lexical database for the English language
nltk.download('wordnet')

animals = {"cat", "degree", "dog"}


def is_animal(word):
    for synset in wordnet.synsets(word):
        # Check if the synset belongs to the 'noun.animal' category
        if synset.lexname() == 'noun.animal':
            return True
    return False


# Get the valid animals
valid_animals = {word for word in animals if is_animal(word)}

print(valid_animals)
