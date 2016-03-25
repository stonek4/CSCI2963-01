"""
 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter,
    then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags

"""

import fileinput
import re

def convertStrong(line):
    line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
    line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
    return line

def convertEm(line):
    line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
    line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
    return line

def convertH(line):
    line = re.sub(r'###(.*)', r'<h3>\1</h3>', line)
    line = re.sub(r'##(.*)', r'<h2>\1</h2>', line)
    line = re.sub(r'#(.*)', r'<h1>\1</h1>', line)
    return line

def convertB(line):
    line = line[1:]
    line = '<blockquote><p>' + line + '</p>'
    return line

def convertIB(line):
    line = '</blockquote><p>' + line + '</p>'
    return line

in_block = False
for line in fileinput.input():
    line = line.rstrip()
    line = convertStrong(line)
    line = convertEm(line)
    line = convertH(line)
    if line[0] == '>' and in_block == False:
        line = convertB(line)
        in_block = True
    else:
        if in_block == True and line[0] != '>':
            line = convertIB(line)
            in_block = False
        elif in_block == True and line[0] == '>':
            line = '<p>' + line[1:] + '</p>'
        else:
            line =  '<p>' + line + '</p>'
    print line,
