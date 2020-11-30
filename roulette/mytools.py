
from random import choice as choisir
from time import sleep as attendre


JOUEURS = [
    'Laurent',
    'Lou',
    'Thomas',
    'Imen',
    'Paul',
    'Yohann',
    'Tristan'
]

def roulette(peut_passer, déjà_passé):

    if peut_passer == []:
        peut_passer = JOUEURS.copy()
        déjà_passé = []

    print(f"Sont en piste pour la prochaine question :\n\t{', '.join(peut_passer)}\n")
    attendre(1)
    print(f"Sont sur le banc pour le moment :\n\t{'Personne 😈' if déjà_passé == [] else ', '.join(déjà_passé)}\n")
    attendre(1)

    l_elu = choisir(peut_passer)
    peut_passer.remove(l_elu)
    déjà_passé.append(l_elu)

    print("L'heureux(se) élu(e) est", end=" ")
    for i in range(3):
        print('.', end="")
        attendre(1)
    print(f" {choisir(['🎉', '🥳', '🎊'])} {l_elu.upper()} {'👩‍💻' if l_elu in ['Claire', 'Marie'] else '👨‍💻'}")

    return peut_passer, déjà_passé


def try_me():
    joueurs = JOUEURS.copy()
    sur_le_banc = []

    joueurs, sur_le_banc = roulette(joueurs, sur_le_banc)
