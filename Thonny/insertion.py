# def tri_insertion(liste):
#     for i in range(1,len(liste)):
#         elt=liste[i]
#         j=i-1
#         while j>=0 and liste[j]<elt:
#             liste[j+1]=liste[j]
#             j-=1
#         liste[j+1]=elt
#     return liste
# 
l=[4,9,6,7,12,3,4]
# print(l)
# print(tri_insertion(l))

def tri_1(liste: list) -> list:
    n = len(liste)
    j = 1
    while j<n:
        i=j
        while liste[i-1]>x and i>0:
            liste[i]=liste[i-1]
            i=i-1
        liste[i]=x
        j+=1
    return liste


def tri_2(liste: list) -> list:
    for i in range(1,len(liste)):
        x = liste[i]
        j = i
        while liste[j-1] > x and j>0:
            liste[j]=liste[j-1]
            j-=1
        liste[j]=x
    return liste


def tri_3(liste: list):
    for j in range(1, len(liste)):
        x = liste[j]
        for i in range(j, len(liste)):
            if liste[i-1] > x:
                liste[i]=liste[i-1]
        liste[i]=x
    return liste

print(tri_3(l))

