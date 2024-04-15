import sys
from collections import defaultdict

class Node:
    def __init__(self, data: str) -> None:
        self.numbers: dict[str, list[tuple]] = self.find_all_numbers(data)
        self.symbols: dict[str, tuple] = self.find_all_symbols(data)

    def find_all_numbers(self, data: str) -> dict[str, list[tuple[int, ...]]]:
        number: str = ''
        index: tuple[int, ...] = ()

        result: dict[str, list[tuple[int, ...]]] = defaultdict(list)

        for i, val in enumerate(data):
            if val.isdigit():
                number += val
                index += (i, )
            else:
                if number:
                    result[number].append(index)
                    number = ''
                    index = ()
        
        if number:
            result[number].append(index)

        return result

    def find_all_symbols(self, data: str) -> dict[str, tuple[int, ...]]:
        result: dict[str, tuple] = defaultdict(tuple)

        for i, val in enumerate(data):
            if not val.isdigit() and val != '.':
                result[val] += (i, )
        return result

class Line:
    def __init__(self, data: tuple[str, str]) -> None:
        self.curr = Node(data[0])
        self.next = Node(data[1])

class Engine:
    def __init__(self) -> None:
        self.head: list[Line] = []

    def add_part(self, l1: str, l2: str) -> None:
        new_line = Line( (l1, l2) )
        self.head.append(new_line)

def self_compare(
        numbers: dict[str, list[tuple]], 
        symbols: dict[str, tuple],
        next_numbers: dict[str, list[tuple]],
        next_symbols: dict[str, tuple]
    ) -> int:
    
    result: int = 0

    for k, num_v in numbers.items():
        for pair in num_v:
            for _, symb_v in symbols.items():
                for index in symb_v:
                    if any(index + offset in pair for offset in (-1, 0, 1)):
                        print(k)
                        result += int(k)
                            

    for k, num_v in numbers.items():
        for pair in num_v:
            for _, symb_v in next_symbols.items():
                for index in symb_v:
                    if any(index + offset in pair for offset in (-1, 0, 1)):
                        print(k)
                        result += int(k)

    for k, num_v in next_numbers.items():
        for pair in num_v:
            for _, symb_v in symbols.items():
                for index in symb_v:
                    if any(index + offset in pair for offset in (-1, 0, 1)):
                        print(k)
                        result += int(k)

    return result

def main() -> None:
    data = [ line.rstrip() for line in sys.stdin.readlines() ]
    engine = Engine()
    result: int = 0
    

    for i in range(len(data) - 1):
        for j in range(i+1, len(data)):
            engine.add_part(data[i], data[j])
            break
    
    for line in engine.head:
        if not isinstance(line, Line):
            raise TypeError('Invalid type')


        result += self_compare(
            line.curr.numbers, 
            line.curr.symbols,
            line.next.numbers,
            line.next.symbols
        )
    print(result)

        
if __name__ == '__main__':
    main()