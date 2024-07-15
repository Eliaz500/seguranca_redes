import numpy as np


def preprocess_text(text):
    return text.replace(" ", "").upper()


def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text]


def numbers_to_text(numbers):
    return ''.join(chr(num + ord('A')) for num in numbers)


def encrypt_block(block, key):
    block_vector = np.array(block).reshape(-1, 1)
    encrypted_vector = np.dot(key, block_vector) % 26
    return encrypted_vector.flatten().tolist()


def hill_cipher_encrypt(plaintext, key):
    # Preprocessar o texto
    plaintext = preprocess_text(plaintext)
    text_numbers = text_to_numbers(plaintext)

    # Adicionar padding se o tamanho não for múltiplo de 2
    if len(text_numbers) % 2 != 0:
        text_numbers.append(23)  # Adiciona 'X' (23) para preencher

    ciphertext_numbers = []
    for i in range(0, len(text_numbers), 2):
        block = text_numbers[i:i + 2]
        encrypted_block = encrypt_block(block, key)
        ciphertext_numbers.extend(encrypted_block)

    ciphertext = numbers_to_text(ciphertext_numbers)
    return ciphertext


# Matriz de chave
key = np.array([[9, 4], [5, 7]])

# Mensagem original
plaintext = "meet me at the usual place at ten rather than eight oclock"

# Criptografar
ciphertext = hill_cipher_encrypt(plaintext, key)
print("Texto Cifrado:", ciphertext)
