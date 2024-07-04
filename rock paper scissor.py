import tkinter as tk
import random

class RockPaperScissor:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("ROCK PAPER SCISSOR GAME")
        self.window.geometry("500x500")

        self.player_score = 0
        self.computer_score = 0

        self.player_score_label = tk.Label(self.window, text="Player Score: 0", font=("ALGERIAN", 20),fg="red")
        self.player_score_label.pack()

        self.computer_score_label = tk.Label(self.window, text="Computer Score: 0", font=("ALGERIAN", 20) , fg="red")
        self.computer_score_label.pack()

        self.result_label = tk.Label(self.window, text="", font=("ALGERIAN", 20))
        self.result_label.pack()

        self.rock_button = tk.Button(self.window, text="Rock", command=lambda: self.play("rock"),font=("ALGERIAN", 20) , fg="blue")
        self.rock_button.pack(fill="both", padx=30, pady=30 )

        self.paper_button = tk.Button(self.window, text="Paper", command=lambda: self.play("paper"),font=("ALGERIAN", 20) , fg="blue")
        self.paper_button.pack(fill="both", padx=30, pady=30)

        self.scissor_button = tk.Button(self.window, text="Scissor", command=lambda: self.play("scissor"),font=("ALGERIAN", 20) , fg="blue")
        self.scissor_button.pack(fill="both", padx=30, pady=30)

       
    def play(self, player_choice):
        choices = ["rock", "paper", "scissor"]
        computer_choice = random.choice(choices)

        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (player_choice == "rock" and computer_choice == "scissor") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissor" and computer_choice == "paper"):
            result = "Player wins!"
            self.player_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        self.result_label.config(text=f"Player: {player_choice}, Computer: {computer_choice}, {result}" , fg="green" ,)
        self.player_score_label.config(text=f"Player Score: {self.player_score}")
        self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = RockPaperScissor()
    game.run()