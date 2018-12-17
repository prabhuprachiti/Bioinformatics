#!/usr/bin/python
import sys

def isPal (string):
    rev = string[::-1]
    
    if string == rev:
        print "The input is a palindrome"
    else:
        print "The input is not a palindrome"


def main():
    seq = sys.argv[1]
    isPal (seq)


if __name__ == "__main__":
    main()
