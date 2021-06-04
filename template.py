#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import sys
import subprocess

recipeName = sys.argv[1]
recipeCategory = sys.argv[2]
recipeFileName = recipeName.replace(" ", "") + '.md'
recipeHeader = '# ' + recipeName
recipeTemplate = ('''
...

## Zutaten

- ...
- ...

## Zubereitung

1. ...
1. ...
''')

def insertToCategoryReadme():
    insertString = "- [" + recipeName + "](" + recipeFileName + ")\n"
    readmeFile = "src/" + recipeCategory + "/" + "README.md"
    with open(readmeFile, "a") as out_file:
        out_file.write(insertString)

def insertToFiles():
    filesToInsert = ["src/SUMMARY.md", "src/README.md"]
    insertString = "	- [" + recipeName + "](" + recipeCategory + "/" + recipeFileName + ")"
    for file in filesToInsert:
        with open(file, "r") as in_file:
            buf = in_file.readlines()

        with open(file, "w") as out_file:
            for line in buf:
                if line.endswith(recipeCategory + "/" + "README.md)\n"):
                    line = line + insertString + "\n"
                out_file.write(line)

def createTemplate():
    with open("src/" + recipeCategory + "/" + recipeFileName, 'w') as out:
        out.write(recipeHeader + "\n" + recipeTemplate)

def main():
    createTemplate()
    insertToFiles()
    insertToCategoryReadme()

if __name__ == '__main__':
    main()