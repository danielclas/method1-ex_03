"""
Python 2023 Assignment 03
"""

import string

# IMPORTANT: assign the parts of your name and your student ID to these variables!
first_name = "Daniel"
family_name = "Clas"
student_id = "6640404"

auxiliaries = ["be", "am", "are", "is", "was", "were", "being", "been", "can", "cannot", "could", "dare", "dares",
               "dared", "do", "does", "did", "have", "has", "had", "having", "may", "might", "must", "need", "needs",
               "needed", "ought", "shall", "should", "will", "won't", "would"]

determiners = ["the", "a", "an", "this", "that", "these", "those", "my", "your", "his", "her", "its", "our", "few",
               "little", "much", "many", "most", "some", "any", "enough", "all", "both", "half", "either", "neither",
               "each", "every", "other", "another", "such", "what", "rather", "quite"]

prepositions = ["aboard", "about", "above, absent", "across", "cross", "after", "against", "along", "alongside",
                "amid", "among", "apropos", "around", "round", "as", "astride", "at", "atop", "bar", "before",
                "behind", "below", "beneath", "beside", "beneath", "beside", "besides", "between", "beyond", "but",
                "by", "circa", "despite", "spite", "down", "during", "except", "for", "from", "in", "inside", "into",
                "less", "like", "minus", "near", "nearer," "nearest", "notwithstanding", "of", "off", "on", "onto",
                "opposite", "out", "outside", "over", "pace", "past", "per", "plus", "post", "pre", "pro", "qua", "re",
                "sans", "save", "short", "than", "through", "throughout", "till", "to", "toward", "towards", "under",
                "underneath", "unlike", "until", "unto", "up", "upside", "versus", "via", "vice", "vis-à-vis", "with",
                "within", "without", "worth"]


def tokenize_space(sentence):
    """
    Tokenizes a sentence using empty spaces as a delimiter.
    """
    s = []
    tokens = []

    for char in sentence:
        if char != ' ':
            s.append(char)
        else:
            tokens.append(''.join(s))
            s = []

    if(len(s) > 0): tokens.append(''.join(s))
    
    return tokens


def tokenize_smart(sentence):
    """
    Tokenizes the sentence in such a way that words and punctuation end up as separate tokens.
    """
    s = []
    tokens = []
    for char in sentence:
        if char != ' ' and char not in string.punctuation:
            s.append(char)
        else:
            if char in string.punctuation:
                tokens.append(''.join(s))
                s = []
                tokens.append(char)
            elif char == ' ' and len(s) > 0:
                tokens.append(''.join(s))
                s = []

    return tokens


def print_tokens(sentence):
    """
    Splits the sentence into tokens and prints them.
    """
    tokens = tokenize_smart(sentence)
    for token in tokens:
        if token: print(token)


def is_auxiliary(token):
    """
    Checks whether a token is an auxiliary.
    """
    return token.lower() in auxiliaries


def is_determiner(token):
    """
    Checks whether a token is a determiner.
    """
    return token.lower() in determiners


def is_preposition(token):
    """
    Checks whether a token is a preposition.
    """
    return token.lower() in prepositions


def is_subject_pronoun(token):
    """
    Checks whether a token is a subject pronoun.
    """
    return token.lower() in ['i', 'you', 'he', 'she', 'it', 'they', 'we']


def normalize(token):
    """
    Normalizes the token by transforming it to lower case and removing the negation "n't".
    """
    return token.lower().replace("n't", '')


def detect_pos(sentence):
    """
    Disambiguates the part-of-speech tag of the word 'force' in the sentence, using some simple rules.
    """
    tokens = [token for token in tokenize_smart(sentence) if token not in string.punctuation]
    i = 0

    while i < len(tokens):
        if tokens[i] == 'force':
            if i - 1 >= 0:
                if is_determiner(tokens[i - 1]): return 'NOUN'
                if is_preposition(tokens[i - 1]): return 'NOUN'
                if is_subject_pronoun(tokens[i - 1]): return 'VERB'
            if i + 1 < len(tokens):
                if is_determiner(tokens[i + 1]): return 'VERB' 
                if is_auxiliary(tokens[i + 1]): return 'VERB' 
        i += 1

    return "Unknown"


# paste your test code here (will not be tested)
if __name__ == '__main__':
    pass