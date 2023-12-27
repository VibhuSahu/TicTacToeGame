import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage



def check_winner():
    """
    The function `check_winner()` checks for a winning combination in a Tic-Tac-Toe game and displays a
    message with the winner's name if a winning combination is found.
    """
    for combo in [[0 , 1, 2], [ 3, 4, 5], [ 6, 7, 8], [ 0, 3, 6], [ 1, 4, 7],[ 2, 5, 8], [ 0, 4, 8], [ 2, 4, 6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] !="":
            buttons[combo[0]].config(bg = "green")
            buttons[combo[1]].config(bg = "green")
            buttons[combo[2]].config(bg = "green")
            messagebox.showinfo("Tic-Tac-Toe", f"player {buttons[combo[0]]['text']} wins!")
            root.quit()
            

def button_click(index):
    """
    The function `button_click` updates the text of a button, checks for a winner, and toggles the
    current player.
    
    :param index: The `index` parameter in the `button_click` function represents the index of the
    button that was clicked. It is used to determine which button was clicked and perform actions based
    on that
    """
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] == current_player
        check_winner()
        toggle_player()
        

def toggle_player():
    """
    The function `toggle_player` switches the current player between "x" and "O" and updates a label to
    display the current player's turn.
    """
    global current_player
    current_player = "x" if current_player == "O" else "O"
    label.config(text = f"Player {current_player}'s turn")
    
    
    
# Create the main Tkinter window    
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Load and set the window icon
logo = PhotoImage(file="images/tic-tac-toe.png")
root.iconphoto(False, logo)


# Set the window size and make it fixed
width, height = 400, 250
root.geometry(f"{width}x{height}")
root.minsize(width=width, height=height)
root.maxsize(width=width, height=height)


# Create buttons for the Tic-Tac-Toe grid
buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]


# Place buttons in a 3x3 grid
for i, button in enumerate(buttons):
    button.grid(row=i //3, column=i%3)


# Initialize game variables
current_player = "x"
winner = False

# Create and place a label for player turn information
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)


# Start the Tkinter event loop
root.mainloop()