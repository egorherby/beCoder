#!/usr/bin/env python3

import sys

def solution(inputString):
    parsed = [e.split() for e in inputString.strip().split("\n")]
    immediateFriends = {e[0] for e in parsed[1:]}
    friendsOfFriends = {item for row in parsed[1:] for item in row[2:]}
    return len(friendsOfFriends - immediateFriends)


def main():

    # ensure proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python solution.py input_file_path")

    # open file and read data, avoid reading errors
    filePath = sys.argv[1]
    try:
        with open(filePath) as f:
            data = f.read()
    except EnvironmentError:
        sys.exit("Probably no such file or directory.")

    # return answer to command line
    print(solution(data))


if __name__ == "__main__":
    main()
