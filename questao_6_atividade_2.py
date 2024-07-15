import numpy as np


def preprocess_text(text):
    return text.replace(" ", "").upper()


def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text]


def numbers_to_text(numbers):
    return ''.join(chr(num + ord('A')) for num in numbers)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1


def matrix_mod_inverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = mod_inverse(det % modulus, modulus)
    matrix_mod_inv = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    return matrix_mod_inv


def encrypt_block(block, key):
    block_vector = np.array(block).reshape(-1, 1)
    encrypted_vector = np.dot(key, block_vector) % 26
    return encrypted_vector.flatten().tolist()


def decrypt_block(block, key_inverse):
    block_vector = np.array(block).reshape(-1, 1)
    decrypted_vector = np.dot(key_inverse, block_vector) % 26
    return decrypted_vector.flatten().tolist()


def hill_cipher_encrypt(plaintext, key):
    plaintext = preprocess_text(plaintext)
    text_numbers = text_to_numbers(plaintext)

    if len(text_numbers) % 2 != 0:
        text_numbers.append(23)  # Adiciona 'X' para preencher

    ciphertext_numbers = []
    for i in range(0, len(text_numbers), 2):
        block = text_numbers[i:i + 2]
        encrypted_block = encrypt_block(block, key)
        ciphertext_numbers.extend(encrypted_block)

    ciphertext = numbers_to_text(ciphertext_numbers)
    return ciphertext


def hill_cipher_decrypt(ciphertext, key):
    text_numbers = text_to_numbers(ciphertext)

    key_inverse = matrix_mod_inverse(key, 26)

    plaintext_numbers = []
    for i in range(0, len(text_numbers), 2):
        block = text_numbers[i:i + 2]
        decrypted_block = decrypt_block(block, key_inverse)
        plaintext_numbers.extend(decrypted_block)

    plaintext = numbers_to_text(plaintext_numbers)
    return plaintext



key = np.array([[9, 4], [5, 7]])

action = input("Digite 'E' para encriptar ou 'D' para decriptar: ").upper()
message = input("Digite a mensagem: ")

if action == 'E':
    result = hill_cipher_encrypt(message, key)
    print("Texto Cifrado:", result)
elif action == 'D':
    result = hill_cipher_decrypt(message, key)
    print("Texto Decifrado:", result)
else:
    print("Ação inválida. Por favor, digite 'E' para encriptar ou 'D' para decriptar.")



