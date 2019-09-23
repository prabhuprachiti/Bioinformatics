#!/usr/bin/python
import sys

def IsSelfComplimentary(string):
    seq_dict = {"A":"T", "T":"A", "G":"C", "C":"G"}

    revComp = "".join(seq_dict[s] for s in string.upper()[::-1])

    if revComp == string.upper():
        print "The sequence is self complementary"

    else:
        print "The sequence is not self complementary"


def main():
    seq = sys.argv[1]
    IsSelfComplimentary(seq)


if __name__ == "__main__":
    main()
