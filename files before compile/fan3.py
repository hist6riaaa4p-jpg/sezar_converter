lat_alphabet_1 = {
    'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5', 'F': '6', 'G': '7', 'H': '8', 'I': '9', 'J': '10',
    'K': '11', 'L': '12', 'M': '13', 'N': '14', 'O': '15', 'P': '16', 'Q': '17', 'R': '18', 'S': '19', 'T': '20',
    'U': '21', 'V': '22', 'W': '23', 'X': '24', 'Y': '25', 'Z': '26'
}

lat_alphabet_2 = {
    '1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F', '7': 'G', '8': 'H', '9': 'I', '10': 'J',
    '11': 'K', '12': 'L', '13': 'M', '14': 'N', '15': 'O', '16': 'P', '17': 'Q', '18': 'R', '19': 'S', '20': 'T',
    '21': 'U', '22': 'V', '23': 'W', '24': 'X', '25': 'Y', '26': 'Z'
}

def choose_mode():
    mode = input("Choose mode (1 for encryption, 2 for decryption): ")
    if mode not in ['1', '2']:
        print("Invalid mode. Please enter 1 or 2.")
        return choose_mode()
    return int(mode)

def key_input():
    key = input('Enter the key (1-26): ')
    if not key.isdigit():
        print("Invalid key. Please enter a number between 1 and 26.")
        return key_input()
    key = int(key)
    if not 1 <= key <= 26:
        print("Invalid key. Please enter a number between 1 and 26.")
        return key_input()
    return key

def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.upper() in lat_alphabet_1:
            num = int(lat_alphabet_1[char.upper()])
            new_num = (num + key - 1) % 26 + 1
            encrypted_char = lat_alphabet_2[str(new_num)]
            if char.islower():
                encrypted_char = encrypted_char.lower()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.upper() in lat_alphabet_1:
            num = int(lat_alphabet_1[char.upper()])
            new_num = (num - key - 1) % 26 + 1
            decrypted_char = lat_alphabet_2[str(new_num)]
            if char.islower():
                decrypted_char = decrypted_char.lower()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    mode = choose_mode()
    key = key_input()
    text = input("Enter the text: ")

    if mode == 1:
        result = encrypt(text, key)
        print("Result:", result)
    else:
        result = decrypt(text, key)
        print("Result:", result)

if __name__ == "__main__":
    main()