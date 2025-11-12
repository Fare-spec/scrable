import utils


def get_values(path: str = "data/lettres.txt") -> dict[str, dict[str, int]]:
    dico = utils.generer_dico(path)
    return dico


def init_pick(dico: dict[str, dict[str, int]]) -> list[str]:
    pick = list()
    for letter, occ in dico.items():
        for _ in range(occ["occ"]):
            pick.append(letter)
    return pick


get_values()
