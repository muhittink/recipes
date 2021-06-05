#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

baseDir = "src/"
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
    readmeFile = baseDir + recipeCategory + "/" + "README.md"
    if os.path.exists(readmeFile):
        with open(readmeFile, "a") as out_file:
            out_file.write(insertString)
    else:
        with open(readmeFile, "a") as out_file:
            out_file.write("# " + recipeCategory + "\n" + insertString)

def insertToFiles():
    filesToInsert = [baseDir + "SUMMARY.md", baseDir + "README.md"]
    insertString = "	- [" + recipeName + "](" + recipeCategory + "/" + recipeFileName + ")"
    categoryString = "- [" + recipeCategory + "](" + str.lower(recipeCategory) + "/README.md)"

    for file in filesToInsert:
        with open(file, "r") as in_file:
            buf = in_file.readlines()

        with open(file) as myfile:
            if recipeCategory + "/" + "README.md)\n" in myfile.read():
                with open(file, "w") as out_file:
                    for line in buf:
                        if line.endswith(recipeCategory + "/" + "README.md)\n"):
                            line = line + insertString + "\n"
                        out_file.write(line)
            else:
                with open(file, "a") as out_file:
                    out_file.write(categoryString + "\n" + insertString + "\n")

def createTemplate():
    categoryDir = baseDir + recipeCategory

    if not os.path.exists(categoryDir):
        os.mkdir(categoryDir)

    if not os.path.exists(baseDir + recipeCategory + "/" + recipeFileName):
        with open(baseDir + recipeCategory + "/" + recipeFileName, 'w') as out:
                out.write(recipeHeader + "\n" + recipeTemplate)
    else:
        print("Existing recipe found! Check manually!")
        exit(1)

def main():
    createTemplate()
    insertToFiles()
    insertToCategoryReadme()

if __name__ == '__main__':
    main()