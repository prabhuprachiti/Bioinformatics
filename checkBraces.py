#!/usr/bin/python
import sys

def checkIfBalanced(braces):
    openBraces = ["[","{","("]
    closeBraces = ["]","}",")"]
    dictBraces = dict (zip(openBraces, closeBraces))

    if len(braces) == 0 or braces[0] in closeBraces or braces[-1] in openBraces:
        return False

    stack = []
    
    for b in braces:
        if b in openBraces:
            stack.append(dictBraces[b])

        elif b in closeBraces and b != stack.pop():
            return False

    return not stack
    
if __name__ == '__main__':
    braces = sys.argv[1]
    print checkIfBalanced(braces)
