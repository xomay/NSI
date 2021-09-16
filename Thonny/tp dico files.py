import random

def dico_alea() -> dict:
    """
    Fonction qui construit un dictionnaire de codage
    à chaque lettre MAJUSCULE de l'alphabet on fait correspondre
    une lettre MAJUSCULE prise aléatoirement
    :return: un dictionnaire ex : {'A': 'D', 'B': 'Y'....}
    """
    dico_alpha=[chr(i) for i in range(65,91)]
    random.shuffle(dico_alpha)
    d={}
    for i in range (0,26):
        d[chr(65+i)]=dico_alpha[i]
    return d


def crypto_lettre(dico: dict, lettre: str) -> str:
    """
    Fonction qui renvoie une lettre cryptée d'après le dictionnaire associé
    :param dico:
    :param lettre: lettre MAJUSCULE
    :return: la lettre cryptée en MAJUSCULE
    """
    l=dico[lettre]
    return l

def crypto_texte(dico: dict, texte: str) -> str:
    """
    Fonction qui renvoie un texte crypté à partir du texte entré et
    du dictionnaire associé
    On utilise la fonction crypto_lettre
    :param dict:
    :param texte: texte en MAJUSCULES
    :return: le texte crypté en MAJUSCULES
    """
    crypt=""
    for lettre in texte:
        if lettre==" ":
            crypt+=" "
        else:
            crypt+=crypto_lettre(dico, lettre)
    return crypt
            

def lire_fichier(fichier: str) -> str:
    """
    Fonction qui renvoie une liste après lecture d'un fichier texte
    :param fichier:
    :return: liste contenant le texte
    """
    f=""
    with open(fichier,"r") as fich:
        f=fich.read()
    return f
        

def occurrence(texte: str) -> dict:
    """
    Fonction qui renvoie un dictionnaire composé des lettres de
    l'alphabet et du nombre d'occurences de la lettre dans le texte
    entré en paramètre
    :param texte: le texte crypté en MAJUSCULES
    :return: un dictionnaire
    """
    occu={'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    for lettre in texte:
        if lettre!=" ":
            occu[lettre]+=1
    return occu
    

def maxi(dico: dict) -> str:
    """
    Fonction qui renvoie la lettre ayant la plus grande occurence
    des lettres du dictionnaire
    :param dico: dictionnaire des occurences
    :return: la lettre ayant la plus grande occurence
    """
    max = None
    lettre_max = None
    for (lettre, occurrence) in dico.items():
        if max is None or occurrence > max:
            max = occurrence
            lettre_max = lettre
    return lettre_max

def propose(texte: str) -> dict:
    """
    Fonction qui renvoie une proposition de dictionnaire de décodage
    du texte entré en paramètre
    On utilise les fonctions occurence et maxi
    :param texte:
    :return: le dictionnaire de décodage
    """
    dico_occu=occurrence(texte)
    deco={}
    frequence=['E', 'A', 'S', 'I', 'N', 'T', 'R', 'L', 'U', 'O', 'D', 'C', 'P', 'M', 'V', 'G', 'F', 'B', 'Q', 'H', 'X', 'J', 'Y', 'Z', 'K', 'W']
    for i in range (0,26):
        lettre=maxi(dico_occu)
        deco[lettre]=frequence[i]
        dico_occu[lettre]=-1
    return deco

def permute(dico: dict,l1: str,l2: str) -> dict:
    """
    Fonction qui permute 2 lettres dans un dictionnaire
    :param dico:
    :param l1: lettre en MAJUSCULE
    :param l2: lettre en MAJUSCULE
    :return: le nouveau dictionnaire
    """
    a=""
    b=""
    for cle, val in dico.items():
        if cle==l1:
            a=cle
        if val==l2:
            b=cle
    dico[a]=l2
    dico[b]=l1
    return dico

#programme principal
table = lire_fichier("texte_crypté.txt")
a = propose(table)
d=dico_alea()
t="scores.txt"
# print(d)
# print(crypto_lettre(d,'A'))
# print(crypto_texte(d,'BIENVENUE EN NSI'))
print(a)
# print(occurrence('VOILA LE TEXTE A LIRE'))
# print(maxi(occurrence('VOILA LE TEXTE A LIRE')))
# print(crypto_texte(d, table))
permute(d,"N","L")
permute(d,"H","B")
permute(d,"H","G")
permute(d,"L","U")
permute(d,"Q","H")
print()
# print(crypto_texte(d, table))