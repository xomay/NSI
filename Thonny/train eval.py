def calcul(n: int) -> int:
    """
    Fonction qui prend un entier n et le divise par 2 s'il est pair
    ou le multiplie par 3 s'il est impair
    :param n: entier suppérieur à 0
    :return: le résultat du calcul
    """
    res=0
    if n%2==0:
        res=n//2
    else:
        res=n*3
    return res

assert(calcul(4))==2
assert(calcul(5))==15
    
# print(calcul(4))

def analyse(chaine: str, c: str) -> bool:
    """
    Fonction qui analyse une chaine de caractère pour savoir
    combien de fois une lettre donnée est présente dans cette chaine
    :param chaine: chaine de caractère
    :param c: lettre présente ou non dans la chaine
    :return: renvoie le nombre de fois qu'apparait cette lettre
    """
    a=0
    for lettre in chaine:
        if lettre==c:
            a+=1
    return a

assert(analyse("Je n'ai pas les mots pour décrire à quel point osu est nul", "a"))==2
            

# print(analyse("osu c nul", "u"))

def 



