def initialiseArray(i):
    return [0 for n in range(i)]

def compileCode(arr, code):
    pointer = 0
    char = 0
    loops = []

    output = ''

    while char < len(code):
        match code[char]:
            case '>':
                pointer += 1
            case '<':
                if pointer > 0:
                    pointer -= 1
                else:
                    print(f"Error in code at position {char+1}")
            case '.':
                output += (chr(arr[pointer]))
            case ',':
                arr[pointer] = ord(input())
            case '+':
                arr[pointer] += 1
            case '-':
                if arr[pointer] > 0:
                    arr[pointer] -= 1
                else:
                    print(f"Error in code at position {char+1}")
            case '[':
                loops.append(char)
            case ']':
                if arr[pointer] != 0:
                    char = loops[-1]
                else:
                    loops.pop()

        #print(f"array: {arr}\npointer: {pointer}\npointer val: {arr[pointer]}\nchar: {char}\nchar val: {code[char]}\nloops list: {loops}\n")
        char += 1

    print(output)

def main():
    arr = initialiseArray(32)
    code = input("Enter code: ")
    compileCode(arr, code)

main()
