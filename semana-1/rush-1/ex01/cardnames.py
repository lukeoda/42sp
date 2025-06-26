def fit(name: str):
    name = remove_prepositions(name)
    name = remove_abr_sufixo(name)
    name = remove_nomes(name)
    return name

def tamanho_nome(name):
    '''recebe name e retorna True se name contem ate 26 caracteres, caso contrario False'''
    return len(name) <= 26

def remove_prepositions(name='Maria do Nacimento da Silva Santos'):
    '''recebe nome e retorna o nome sem preposicoes'''
    if tamanho_nome(name):
        return name
    names = name.split(" ")
    result = []
    for value in names:
            if value not in ["DE", "DO", "DA", "DAS", "DOS"]:
                 result.append(value)
            else:
                continue
    return " ".join(result)

def remove_abr_sufixo(name='Maria do Nacimento da Silva Santos'):
    '''recebe nome e retona nome tratado de acordo com os sufixos'''
    if tamanho_nome(name):
        return name
    names = name.split(" ")
    result = []
    match names[len(names) -1]:
        case "JUNIOR":
            names[len(names) -1] = "JR" 
        case "FILHO":
            names[0] = names[0][:1] 
        case "NETO":
            names[0] = names[0][:1] 
    return " ".join(names)
      
def remove_nomes(name='Gabriel Joao da Silva Jardins Maitê de Paula Junior'):
    '''recebe nome e retona nome com o maior nome abreviado'''
    if tamanho_nome(name):
        return name
    names = name.split(" ")
    
    maior_nome = max(names[1:-1], key=len)

    names[names.index(maior_nome)] = names[names.index(maior_nome)][:1]

    return remove_nomes(" ".join(names))

   