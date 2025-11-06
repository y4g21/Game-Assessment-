import tkinter as tk
import random
from tkinter import messagebox

class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Guess the Number")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        self.number_to_guess = random.randint(1, 100)
        self.max_attempts = 7
        self.attempts = 0
        
        # Title label
        tk.Label(root, text="I'm thinking of a number between 1 and 100!", 
                 font=("Arial", 12)).pack(pady=10)
        
        # Guess entry
        self.entry = tk.Entry(root, font=("Arial", 14), justify='center')
        self.entry.pack(pady=10)
        self.entry.focus()
        
        # Submit button
        tk.Button(root, text="Guess", font=("Arial", 12), command=self.check_guess).pack(pady=5)
        
        # Feedback label
        self.feedback_label = tk.Label(root, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=10)
        
        # Attempts left label
        self.attempts_label = tk.Label(root, text=f"Attempts left: {self.max_attempts}", font=("Arial", 12))
        self.attempts_label.pack(pady=10)
        
        # Restart button
        tk.Button(root, text="Restart Game", font=("Arial", 10), command=self.restart_game).pack(pady=10)
    
    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit():
            self.feedback_label.config(text="⚠️ Please enter a number!", fg="orange")
            return
        
        guess = int(guess)
        self.attempts += 1
        attempts_left = self.max_attempts - self.attempts
        
        if guess < self.number_to_guess:
            self.feedback_label.config(text="Too low! Try again.", fg="blue")
        elif guess > self.number_to_guess:
            self.feedback_label.config(text="Too high! Try again.", fg="purple")
        else:
            messagebox.showinfo("🎉 You Win!", 
                                f"Congratulations! You guessed the number {self.number_to_guess} in {self.attempts} attempts.")
            self.restart_game()
            return
        
        self.attempts_label.config(text=f"Attempts left: {attempts_left}")
        
        if attempts_left == 0:
            messagebox.showwarning("😢 Game Over", f"Out of attempts! The number was {self.number_to_guess}.")
            self.restart_game()
    
    def restart_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.feedback_label.config(text="")
        self.attempts_label.config(text=f"Attempts left: {self.max_attempts}")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()
