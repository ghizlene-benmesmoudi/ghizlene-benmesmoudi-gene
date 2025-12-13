# BENMESMOUDI Ghizlene
# M1 Génétique....13/12/2025
# Membres de projet : - BENMESMOUDI Ghizlene
#                     - MOSTEFAOUI MARWA
#                     - BADAOUI FATIMA ZOHRA
#                     - MOUMENI ROUMAISSA AICHA
#                     - BENSALAH YOUSRA
import pandas as pd
# Données de Départ
sequences = [
    "ATGCGTACGTA",
    "GCTAGCTAGGCC",
    "ATGCGCGTAAGT",
    "TACCGATCGTA",
    "ATGAAAGGCTT",
    "CGTACGTAGC",
    "TTAACCGGAT"
]
# Question 1 : Créer et afficher le DataFrame
df = pd.DataFrame({"Sequence": sequences})
print("Question 1 :")
print(df)
# Question 2 : Créer et afficher uniquement la colonne Length
df["Length"] = df["Sequence"].str.len()
print("\nQuestion 2 :")
print(df["Length"]) 
# Question 7 : Calculer l’écart-type de GC% et Length
ecart_type_gc = df["GC%"].std()
ecart_type_length = df["Length"].std()
print("\nQuestion 7 :")
print("Écart-type GC% :", ecart_type_gc)
print("Écart-type Length :", ecart_type_length)

 
