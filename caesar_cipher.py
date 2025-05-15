def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Main Program
if __name__ == "__main__":
    print("=== Caesar Cipher Tool ===")
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g., 3): "))

    if choice == 'e':
        encrypted = encrypt(message, shift)
        print("Encrypted message:", encrypted)
    elif choice == 'd':
        decrypted = decrypt(message, shift)
        print("Decrypted message:", decrypted)
    else:
        print("Invalid choice. Use 'e' or 'd'.")
