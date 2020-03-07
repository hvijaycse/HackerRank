# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    String = input()
    Length = len(String)
    i = 0 
    while i < Length:
        Character = String[i]
        count = 1
        i = i + 1
        while i < Length and String[i] == Character:
            i = i + 1
            count = count + 1
        print( '({0}, {1}) '.format(count, Character), end = '')
