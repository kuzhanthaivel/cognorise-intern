import random
import tkinter as tk
from tkinter import messagebox

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return "Win"
    else:
        return "Lose"

def on_choice_button_click(choice):
    computer_choice = get_computer_choice()
    result = determine_winner(choice, computer_choice)
    
    display_result_label.config(text=f"Computer chose {computer_choice}\nResult: {result}")

    if result == "Win":
        messagebox.showinfo("Result", "You win!")
    elif result == "Lose":
        messagebox.showinfo("Result", "You lose.")
    else:
        messagebox.showinfo("Result", "It's a tie!")


root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

choice_label = tk.Label(root, text="Choose rock, paper, or scissors:")
choice_label.pack(pady=10)

rock_button = tk.Button(root, text="Rock", command=lambda: on_choice_button_click("rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", command=lambda: on_choice_button_click("paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", command=lambda: on_choice_button_click("scissors"))
scissors_button.pack(pady=5)

display_result_label = tk.Label(root, text="")
display_result_label.pack(pady=10)

root.mainloop()
