
from typing import Text


def first_unique(text):
    data = {}
    for char in text:
        data[char] = data.get(char,0) + 1
    
    for key, value in data.items():
        if value == 1:
            return text.index(key)
    return -1


def main():
    text = 'aaabcccdeeef'
    print(first_unique(text))


if __name__ == '__main__':
    print("Hi")
    main()
