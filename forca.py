def jogar():
    print("*********************************")
    print("** Bem vindo ao jogo da Forca! **")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        print("jogando...")

        chute = input("Qual letra? ")
        chute = chute.strip()

        for letra in palavra_secreta:
            if letra.upper() == chute.upper():
                print(chute)

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()