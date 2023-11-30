#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1

    # In case 0 argument
    if length == 0:
        print("{} arguments.".format(length))
    # In case 1 argument
    elif length == 1:
        print("{} argument:".format(length))
    # In case more than 1 atguments
    else:
        print("{} arguments:".format(length))
        j = 0
        for i in sys.argv:
            if j != 0:
                print("{}: {}".format(j, i))
            j = j + 1
