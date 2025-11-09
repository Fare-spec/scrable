import scrabble as scr


class Board:
    def __init__(self, size) -> None:
        self.size = size

    def init_jetons(self):
        self.board = [["" for _ in range(self.size)] for _ in range(self.size)]

    def affiche_jetons(self):
        # En-tête colonnes
        print("    " + "  ".join(f"{i:02d}" for i in range(1, self.size + 1)))
        print("   " + "|---" * self.size + "|")
        # Corps du plateau
        for i in range(self.size):
            ligne = f"{i + 1:02d} |"
            for j in range(self.size):
                ligne += f" {self.board[i][j]}  |"
            print(ligne)
            print("   " + "|---" * self.size + "|")
