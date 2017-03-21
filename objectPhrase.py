#!/usr/bin/env python
"""object of SubjectPhrase, RelatorPhrase, ObjectPhrase"""
class objectPhrase:
    
    def __init__(self, phrase):
        'initialise variables within objectPhrase'
        subj, rel, obj = self.splitObjectPhrase(phrase)
        obj = self.removeTab(obj)
        self.subj = subj
        self.obj = obj
        self.rel = rel

    def splitObjectPhrase(self, parse):
        'objectPhrase -> subject relation object'
        subj = ''
        rel = ''
        obj = ''
        previous = None
        for phrase in parse.split("\n +-- "): # split parse tree by branches
            splice = phrase.split(' ') # split down a branch by ' ' characters
            if (splice[1] == 'VBD' or 'adv' in splice[2]):
                rel += phrase + ' '
            elif ('nsubj' in splice[2]):
                subj += phrase + ' '
            elif ('dobj' in splice[2]):
                obj += phrase + ' '
            elif ('prep' in splice[2]):
                if ('dobj' in previous[2]):
                    obj += '\n' + phrase + ' '
                elif ('nsubj' in splice[2]):
                    subj += '\n' + phrase + ' '
            previous = splice
        return subj, rel, obj

    def removeTab(self, phrase):
        'remove first four characters from each line in phrase'
        phrase = phrase.split('\n')
        phrase = [leaf[4:] if leaf[0] == ' ' else leaf for leaf in phrase]
        phrase = '\n'.join(phrase)
        return phrase
