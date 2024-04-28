import sys
import hashlib

def main() -> None:
    data: str = sys.stdin.readline()
    num: int = 0
    
    m = hashlib.md5()
    while m.hexdigest()[:6] != '000000':
        num += 1
        m = hashlib.md5()
        m.update(f'{data}{num}'.encode('ascii'))
    print(data + str(num))

if __name__ == '__main__':
    main()