import random
import string

def gerar_senha(palavras, qtd_letras_maiusculas, qtd_caracteres_especiais, qtd_caracteres):
    # Seleciona aleatoriamente palavras da lista
    nova_palavra = "".join(random.sample(palavras, len(palavras)))
    
    # Reduz a palavra gerada para o tamanho desejado
    if len(nova_palavra) > qtd_caracteres:
        nova_palavra = nova_palavra[:qtd_caracteres]
    
    # Transforma aleatoriamente letras em maiúsculas
    indices = random.sample(range(len(nova_palavra)), qtd_letras_maiusculas)
    nova_palavra = "".join([nova_palavra[i].upper() if i in indices else nova_palavra[i] for i in range(len(nova_palavra))])
    
    # Adiciona caracteres especiais aleatoriamente
    for i in range(qtd_caracteres_especiais):
        indice = random.randint(0, len(nova_palavra) - 1)
        nova_palavra = nova_palavra[:indice] + random.choice(string.punctuation) + nova_palavra[indice:]

    # Adiciona caracteres aleatórios até atingir a quantidade desejada
    nova_palavra += ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=qtd_caracteres - len(nova_palavra)))

    return nova_palavra

# Lista pré-definida de palavras
palavras = ["absorver", "bolacha", "carro", "dedo", "escuro", "festa", "gato", "hotel", "iludir", "janela", "karatê", "laranja", "música", "navio", "óculos", "pipoca", "quarto", "receita", "sapato", "tatuagem", "uva", "vaca", "xadrez", "yoga", "zebra", "ajuste", "branco", "caminhão", "decoração", "encontro", "fácil", "girassol", "história", "internet", "joelho", "lanterna", "mangueira", "neve", "ouro", "passarinho", "queijo", "rosto", "sapateiro", "telefone", "universo", "vela", "xadrezado", "youtuber", "zelador", "armário", "beijo", "computador", "doce", "escola", "faca", "gelo", "hélice", "irmão", "jardim", "lâmpada", "mala", "noite", "orelha", "prato", "quente", "respiração", "sol", "tapete", "uísque", "vampiro", "xícara", "yakissoba", "zumbi", "amarelo", "beleza", "casa", "dinheiro", "elefante", "floresta", "garfo", "hotelaria", "imaginação", "joaninha", "labirinto", "mangá", "noz", "olho", "praia", "queimadura", "restaurante", "solitário", "tartaruga", "urso", "vassoura", "xale", "youtubers", "zíper", "aniversário", "banana", "chave", "disco", "escada", "fogueira", "guitarra", "hipopótamo", "igreja", "jogador", "lado", "cinzeiro", "macaco", "nuvem", "outono", "pássaro", "rio", "solteiro", "tigela", "urubu", "ventilador", "xarope", "yogaçarina", "zoólogo", "avião", "borboleta", "camisa", "dedal", "eletricidade", "forno", "hidrante", "impressora", "lar", "máquina", "ninho", "pão", "roupa", "tambor", "urina", "vaso", "xerife", "yogurt", "ziguezague", "alfinete", "bebê", "café", "doença", "eletrônico", "foguete", "garrafa", "hidroavião", "imagem", "jardineiro"]

# Pede ao usuário a quantidade de letras maiúsculas, caracteres especiais e caracteres que deseja na senha
qtd_letras_maiusculas = int(input("Digite a quantidade de letras maiúsculas que deseja na senha: "))
qtd_caracteres_especiais = int(input("Digite a quantidade de caracteres especiais que deseja na senha: "))
qtd_caracteres = int(input("Digite a quantidade de caracteres que deseja na senha: "))

senha = gerar_senha(palavras, qtd_letras_maiusculas, qtd_caracteres_especiais, qtd_caracteres)

print("Senha gerada: ", senha)
