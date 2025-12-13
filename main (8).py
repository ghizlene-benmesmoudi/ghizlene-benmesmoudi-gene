# BENMESMOUDI Ghizlene { LE CHEF DE GROUP}

# M1 Génétique....13/12/2025

# Membres de projet : - MOUMENI  ROUMAISSA AICHA 
                   
#                     -  BENMESMOUDI Ghizlene

#                     - MOSTEFAOUI MARWA

#                     - BADAOUI FATIMA ZOHRA

#                     - BENSALAH YOUSRA

import pandas as pd

# 1) Liste des sequences

sequences = [

    "ATGCGTACGTA",

    "CGTAGCTAGGCC",

    "ATGCGCGTAAGT",

    "TACGATCGTA",

    "ATGAAAGGCTT",

    "CGTACGTAGC",

    "TTAACCGGAT"
    ]

#question 03
# 3) Calculer la longueur et compter G, C

df["Length"] = df["Sequence"].str.len()

df["G_count"] = df["Sequence"].str.count("G")

df["C_count"] = df["Sequence"].str.count("C")

# question 04
# 4) Calculer %GC et arrondir à 3 décimales

df["GC%"] = ((df["G_count"] + df["C_count"]) / df["Length"] * 100).round(3)

 

