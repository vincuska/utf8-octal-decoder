import os

decoded_filename = "decoded.txt"

replacements = [
    '\\x41', 'A' , '\\x42', 'B' , '\\x43', 'C' , '\\x44', 'D' , '\\x45', 'E' , '\\x46', 'F' ,
    '\\x47', 'G' , '\\x48', 'H' , '\\x49', 'I' , '\\x4a', 'J' , '\\x4b', 'K' , '\\x4c', 'L' ,
    '\\x4d', 'M' , '\\x4e', 'N' , '\\x4f', 'O' , '\\x4A', 'J' , '\\x4B', 'K' , '\\x4C', 'L' ,
    '\\x4D', 'M' , '\\x4E', 'N' , '\\x4F', 'O' , '\\x50', 'P' , '\\x51', 'Q' , '\\x52', 'R' ,
    '\\x53', 'S' , '\\x54', 'T' , '\\x55', 'U' , '\\x56', 'V' , '\\x57', 'W' , '\\x58', 'X' ,
    '\\x59', 'Y' , '\\x5a', 'Z' , '\\x5A', 'Z' , '\\x61', 'a' , '\\x62', 'b' , '\\x63', 'c' ,
    '\\x64', 'd' , '\\x65', 'e' , '\\x66', 'f' , '\\x67', 'g' , '\\x68', 'h' , '\\x69', 'i' ,
    '\\x6a', 'j' , '\\x6b', 'k' , '\\x6c', 'l' , '\\x6d', 'm' , '\\x6e', 'n' , '\\x6f', 'o' ,
    '\\x6A', 'j' , '\\x6B', 'k' , '\\x6C', 'l' , '\\x6D', 'm' , '\\x6E', 'n' , '\\x6F', 'o' ,
    '\\x70', 'p' , '\\x71', 'q' , '\\x72', 'r' , '\\x73', 's' , '\\x74', 't' , '\\x75', 'u' ,
    '\\x76', 'v' , '\\x77', 'w' , '\\x78', 'x' , '\\x79', 'y' , '\\x7a', 'z' , '\\x7A', 'z' ,
    '\\x40', '@' , '\\x5b', '[' , '\\x5d', ']' , '\\x5e', '^' , '\\x5f', '_' , '\\x60', '`' ,
    '\\x7b', '{' , '\\x7d', '}' , '\\x7c', '|' , '\\x7e', '~' , '\\x5B', '[' , '\\x5d', ']' ,
    '\\x5e', '^' , '\\x5f', '_' , '\\x60', '`' , '\\x7b', '{' , '\\x7d', '}' , '\\x7c', '|' ,
    '\\x7e', '~' , '\\x5B', '[' , '\\x5D', ']' , '\\x5E', '^' , '\\x5F', '_' , '\\x60', '`' ,
    '\\x7B', '{' , '\\x7D', '}' , '\\x7C', '|' , '\\x7E', '~' , '\\x20', ' ' , '\\x21', '!' ,
    '\\x22', '"' , '\\x23', '#' , '\\x24', '$' , '\\x25', '%' , '\\x26', '&' , '\\x27', "'" ,
    '\\x28', '(' , '\\x29', ')' , '\\x2a', '*' , '\\x2b', '+' , '\\x2c', ',' , '\\x2d', '-' ,
    '\\x2e', '.' , '\\x2f', '/' , '\\x3a', ':' , '\\x3b', ';' , '\\x3c', '<' , '\\x3d', '=' ,
    '\\x3e', '>' , '\\x3f', '?' , '\\x2A', '*' , '\\x2B', '+' , '\\x2C', ',' , '\\x2D', '-' ,
    '\\x2E', '.' , '\\x2F', '/' , '\\x3A', ':' , '\\x3B', ';' , '\\x3C', '<' , '\\x3D', '=' ,
    '\\x3E', '>' , '\\x3F', '?' , '\\x4f', 'O' , '\\x4F', 'O' , '\\x30', '0' , '\\x31', '1' ,
    '\\x32', '2' , '\\x33', '3' , '\\x34', '4' , '\\x35', '5' , '\\x36', '6' , '\\x37', '7' ,
    '\\x38', '8' , '\\x39', '9' , '\\x5c', '\\', '\\x5C', '\\', '\\'   , ''
]

while True:
    try:
        filename = input("File name (only .txt): ")
        if filename.strip():
            if filename.endswith(".txt"):
                with open(filename, 'r') as file:
                    filedata = file.read()
                    if len(filedata) == 0:
                        print("\nFile empty!\n")
                    else:
                        break
            else:
                print("\nFile name not ending with .txt!\n")
        else:
            print("\nInput needed!\n")
    except KeyboardInterrupt:
        print("\nBye!\n")
        break
    except FileNotFoundError:
        print("\nFile not found!\n")


def replace_in_file(filedata, replacements, decoded_filename):
    if len(replacements) % 2 != 0:
        raise ValueError("The replacements list must have an even number of elements")

    x = 0
    for item in replacements:
        try:
            filedata = filedata.replace(replacements[x], replacements[x + 1])
            x += 2
        except IndexError:
            break
        with open(decoded_filename, 'w') as file:
            file.write(filedata)
        print(f"\nDecoded and saved to {os.path.abspath(decoded_filename)}")

    return filedata


if __name__ == "__main__":
    replace_in_file(filedata, replacements, decoded_filename)