def occurrences(caractère, mot):
    compteur=0
    for lettre in mot:
        if lettre==caractère:
            compteur=compteur+1
    return compteur

print(occurrences("a", "caractère"))