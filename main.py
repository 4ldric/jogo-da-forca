
import random

def sortear_palavra(palavras):
    return random.choice(palavras)

def codificar_palavra(palavra_secreta):
    palavra_codificada = []
    for letra in palavra_secreta:
        palavra_codificada.append("_")
    return palavra_codificada

def exibir_status(palavra_codificada, palpites, tentativas):
    print("\n == Jogo da forca ==")
    print(f"\nPalavra secreta: {" ".join(palavra_codificada)}")
    print(f"Palavras ja utilizadas: {" ".join(palpites)}")
    print(f"Tentativas restantes: {tentativas}\n")


def verificar_letra(chute, palpites, palavra_secreta, palavra_codificada, tentativas):
    acertou = False
    if chute not in palpites:
        palpites.append(chute)
        for indice, elemento in enumerate(palavra_secreta):
            if chute == elemento:
                acertou = True
                palavra_codificada[indice] = chute
        if not acertou:
            print("Não possui esta letra na palavra.. -1 tentativa\n")
            tentativas -= 1
            
    else:
        print("letra ja utilizada. -1 tentativa\n")
        tentativas -= 1
    return tentativas

def verificar_palavra(palavra_secreta, palavra_codificada, concluido):
    palavra_codificada = "".join(palavra_codificada)
    if palavra_codificada == palavra_secreta:
        print(f"\nParabens voce descobriu a palavra secreta: ({palavra_secreta})")
        concluido = True
    return concluido

def jogar_forca():
    novo_jogo = False
    while not novo_jogo:
        palavras = ["fortaleza", "marrocos", "guarana", "brasil"]
        palavra_secreta = sortear_palavra(palavras)
        palavra_codificada = codificar_palavra(palavra_secreta)
        palpites = []
        concluido = False
        tentativas = 3
        print(palavra_secreta)

        while tentativas >= 0 and not concluido:
            if tentativas != 0:
                exibir_status(palavra_codificada, palpites, tentativas)
                chute = input("Digite uma letra: ")
                tentativas = verificar_letra(chute, palpites, palavra_secreta, palavra_codificada, tentativas)
                concluido = verificar_palavra(palavra_secreta, palavra_codificada,concluido)
            else:
                print(f"\nQue pena, Voce não conseguiu descobrir a palavra ({palavra_secreta})")
                break
                
        novo_jogo = input("\nVocê deseja iniciar um novo jogo? (s/n): ")
        if novo_jogo != "s":
            novo_jogo = True
            print("Saindo...")
            break
        else:
            jogar_forca()
jogar_forca()
