chaine=str(input("écrivez une chaine de charactère "))
chaine2=""
def rot13(s) -> str:
    """Fonction qui code selon le code César avec un décalage de 13
    Args:
        s (str): chaine à coder
    Returns:
        str: chaine codée
    """
    chaine2=""
    for i in range(len(s)):
        if s[i] == chr(32):
            chaine2=chaine2+chr(32)
        else:
            cha=(ord(s[i])-97)
            cha=cha+13
            cha=cha%26
            cha=cha+97
            chaine2=chaine2+chr(cha)
    return chaine2

print(rot13(chaine))

# je pense que les opérations peuvent être regroupé mais je préférais les faire une par une par soucis de compréhension
# actuellement ça donne une erreur