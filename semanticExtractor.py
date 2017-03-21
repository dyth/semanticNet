#!/usr/bin/env python
"""from English sentences, use denotational semantics parser, then extract relations"""
import os, subprocess
from objectPhrase import objectPhrase
from subprocess import Popen, PIPE


def getParseTree(sentence):
    'return string of parse tree of sentence'
    cmd = "echo " + sentence + " | docker run --rm -i brianlow/syntaxnet"
    pipe = subprocess.Popen(cmd, shell=True, stdout=PIPE).stdout
    output = pipe.read()
    return output.split("Parse:")[1]


def trimDown(word):
    'return the word in the sentence'
    index = 0
    for c in word:
        if (c == '+--' or c == '' or c == '|'):
           pass
        else:
           return c


# get parse tree from Parsey McParseFace
parse = getParseTree("Marvellously, I suddenly saw the man with glasses and with hair who bought the cute rabbit")[1:][:-1]

print parse

sentence = objectPhrase(parse)

print '\n' + sentence.subj
print '\n' + sentence.rel
print '\n' + sentence.obj

quit()






# split up parse tree into nested list and do analysis
# read is an array containing indexes of all branches which have been read
read = []
phrases = parse.split('\n')[1:][:-1]
parts = [word.split(' ') for word in phrases]
for i in range(len(phrases)):
    if "nsubj" in phrases[i]:
        subj = parts[i]
        read.append(i)
    elif "dobj" in phrases[i]:
        obj = parts[i]
        read.append(i)
    elif "VB" in phrases[i]:
        verb = parts[i]
        read.append(i)

# print out a relation
print trimDown(subj), trimDown(verb), trimDown(obj)

print parse
print phrases
print read

sentence = objectPhrase();
print sentence
