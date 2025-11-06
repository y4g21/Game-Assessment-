import tkinter as tk
import random
from tkinter import messagebox

class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Guess the Number")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        
        # Default game settings
        self.number_to_guess = None
        self.max_attempts = 0
        self.attempts = 0
        self.range_max = 100
        
        # Title label
        tk.Label(root, text="🎯 Guess the Number!", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(root, text="Choose your difficulty:", font=("Arial", 12)).pack()
        
        # Difficulty selection buttons
        tk.Button(root, text="Easy (1-50, 10 attempts)", font=("Arial", 10), width=25, 
                  command=lambda: self.start_game("Easy")).pack(pady=5)
        tk.Button(root, text="Medium (1-100, 7 attempts)", font=("Arial", 10), width=25, 
                  command=lambda: self.start_game("Medium")).pack(pady=5)
        tk.Button(root, text="Hard (1-200, 5 attempts)", font=("Arial", 10), width=25, 
                  command=lambda: self.start_game("Hard")).pack(pady=5)
        
        # Frame for game widgets
        self.game_frame = tk.Frame(root)
        self.game_frame.pack(pady=10)
        
        # Entry and labels (will be shown after difficulty chosen)
        self.info_label = tk.Label(self.game_frame, text="", font=("Arial", 12))
        self.entry = tk.Entry(self.game_frame, font=("Arial", 14), justify='center')
        self.feedback_label = tk.Label(self.game_frame, text="", font=("Arial", 12))
        self.attempts_label = tk.Label(self.game_frame, text="", font=("Arial", 12))
        
        self.guess_button = tk.Button(self.game_frame, text="Guess", font=("Arial", 12), command=self.check_guess)
        self.restart_button = tk.Button(self.game_frame, text="Restart Game", font=("Arial", 10), command=self.restart_game)

    def start_game(self, level):
        # Configure difficulty
        if level == "Easy":
            self.range_max = 50
            self.max_attempts = 10
        elif level == "Medium":
            self.range_max = 100
            self.max_attempts = 7
        elif level == "Hard":
            self.range_max = 200
            self.max_attempts = 5
        
        self.number_to_guess = random.randint(1, self.range_max)
        self.attempts = 0
        
        # Clear previous widgets and show game frame
        for widget in self.game_frame.winfo_children():
            widget.pack_forget()
        
        self.info_label.config(text=f"I'm thinking of a number between 1 and {self.range_max}.")
        self.info_label.pack(pady=5)
        self.entry.pack(pady=5)
        self.guess_button.pack(pady=5)
        self.feedback_label.pack(pady=5)
        self.attempts_label.pack(pady=5)
        self.restart_button.pack(pady=10)
        
        self.update_attempts_label()

    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit():
            self.feedback_label.config(text="⚠️ Please enter a number!", fg="orange")
            return
        
        guess = int(guess)
        self.attempts += 1
        
        if guess < self.number_to_guess:
            self.feedback_label.config(text="Too low! Try again.", fg="blue")
        elif guess > self.number_to_guess:
            self.feedback_label.config(text="Too high! Try again.", fg="purple")
        else:
            messagebox.showinfo("🎉 You Win!", 
                                f"Congratulations! You guessed {self.number_to_guess} in {self.attempts} attempts.")
            self.restart_game()
            return
        
        self.update_attempts_label()
        
        if self.attempts >= self.max_attempts:
            messagebox.showwarning("😢 Game Over", f"Out of attempts! The number was {self.number_to_guess}.")
            self.restart_game()

    def update_attempts_label(self):
        self.attempts_label.config(
            text=f"Attempts left: {self.max_attempts - self.attempts}"
        )

    def restart_game(self):
        # Clear entry and feedback
        self.entry.delete(0, tk.END)
        self.feedback_label.config(text="")
        self.info_label.config(text="Choose your difficulty:")
        
        # Reset to main menu
        for widget in self.game_frame.winfo_children():
            widget.pack_forget()
        
        self.__init__(self.root)  # reinitialize to show menu

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()
