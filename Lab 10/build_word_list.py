"""
SYSC 1005 A Fall 2017
Case study: iterative, incremental development of a function that uses
Python's str, list, and set types.
"""
import string

# For information about the string module, type help(string) at the shell 
# prompt, or browse the Library Reference, Section 6.1, in the Python 3.5.2 
# documentation (available @ python.org).


def build_word_list(filename):
    """ (str) -> list of str
    
    Return a list of all the distinct words in the specified file,
    sorted in ascending order.
    
    >>> word_list = build_word_list('sons_of_martha.txt')
    >>> word_list
    ['a', 'afar', 'afraid', 'again', 'against', 'ages', 'all', 'allows', 'already', 'altars', 'and', 'angels', 'any', 'are', 'as', 'at', 'bare', 'be', 'because', 'bed', 'before', 'behind', 'belief', 'birth', 'black', 'blessed', 'blood', 'bother', "brethren's", 'buffet', 'burden', 'but', 'by', 'care', 'careful', 'cast', 'choose', 'city', 'clear', 'cleave', 'common', 'concerned', 'confessed', 'creed', 'cup', 'cushion', 'damn-well', 'dark', 'dawn', 'days', 'death', 'deep', 'deliver', 'desert', 'do', 'drouth', 'dry', 'duly', 'early', 'earth', 'earthline', 'embark', 'end', 'engages', 'entrain', 'ere', 'evenfall', 'fair', 'favour', 'feed', 'feet', 'finger', 'fires', 'flat', 'floods', 'follow', 'for', 'forbidden', 'forth', 'fountains', 'from', 'gates', 'gather', 'gear', 'given', 'gloves', 'goad', 'god', 'good', 'grace', 'guest', 'hale', 'haltered', 'have', 'he', 'hear', 'heart', 'heaven', 'her', 'hidden', 'high', 'hill-tops', 'him', 'his', 'how', 'hungry', 'in', 'inherited', 'into', 'is', 'it', 'kind', 'know', 'ladder', 'laid', 'land', 'lays', 'leave', 'lesser', 'lighted', 'like', 'little', 'living', 'lo', 'lock', 'long', 'loose', 'lord', 'lost', 'main', 'make', 'martha', "martha's", 'mary', "mary's", 'matter', 'may', 'men', 'mercies', 'more', 'mother', 'mountains', 'mouth', 'multiplied', 'must', 'need', 'not', 'nuts', 'of', 'on', 'once', 'or', 'overcome', 'own', 'part', 'path', 'piece', 'pity', 'pleasantly', 'pour', 'preach', 'promise', 'raise', 'rears', 'relief', 'removed', 'repiece', 'reprieve', 'reproved', 'rest', 'restore', 'rocks', 'rods', 'rouse', 'rude', 'run', 'runs', 'say', 'secret', 'see', 'seldom', 'service', 'shake', 'she', 'shock', 'side', 'simple', 'simply', 'sit', 'sleeping', 'smile', 'so', 'some', 'son', 'sons', 'soul', 'spilled', 'stall', 'stand', 'steer', 'stone', 'stumble', 'summit', 'switches', 'take', 'tally', 'teach', 'temper', 'tend', 'terrible', 'that', 'the', 'their', 'them', 'then', 'these', 'they', 'thronged', 'till', 'to', 'transport', 'troubled', 'truly', 'turn', 'unaware', 'under', 'up', 'upon', 'wait', 'wary', 'was', 'watchful', 'waters', 'ways', 'wheels', 'when', 'where', 'which', 'will', 'wires', 'with', 'withdrawn', 'without', 'witness', 'wood', 'word', 'work', 'world', 'ye']
    >>> len(word_list)  # How many different words are in the file?
    249
    """
    
    infile = open(filename, "r")
    word_set = set()

    for line in infile:

        # Split each line into a list of words.
        # By default, the split method removes all whitespace; e.g.,
        # '  Hello,    world!   '.split() returns this list:
        #
        # ['Hello,', 'world!']
        #
        # and not:
        #
        # ['  Hello,', '    world!   ']
        #
        # Notice that the punctuation marks have not been removed.
        
        word_list = line.split()

        # For each word, first remove any leading or trailing punctuation,
        # then convert the the word to lower case.
        #
        # Examples: 
        #  'Hello,'.strip(string.punctuation) returns 'Hello'.
        #  'Hello'.lower() returns 'hello'.
        
        for word in word_list:
            word = word.strip(string.punctuation).lower()
            
            # This statement is equivalent to: 
            # word = word.strip(string.punctuation)
            # word = word.lower()

            # Don't save any empty strings that were created when the 
            # punctuation marks were removed.
            # For example, if word is bound to a hyphen, '-',
            # word.strip(string.punctuation) yields the empty string, ''.
            
            if word != '':
                # Storing the words in a set discards any duplicates.
                word_set.add(word)

    # Now build the list of distinct words.  
    word_list = list(word_set)
    
    # or,
    # word_list = []
    # for word in word_set:
    #    word_list.append(word)

    # Sort the list into ascending order.
    word_list.sort()
    
    return word_list
