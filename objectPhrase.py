#!/usr/bin/env python

class objectPhrase(object):
    """Abstracts SubjectPhrase, RelatorPhrase, ObjectPhrase"""
    
    def __init__(self, subj, rel, obj):
        self.subj = None
        self.obj = None
        self.rel = None
