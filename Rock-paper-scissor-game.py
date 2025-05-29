import tkinter as tk
import random
from tkinter import messagebox
options = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0
def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(options)
    user_choice_label.config(text=f"Your Choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")
    if user_choice == computer_choice:result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        computer_score += 1

    result_label.config(text=result)
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")
def reset_game():
    global user_score, co_
