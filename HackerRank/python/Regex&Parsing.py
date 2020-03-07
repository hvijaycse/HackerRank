# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    String = input()
    last = String[0]
    for character in String[1:]:
        if character == last and character.isalnum():
            print(character)
            exit(0)
        last = character
    print('-1')