"""
SYSC 1005 A Fall 2017 - Using a Dictionary to Implement a Histogram
"""
import string

# For information about the string module, type help(string) at the shell 
# prompt, or browse the Library Reference, Section 6.1, in the Python 3.5.2 
# documentation (available @ python.org).

def build_histogram(filename):
    """ (str) -> dict of str, int pairs
    
    Return a histogram of the words in the specified file.
    (A histogram is a set of counters. In this example, each counter
    keeps track of the number of occurrences of one word.)
     
    >>> hist = build_histogram('sons_of_martha.txt')
    >>> hist
    {'the': 42, 'sons': 9, 'of': 10, 'martha': 3, 'mary': 4, 'seldom': 1, 'bother': 1, 'for': 3, 'they': 20, 'have': 2, 'inherited': 1, 'that': 10, 'good': 1, 'part': 1, 'but': 2, 'favour': 1, 'their': 17, 'mother': 1, 'careful': 1, 'soul': 1, 'and': 21, 'troubled': 1, 'heart': 1, 'because': 2, 'she': 2, 'lost': 1, 'her': 3, 'temper': 1, 'once': 1, 'was': 1, 'rude': 1, 'to': 15, 'lord': 3, 'guest': 1, 'must': 1, 'wait': 1, 'upon': 2, "mary's": 1, 'world': 1, 'without': 1, 'end': 2, 'reprieve': 1, 'or': 3, 'rest': 1, 'it': 8, 'is': 11, 'care': 5, 'in': 7, 'all': 2, 'ages': 1, 'take': 1, 'buffet': 1, 'cushion': 1, 'shock': 1, 'gear': 1, 'engages': 1, 'switches': 1, 'lock': 1, 'wheels': 1, 'run': 1, 'truly': 2, 'embark': 1, 'entrain': 1, 'tally': 1, 'transport': 1, 'deliver': 1, 'duly': 1, 'by': 1, 'land': 2, 'main': 1, 'say': 2, 'mountains': 1, 'be': 3, 'ye': 2, 'removed': 1, 'lesser': 1, 'floods': 2, 'dry': 1, 'under': 2, 'rods': 1, 'are': 7, 'rocks': 1, 'reproved': 1, 'not': 5, 'afraid': 1, 'which': 1, 'high': 1, 'then': 2, 'do': 3, 'hill-tops': 1, 'shake': 1, 'summit': 1, 'bed': 1, 'deep': 1, 'laid': 1, 'bare': 1, 'may': 2, 'overcome': 1, 'pleasantly': 1, 'sleeping': 1, 'unaware': 1, 'finger': 1, 'death': 2, 'at': 4, 'gloves': 1, 'where': 1, 'piece': 1, 'repiece': 1, 'living': 1, 'wires': 1, 'he': 2, 'rears': 1, 'against': 1, 'gates': 1, 'tend': 1, 'feed': 1, 'him': 3, 'hungry': 1, 'behind': 1, 'fires': 1, 'early': 1, 'dawn': 1, 'ere': 1, 'men': 1, 'see': 2, 'clear': 1, 'stumble': 1, 'into': 1, 'his': 3, 'terrible': 1, 'stall': 1, 'hale': 1, 'forth': 1, 'like': 1, 'a': 7, 'haltered': 1, 'steer': 1, 'goad': 1, 'turn': 1, 'till': 2, 'evenfall': 1, 'these': 2, 'from': 3, 'birth': 1, 'belief': 1, 'forbidden': 1, 'relief': 1, 'afar': 1, 'concerned': 1, 'with': 2, 'matter': 1, 'hidden': 1, 'earthline': 1, 'altars': 1, 'secret': 1, 'fountains': 1, 'follow': 1, 'up': 1, 'waters': 1, 'withdrawn': 1, 'restore': 1, 'mouth': 1, 'gather': 1, 'as': 4, 'cup': 1, 'pour': 1, 'them': 5, 'again': 1, 'city': 1, 'drouth': 1, 'preach': 1, 'god': 1, 'will': 1, 'rouse': 1, 'little': 1, 'before': 1, 'nuts': 1, 'work': 2, 'loose': 1, 'teach': 1, 'pity': 1, 'allows': 1, 'leave': 1, 'when': 1, 'damn-well': 1, 'choose': 1, 'thronged': 1, 'lighted': 1, 'ways': 1, 'so': 1, 'dark': 1, 'desert': 1, 'stand': 1, 'wary': 1, 'watchful': 1, 'days': 2, "brethren's": 1, 'long': 1, 'raise': 1, 'stone': 1, 'cleave': 1, 'wood': 1, 'make': 1, 'path': 1, 'more': 1, 'fair': 1, 'flat': 1, 'lo': 1, 'black': 1, 'already': 1, 'blood': 1, 'some': 1, 'son': 1, 'spilled': 1, 'ladder': 1, 'earth': 1, 'heaven': 1, 'witness': 1, 'any': 1, 'creed': 1, 'simple': 1, 'service': 1, 'simply': 1, 'given': 1, 'own': 1, 'kind': 1, 'common': 1, 'need': 1, 'smile': 1, 'blessed': 1, 'know': 2, 'angels': 1, 'on': 2, 'side': 1, 'grace': 1, 'confessed': 1, 'mercies': 1, 'multiplied': 1, 'sit': 1, 'feet': 1, 'hear': 1, 'word': 1, 'how': 1, 'promise': 1, 'runs': 1, 'cast': 1, 'burden': 1, 'lays': 1, "martha's": 1}
    >>> len(hist)  # How many different words are in the file?
    249
    >>> most_frequent_word(hist)  # Which word occurs most often?
    ('the', 42)
    >>> hist = build_histogram('two_cities.txt')
    >>> hist
    {'it': 2, 'was': 2, 'the': 2, 'best': 1, 'of': 2, 'times': 2, 'worst': 1}
    >>> len(hist)  # How many different words are in the file?
    7
    >>> most_frequent_word(hist)  # Which word occurs most often?
    ('it', 2)
    """

    infile = open(filename, "r")
    hist = {}

    for line in infile:

        # Split each line into a list of words.
        # The split method removes the whitespace from around each word.
        word_list = line.split()

        # For each word, remove any punctuation marks immediately
        # before and after the word, then convert it to lower case.
        
        for word in word_list:
            word = word.strip(string.punctuation).lower()
            
            # or, 
            # word = word.strip(string.punctuation)
            # word = word.lower()

            # Don't count any empty strings created when the punctuation marks
            # are removed. For example, if word is bound to a hyphen, '-',
            # word.strip(string.punctuation) yields the empty string, ''.
            
            if word != '':
                count = hist.get(word, 0)  # get returns the current count of
                                           # the number of occurrences of word, 
                                           # or 0 if word is not yet in the 
                                           # dictionary.
                hist[word] = count + 1

            # or simply,
            # hist[word] = hist.get(word, 0) + 1

    return hist


def most_frequent_word(hist):
    """ (dict of str, int pairs) -> tuple of str, int
    
    Return a tuple containing the most frequently occurring word in the 
    specified histogram (a dictionary of word/frequency pairs), along with its 
    frequency.
    
    >>> hist = build_histogram('sons_of_martha.txt')
    >>> hist
    >>> len(hist)  # How many different words are in the file?
    >>> most_frequent_word(hist)  # Which word occurs most often?    
    """
    max_frequency = -1
    for word in hist:
        if hist[word] > max_frequency:
            max_frequency = hist[word]
            most_frequent = word
    
    return (most_frequent, max_frequency)


def words_with_frequency(hist, n):
    """
    >>> hist = build_histogram('sons_of_martha.txt')
    >>> words_with_frequency(hist,1)
    ['afar', 'afraid', 'again', 'against', 'ages', 'allows', 'already', 'altars', 'angels', 'any', 'bare', 'bed', 'before', 'behind', 'belief', 'birth', 'black', 'blessed', 'blood', 'bother', "brethren's", 'buffet', 'burden', 'by', 'careful', 'cast', 'choose', 'city', 'clear', 'cleave', 'common', 'concerned', 'confessed', 'creed', 'cup', 'cushion', 'damn-well', 'dark', 'dawn', 'deep', 'deliver', 'desert', 'drouth', 'dry', 'duly', 'early', 'earth', 'earthline', 'embark', 'engages', 'entrain', 'ere', 'evenfall', 'fair', 'favour', 'feed', 'feet', 'finger', 'fires', 'flat', 'follow', 'forbidden', 'forth', 'fountains', 'gates', 'gather', 'gear', 'given', 'gloves', 'goad', 'god', 'good', 'grace', 'guest', 'hale', 'haltered', 'hear', 'heart', 'heaven', 'hidden', 'high', 'hill-tops', 'how', 'hungry', 'inherited', 'into', 'kind', 'ladder', 'laid', 'lays', 'leave', 'lesser', 'lighted', 'like', 'little', 'living', 'lo', 'lock', 'long', 'loose', 'lost', 'main', 'make', "martha's", "mary's", 'matter', 'men', 'mercies', 'more', 'mother', 'mountains', 'mouth', 'multiplied', 'must', 'need', 'nuts', 'once', 'overcome', 'own', 'part', 'path', 'piece', 'pity', 'pleasantly', 'pour', 'preach', 'promise', 'raise', 'rears', 'relief', 'removed', 'repiece', 'reprieve', 'reproved', 'rest', 'restore', 'rocks', 'rods', 'rouse', 'rude', 'run', 'runs', 'secret', 'seldom', 'service', 'shake', 'shock', 'side', 'simple', 'simply', 'sit', 'sleeping', 'smile', 'so', 'some', 'son', 'soul', 'spilled', 'stall', 'stand', 'steer', 'stone', 'stumble', 'summit', 'switches', 'take', 'tally', 'teach', 'temper', 'tend', 'terrible', 'thronged', 'transport', 'troubled', 'turn', 'unaware', 'up', 'wait', 'wary', 'was', 'watchful', 'waters', 'ways', 'wheels', 'when', 'where', 'which', 'will', 'wires', 'withdrawn', 'without', 'witness', 'wood', 'word', 'world']
    >>> words_with_frequency(hist, 5)
    ['care', 'not', 'them']

    >>> hist = build_histogram('two_cities.txt')
    >>> words_with_frequency(hist, 1)
    ['best', 'worst']
    >>> words_with_frequency(hist, 2)
    ['it', 'of', 'the', 'times', 'was']

    :param hist:
    :param n:
    :return:
    """
    output = []
    for word in hist:
        if hist[word] == n:
            output.append(word)
    output.sort()
    return output
