#A cipher is a method of transforming text in order to keep it secret#
def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    shift = shift if mode == 'encrypt' else -shift
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

if __name__ == "__main__":
    choice = input("Choose action: (e)ncrypt or (d)ecrypt: ").lower()
    text = input("Enter the text: ")
    shift = int(input("Enter shift value: "))
    
    mode = 'encrypt' if choice == 'e' else 'decrypt'
    print(f"Result: {caesar_cipher(text, shift, mode)}")
