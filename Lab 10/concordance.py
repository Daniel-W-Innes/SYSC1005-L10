import string
from tkinter import *
import tkinter.filedialog


def build_concordance(filename):
    """
    >>> build_concordance('sons_of_martha.txt')
    {'the': [1, 3, 4, 5, 8, 9, 10, 11, 13, 14, 15, 16, 18, 19, 24, 25, 26, 28, 30, 31, 33, 38, 39, 40, 41], 'sons': [1, 3, 4, 6, 38, 41, 11, 16], 'of': [1, 34, 3, 4, 38, 11, 14, 15, 16], 'martha': [1, 34, 4], 'mary': [11, 16, 3, 38], 'seldom': [3], 'bother': [3], 'for': [34, 3, 39], 'they': [3, 38, 39, 40, 41, 13, 14, 18, 19, 20, 24, 28, 29, 30], 'have': [41, 3], 'inherited': [3], 'that': [34, 3, 9, 10, 14, 16, 28, 29, 31], 'good': [3], 'part': [3], 'but': [4, 36], 'favour': [4], 'their': [4, 36, 38, 8, 9, 10, 41, 14, 18, 19, 24, 28, 29, 31], 'mother': [4], 'careful': [4], 'soul': [4], 'and': [4, 5, 38, 39, 8, 41, 10, 11, 16, 18, 21, 26, 30, 31], 'troubled': [4], 'heart': [4], 'because': [5], 'she': [5], 'lost': [5], 'her': [5, 6], 'temper': [5], 'once': [5], 'was': [5], 'rude': [5], 'to': [33, 35, 36, 5, 8, 10, 13, 15, 23, 25, 29], 'lord': [41, 5], 'guest': [5], 'must': [6], 'wait': [6], 'upon': [41, 6], "mary's": [6], 'world': [6], 'without': [6], 'end': [18, 6], 'reprieve': [6], 'or': [33, 6], 'rest': [6], 'it': [34, 8, 9, 10, 41, 16], 'is': [34, 39, 8, 9, 10, 14, 15, 23], 'care': [8, 9, 10], 'in': [36, 39, 8, 26, 30, 31], 'all': [8, 31], 'ages': [8], 'take': [8], 'buffet': [8], 'cushion': [8], 'shock': [8], 'gear': [9], 'engages': [9], 'switches': [9], 'lock': [9], 'wheels': [10], 'run': [10], 'truly': [40, 10], 'embark': [10], 'entrain': [10], 'tally': [11], 'transport': [11], 'deliver': [11], 'duly': [11], 'by': [11], 'land': [11, 31], 'main': [11], 'say': [13], 'mountains': [13], 'be': [13, 31], 'ye': [33, 13], 'removed': [13], 'lesser': [13], 'floods': [26, 13], 'dry': [13], 'under': [24, 14], 'rods': [14], 'are': [24, 38, 14, 39], 'rocks': [14], 'reproved': [14], 'not': [35, 28, 29, 14], 'afraid': [14], 'which': [14], 'high': [14], 'then': [15], 'do': [28, 29, 15], 'hill-tops': [15], 'shake': [15], 'summit': [15], 'bed': [15], 'deep': [15], 'laid': [15], 'bare': [15], 'may': [16, 31], 'overcome': [16], 'pleasantly': [16], 'sleeping': [16], 'unaware': [16], 'finger': [18], 'death': [18, 23], 'at': [40, 18, 26, 20], 'gloves': [18], 'where': [18], 'piece': [18], 'repiece': [18], 'living': [18], 'wires': [18], 'he': [41, 19], 'rears': [19], 'against': [19], 'gates': [19], 'tend': [19], 'feed': [19], 'him': [19, 21], 'hungry': [19], 'behind': [19], 'fires': [19], 'early': [20], 'dawn': [20], 'ere': [20], 'men': [20], 'see': [40, 20], 'clear': [20], 'stumble': [20], 'into': [20], 'his': [20, 29, 36], 'terrible': [20], 'stall': [20], 'hale': [21], 'forth': [21], 'like': [21], 'a': [33, 35, 21, 26, 28], 'haltered': [21], 'steer': [21], 'goad': [21], 'turn': [21], 'till': [21, 23], 'evenfall': [21], 'these': [23], 'from': [35, 23], 'birth': [23], 'belief': [23], 'forbidden': [23], 'relief': [23], 'afar': [23], 'concerned': [24], 'with': [24, 34], 'matter': [24], 'hidden': [24], 'earthline': [24], 'altars': [24], 'secret': [25], 'fountains': [25], 'follow': [25], 'up': [25], 'waters': [25], 'withdrawn': [25], 'restore': [25], 'mouth': [25], 'gather': [26], 'as': [26, 35, 30], 'cup': [26], 'pour': [26], 'them': [26, 28, 29, 39], 'again': [26], 'city': [26], 'drouth': [26], 'preach': [28], 'god': [28], 'will': [28], 'rouse': [28], 'little': [28], 'before': [28], 'nuts': [28], 'work': [28, 29], 'loose': [28], 'teach': [29], 'pity': [29], 'allows': [29], 'leave': [29], 'when': [29], 'damn-well': [29], 'choose': [29], 'thronged': [30], 'lighted': [30], 'ways': [30], 'so': [30], 'dark': [30], 'desert': [30], 'stand': [30], 'wary': [31], 'watchful': [31], 'days': [31], "brethren's": [31], 'long': [31], 'raise': [33], 'stone': [33], 'cleave': [33], 'wood': [33], 'make': [33], 'path': [33], 'more': [33], 'fair': [33], 'flat': [33], 'lo': [34], 'black': [34], 'already': [34], 'blood': [34], 'some': [34], 'son': [34], 'spilled': [34], 'ladder': [35], 'earth': [35], 'heaven': [35], 'witness': [35], 'any': [35], 'creed': [35], 'simple': [36], 'service': [36], 'simply': [36], 'given': [36], 'own': [36], 'kind': [36], 'common': [36], 'need': [36], 'smile': [38], 'blessed': [38], 'know': [38, 39], 'angels': [38], 'on': [41, 38], 'side': [38], 'grace': [39], 'confessed': [39], 'mercies': [39], 'multiplied': [39], 'sit': [40], 'feet': [40], 'hear': [40], 'word': [40], 'how': [40], 'promise': [40], 'runs': [40], 'cast': [41], 'burden': [41], 'lays': [41], "martha's": [41]}
    >>> build_concordance('two_cities.txt')
    {'it': [1, 2], 'was': [1, 2], 'the': [1, 2], 'best': [1], 'of': [1, 2], 'times': [1, 2], 'worst': [2]}

    :param filename:
    :return:
    """
    infile = open(filename, "r")
    concordance = {}
    linenum = 0
    for line in infile:
        linenum = linenum + 1
        word_list = line.split()
        for word in word_list:
            word = word.strip(string.punctuation).lower()
            if word != '':
                count = concordance.get(word, set())
                count.add(linenum)
                concordance[word] = count
    for word in concordance:
        concordance[word] = list(concordance[word])
    return concordance


def output_concordance():
    """
    >>> output_concordance()
    best : [1]
    it : [1, 2]
    of : [1, 2]
    the : [1, 2]
    times : [1, 2]
    was : [1, 2]
    worst : [2]

    :return:
    """
    root = Tk()
    root.withdraw()
    path = tkinter.filedialog.askopenfilename()
    root.destroy()
    concordance = build_concordance(path)
    words = sorted(concordance)
    for word in words:
        print(word + " : " + str(concordance[word]))
