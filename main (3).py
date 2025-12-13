# BENMESMOUDI Ghizlene

# M1 Génétique....13/12/2025
# Membres de projet : - BENMESMOUDI Ghizlene
#                     - MOSTEFAOUI MARWA
#                     - BADAOUI FATIMA ZOHRA
#                     - MOUMENI ROUMAISSA AICHA
#                     - BENSALAH YOUSRA

 import pandas as pd

# Données de départ

sequences = [

    "ATGCGTACGTA",

    "GCTAGCTAGGCC",

    "ATGCGCGTAAGT",

    "TACCGATCGTA",

    "ATGAAAGGCTT",

    "CGTACGTAGC",

    "TTAACCGGAT"

]
# Question 5 : Calculer et afficher le pourcentage GC

df["GC%"] = ((df["G_count"] + df["C_count"]) / df["Length"]) * 100

print("\nQuestion 5 :")

print(df["GC%"])

# Question 6 : Classer les séquences selon le pourcentage GC

def gc_categorie(gc):

    if gc > 55:

        return "Riche"

    elif 45 <= gc <= 55:

        return "Moyen"

    else:

        return "Faible"

df["Categorie_GC"] = df["GC%"].apply(gc_categorie)

print("\nQuestion 6 :")

print(df["Categorie_GC"])
