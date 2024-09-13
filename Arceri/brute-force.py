import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import string

def decrypt_message(encrypted_message, key):
    # Convert the encrypted message from Base64 to bytes
    encrypted_bytes = base64.b64decode(encrypted_message)

    # Create an AES cipher object with the given key
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the message
    decrypted_bytes = decryptor.update(encrypted_bytes) + decryptor.finalize()

    # Convert the decrypted bytes to a string
    decrypted_message = decrypted_bytes.decode('utf-8')

    return decrypted_message

# Define the alphabet (both uppercase and lowercase letters)
alphabet = string.ascii_letters

# Try each possible combination of the first 4 characters of the key
for i in range(26**4):
    possible_key = ''.join(alphabet[(i // (26**j)) % 26] for j in range(4)) + 'IsASecretKey'
    try:
        decrypted_message = decrypt_message('OgJuOYJZT0FDb47DBOkNgA==', possible_key.encode())
        print(f"Possible key: {possible_key}, Decrypted message: {decrypted_message}")
    except ValueError:
        pass
