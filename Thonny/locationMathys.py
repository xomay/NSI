tri=[[1,3],[2,5],[4,7],[1,8],[5,9],[9,10],[8,11],[11,14],[13,16]]
def final(t: list) -> list:
    """
    fonction qui renvoie la liste des clients pris
    :param t: liste de tous les clients tries
    :param return: liste des clients pris
    """
    client=[]
    for i in range(len(t)):
        if len(client)==0:
            client.append(t[0])
        else:
            for i in range(len(t)):
                if t[i][0]-client[len(client)-1][1]>0:
                    client.append(t[i])
    return client
print(final(tri))