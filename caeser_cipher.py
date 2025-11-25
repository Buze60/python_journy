def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


while True:
    options = input('Enter (E) for encrypt and (D) for decrypt: ')
    if options.upper() == 'E':
        text = input('Enter text to encrypt: ')
    result = encrypt(text,3)
    if options.upper() == 'D':
        text = input('Enter text to decrypt: ')
    result = decrypt(text,3)
    print(result)
