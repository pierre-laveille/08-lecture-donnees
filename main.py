"""
Module de gestion et d'analyse de listes numériques extraites d'un fichier CSV.
Ce programme permet de lire un fichier et d'effectuer des calculs statistiques.
"""

#### Imports et définition des variables globales
import csv

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, mode='r', encoding='utf8') as f:
        lecteur = csv.reader(f, delimiter=';')
        l = []
        for ligne in lecteur:
            liste_entiers = [int(x) for x in ligne]
            l.append(liste_entiers)
    return l

def get_list_k(data, k):
    """Retourne la k-ième liste de la structure de données <data>."""
    return data[k]

def get_first(l):
    """Retourne le premier élément de la liste <l>."""
    return l[0]

def get_last(l):
    """Retourne le dernier élément de la liste <l>."""
    return l[-1]

def get_max(l):
    """Retourne la valeur maximale présente dans la liste <l>."""
    return max(l)

def get_min(l):
    """Retourne la valeur minimale présente dans la liste <l>."""
    return min(l)

def get_sum(l):
    """Retourne la somme de tous les éléments de la liste <l>."""
    return sum(l)


#### Fonction principale


def main():
    """
    Fonction principale : charge les données et affiche les résultats des tests.
    """
    # data = read_data(FILENAME)
    # for i, l in enumerate(data):
    #     print(i, l)
    # k = 37
    # print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
