import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.turn = "X"
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(self.master, text="", font=("Helvetica", 30), height=1, width=2,
                                   command=lambda row=row, col=col: self.button_click(row, col))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

    def button_click(self, row, col):
        if self.board[row][col] == "":
            self.buttons[row][col].config(text=self.turn)
            self.board[row][col] = self.turn
            if self.check_win():
                messagebox.showinfo("Tic Tac Toe", f"{self.turn} wins!")
                self.reset_game()
            elif self.check_tie():
                messagebox.showinfo("Tic Tac Toe", "Tie game!")
                self.reset_game()
            else:
                self.change_turn()

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_tie(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def change_turn(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def reset_game(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")
                self.board[row][col] = ""
        self.turn = "X"


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
