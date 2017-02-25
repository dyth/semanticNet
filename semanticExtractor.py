#!/usr/bin/env python
"""from English sentences, use denotational semantics parser, then extract relations"""
import os, subprocess
from subprocess import Popen, PIPE


def getParseTree(sentence):
    'return string of parse tree of sentence'
    cmd = "echo " + sentence + " | docker run --rm -i brianlow/syntaxnet"
    pipe = subprocess.Popen(cmd, shell=True, stdout=PIPE).stdout
    output = pipe.read()
    return output.split("Parse:")[1]

    
getParseTree("Please change this sentence")
