def funcao_rotacao(metade, chave):
    return metade ^ chave


def cifra_feistel(texto, chave1, chave2):
    # Dividir o texto em duas metades
    L, R = texto >> 8, texto & 0xFF

    # Primeiro round
    L1 = R
    R1 = L ^ funcao_rotacao(R, chave1)

    # Segundo round
    L2 = R1
    R2 = L1 ^ funcao_rotacao(R1, chave2)

    # Combinar as metades para obter o texto cifrado
    texto_cifrado = (L2 << 8) | R2
    return texto_cifrado


def decifra_feistel(texto_cifrado, chave1, chave2):
    # Dividir o texto cifrado em duas metades
    L2, R2 = texto_cifrado >> 8, texto_cifrado & 0xFF

    # Segundo round
    R1 = L2
    L1 = R2 ^ funcao_rotacao(R1, chave2)

    # Primeiro round
    R = L1
    L = R1 ^ funcao_rotacao(R, chave1)

    # Combinar as metades para obter o texto original
    texto_decifrado = (L << 8) | R
    return texto_decifrado



# Texto original (16 bits, representando dois caracteres)
texto = 0b0100100001100101  # 'He' em binário

# Chaves para os rounds
chave1 = 0b0000111100001111
chave2 = 0b0011001100110011

print("Texto Original: ", bin(texto))

# Criptografar
texto_cifrado = cifra_feistel(texto, chave1, chave2)
print("Texto Cifrado: ", bin(texto_cifrado))

# Descriptografar
texto_decifrado = decifra_feistel(texto_cifrado, chave1, chave2)
print("Texto Decifrado: ", bin(texto_decifrado))


