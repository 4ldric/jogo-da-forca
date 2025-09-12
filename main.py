import random

def sortear_palavra(palavras):
    return random.choice(palavras)

def codificar_palavra(palavra_secreta):
    palavra_codificada = []
    for letra in palavra_secreta:
        palavra_codificada.append("*")
    return palavra_codificada

def exibir_status(palavra_codificada, palpites):
    print("\n == status ==")
    print(f"\nPalavra secreta: {" ".join(palavra_codificada)}")
    print(f"Palavras ja utilizadas: {" ".join(palpites)}")

def jogar_forca():
    palavras = ["fortaleza", "marrocos", "guarana", "brasil"]
    palavra_secreta = sortear_palavra(palavras)
    palavra_codificada = codificar_palavra(palavra_secreta)
    palpites = []