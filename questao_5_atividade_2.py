from spellchecker import SpellChecker

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

lista_texto = [None] * 25
frase_descobertas = []


def decriptar_cesar(texto, alfabeto):
    texto_decriptado = ''
    for i in range(25):
        for letra in texto:
            if letra != ' ':
                cifra = (alfabeto.index(letra) - i) % 26
                texto_decriptado += alfabeto[cifra].upper()
            else:
                texto_decriptado += ' '
        lista_texto[i] = texto_decriptado
        texto_decriptado = ''

    return lista_texto


texto_decriptado = input("Digite um texto para ser decriptado: ")
texto_decriptado_formatado = texto_decriptado.lower()

texto_decriptado = decriptar_cesar(texto_decriptado_formatado, alfabeto)

for texto in texto_decriptado:

    # Cria um corretor ortográfico
    spell = SpellChecker()

    # Dividindo a frase em palavras
    palavras = texto.split()

    # Selecionando a primeira palavra
    primeira_palavra = palavras[0]
    if primeira_palavra in spell:
        frase_descobertas.append(texto)

for frase in frase_descobertas:
    print(frase)
