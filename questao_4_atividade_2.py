

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




def cifra_cesar(texto, chave, alfabeto):
   texto_cifrado = ''
   for letra in texto:
       if letra != ' ':
           cifra = (alfabeto.index(letra) + chave) % 26
           texto_cifrado += alfabeto[cifra].upper()
       else:
           texto_cifrado += ' '
   return texto_cifrado


def decriptar_cesar(texto, chave, alfabeto):
   texto_decriptado = ''
   for letra in texto:
       if letra != ' ':
           cifra = (alfabeto.index(letra) - chave) % 26
           texto_decriptado += alfabeto[cifra].upper()
       else:
           texto_decriptado += ' '
   return texto_decriptado






texto = input("Digite um texto para encriptar: ")
texto_formatado = texto.lower()


texto_decriptado = input("Digite um texto para ser decriptado: ")
texto_decriptado_formatado = texto_decriptado.lower()


chave  = 3


texto_cifrado = cifra_cesar(texto_formatado, chave, alfabeto)
texto_decriptado = decriptar_cesar(texto_decriptado_formatado, chave, alfabeto)


print(texto_cifrado)
print(texto_decriptado)
