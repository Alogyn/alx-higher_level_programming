#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    for i in sys.argv:
        if i != sys.argv[0]:
            result = result + int(i)
    print(result)
