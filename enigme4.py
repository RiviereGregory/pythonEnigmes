base_4 = {
    "GA": 0,
    "BU": 1,
    "ZO": 2,
    "MEU": 3
}


def calcul_base_4(list_nb):
    somme = 0
    power = len(list_nb)
    for nb in list_nb:
        power = power - 1
        somme = somme + pow(4, power) * nb
    print(somme)


def read_fichier(name):
    file = open(name, 'r')
    list_nb = []
    for line in file:
        for word in line.split():
            list_nb.append(base_4[word])
    file.close()
    calcul_base_4(list_nb)


# réponse 1968

if __name__ == '__main__':
    read_fichier('enigmes\Enigme4.txt')
