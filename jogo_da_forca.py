
def jogo_da_forca():
    print("Bem-vindo ao Jogo da Forca!")
    
    palavra = "PRODUTO"  
    letras_corretas = []  
    tentativas = 6  
    
    while True:
        palavra_oculta = ''.join([letra if letra in letras_corretas else '-' for letra in palavra])
        print(f"Palavra: {palavra_oculta}")
        print(f"Tentativas restantes: {tentativas}")
        
        if '-' not in palavra_oculta:
            print("Parabéns! Você venceu!")
            break
        
        if tentativas == 0:
            print("Game over! Você perdeu.")
            break
        
       
        letra = input("Digite uma letra: ").upper()
        
       
        if letra in letras_corretas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        
        if letra in palavra:
            letras_corretas.append(letra)
            print("Letra correta!")
        else:
            tentativas -= 1
            print("Letra incorreta!")
    
    print(f"A palavra era: {palavra}")


if __name__ == "__main__":
    jogo_da_forca()
