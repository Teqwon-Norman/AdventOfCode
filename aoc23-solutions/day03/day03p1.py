import sys

def main():
    s = ''

    for line in sys.stdin:
        for i in line:
            if i.isdigit():
                s += i
            else:
                if s: print(s)
                s = ''
 
if __name__ == '__main__':
    main()