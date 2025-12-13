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
],
"longueur" :[12,12,12,10,11,10,10],
"pourcentage de GC": [50,60,67,58,33,40,45,45,60,50]
# Question 1 : Créer et afficher le DataFrame
df = pd.DataFrame({"Sequence": sequences})
print("Question 1 :")
print(df)
# Question 2 : Créer et afficher uniquement la colonne Length
df["Length"] = df["Sequence"].str.len()
print("\nQuestion 2 :")
print(df["Length"]) 

 
