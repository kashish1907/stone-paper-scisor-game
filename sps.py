import tkinter as tk
import random
from tkinter import messagebox

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("400x500")
        self.root.configure(bg="#f4f4f4")

        self.choices = ["Rock", "Paper", "Scissors"]
        self.user_score = 0
        self.comp_score = 0

        self.title = tk.Label(root, text="Rock, Paper, Scissors", font=("Segoe UI", 20, "bold"), bg="#f4f4f4")
        self.title.pack(pady=20)

        self.result_label = tk.Label(root, text="", font=("Segoe UI", 14), bg="#f4f4f4")
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(root, text="Your Score: 0   |   Computer Score: 0", font=("Segoe UI", 12), bg="#f4f4f4")
        self.score_label.pack(pady=10)

        self.btn_frame = tk.Frame(root, bg="#f4f4f4")
        self.btn_frame.pack(pady=20)

        self.create_buttons()

        self.reset_btn = tk.Button(root, text="Reset Game", font=("Segoe UI", 11), bg="#d35400", fg="white",
                                   padx=10, pady=5, command=self.reset_game)
        self.reset_btn.pack(pady=10)

    def create_buttons(self):
        for i, choice in enumerate(self.choices):
            btn = tk.Button(self.btn_frame, text=choice, font=("Segoe UI", 12), width=10, height=2,
                            bg="#2980b9", fg="white", command=lambda c=choice: self.play_round(c))
            btn.grid(row=0, column=i, padx=10, pady=10)

    def play_round(self, user_choice):
        comp_choice = random.choice(self.choices)

        outcome = self.get_winner(user_choice, comp_choice)

        if outcome == "win":
            self.user_score += 1
            result_text = f"You chose {user_choice}. Computer chose {comp_choice}.\n🎉 You Win!"
        elif outcome == "lose":
            self.comp_score += 1
            result_text = f"You chose {user_choice}. Computer chose {comp_choice}.\n😞 You Lose!"
        else:
            result_text = f"You chose {user_choice}. Computer chose {comp_choice}.\n😐 It's a Tie!"

        self.result_label.config(text=result_text)
        self.score_label.config(text=f"Your Score: {self.user_score}   |   Computer Score: {self.comp_score}")

    def get_winner(self, user, comp):
        if user == comp:
            return "tie"
        elif (user == "Rock" and comp == "Scissors") or \
             (user == "Scissors" and comp == "Paper") or \
             (user == "Paper" and comp == "Rock"):
            return "win"
        else:
            return "lose"

    def reset_game(self):
        self.user_score = 0
        self.comp_score = 0
        self.result_label.config(text="")
        self.score_label.config(text="Your Score: 0   |   Computer Score: 0")
        messagebox.showinfo("Reset", "Game has been reset. Let's play again!")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = RPSGame(root)
    root.mainloop()
