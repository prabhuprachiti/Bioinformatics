#!/usr/bin/python

import sys

def printRevComp(string):
    revComp = {"A":"T", "T":"A", "G":"C", "C":"G"}

    reverse_comp = "".join(revComp[s] for s in string[::-1])
    print reverse_comp

        
def main():
    seq = sys.argv[1]
    printRevComp(seq)

if __name__ == "__main__":
    main()
