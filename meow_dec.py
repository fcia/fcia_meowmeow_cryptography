# Meow Meow Decryption Program

# Same unique variant mappings as the encryption program
meow_variants = {
    'a': 'Me00w', 'b': 'Me01w', 'c': 'Me02w', 'd': 'Me03w', 'e': 'Me04w', 'f': 'Me05w',
    'g': 'Me06w', 'h': 'Me07w', 'i': 'Me08w', 'j': 'Me09w', 'k': 'Me10w', 'l': 'Me11w',
    'm': 'Me12w', 'n': 'Me13w', 'o': 'Me14w', 'p': 'Me15w', 'q': 'Me16w', 'r': 'Me17w',
    's': 'Me18w', 't': 'Me19w', 'u': 'Me20w', 'v': 'Me21w', 'w': 'Me22w', 'x': 'Me23w',
    'y': 'Me24w', 'z': 'Me25w',
    'A': 'ME00W', 'B': 'ME01W', 'C': 'ME02W', 'D': 'ME03W', 'E': 'ME04W', 'F': 'ME05W',
    'G': 'ME06W', 'H': 'ME07W', 'I': 'ME08W', 'J': 'ME09W', 'K': 'ME10W', 'L': 'ME11W',
    'M': 'ME12W', 'N': 'ME13W', 'O': 'ME14W', 'P': 'ME15W', 'Q': 'ME16W', 'R': 'ME17W',
    'S': 'ME18W', 'T': 'ME19W', 'U': 'ME20W', 'V': 'ME21W', 'W': 'ME22W', 'X': 'ME23W',
    'Y': 'ME24W', 'Z': 'ME25W',
    '0': 'M3000', '1': 'M3001', '2': 'M3002', '3': 'M3003', '4': 'M3004', '5': 'M3005',
    '6': 'M3006', '7': 'M3007', '8': 'M3008', '9': 'M3009',
    '{': 'Me{00', '}': 'Me}00', '/': 'Me/00', '_': 'Me_00', ' ': 'MeSPC'
}

# Reverse mapping for decryption
reverse_meow_variants = {v: k for k, v in meow_variants.items()}

def meow_meow_decrypt(encrypted_text):
    decrypted = ""
    i = 0
    while i < len(encrypted_text):
        # Match 5-character chunks
        chunk = encrypted_text[i:i+5]
        if chunk in reverse_meow_variants:
            decrypted += reverse_meow_variants[chunk]
        else:
            decrypted += chunk  # If no match found (shouldn't happen)
        i += 5
    return decrypted

# Example usage
encrypted_flag = input("Enter the encrypted flag: ")

# Decrypt the flag
decrypted_flag = meow_meow_decrypt(encrypted_flag)

print(f"Decrypted Flag: {decrypted_flag}")
