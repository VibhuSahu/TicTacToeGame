
# Tic Tac Toe Game with Tkinter

This project is a simple implementation of the classic Tic Tac Toe game using Python and the Tkinter graphical user interface (GUI) library. The game allows two players to take turns marking spaces on a 3x3 grid. The player who successfully places three of their marks (either "X" or "O") in a horizontal, vertical, or diagonal row is declared the winner.

## Features

- The game features a user-friendly graphical interface created with Tkinter, providing a visually appealing way for players to interact with the game.

- Players alternate turns, and the current player is indicated on a label at the bottom of the window. The label dynamically updates to show whose turn it is.

- The game checks for a winner after each move. If a player achieves three consecutive marks in a row, the game declares that player the winner and highlights the winning combination.

- A message box from Tkinter's messagebox module is used to display information about the winner when the game concludes. It shows a message indicating which player won and then exits the game.

## Code Structure

The Tic Tac Toe game follows a structured implementation in Python using the Tkinter library:

### Game Logic Functions

The core game logic is encapsulated in Python functions, which handle various aspects of the game:

- **Button Clicks:** Functions are defined to respond to button clicks on the Tic Tac Toe grid. These functions control the placement of marks on the board.

- **Winner Checking:** There is a dedicated function to check for a winner after each move. It examines the current state of the board to determine if a player has achieved a winning combination.

- **Player Toggling:** Another function manages the toggling of turns between players. It updates the current player and dynamically modifies the information displayed at the bottom of the window.

### Tkinter's Button Widget

The graphical representation of the game board is created using Tkinter's `Button` widget. Each button corresponds to a cell on the 3x3 grid, allowing players to interactively place their marks.

### Labels for Player Information

Tkinter's `Label` widget is employed to display information about the current player's turn. The label, positioned at the bottom of the window, dynamically updates to indicate which player's turn it is.

This structured approach makes the code modular and easy to understand, facilitating maintenance and potential future enhancements.

## Support

The Tic Tac Toe game is designed to run seamlessly on multiple operating systems, providing a versatile and accessible gaming experience. The supported platforms include:

- **Windows:** The game has been tested and confirmed to run on Windows systems.

- **Linux:** Users on Linux-based operating systems can enjoy the game without compatibility concerns.

- **Mac:** The game is compatible with macOS, ensuring a consistent experience for Mac users.

For any issues or questions regarding compatibility or gameplay, feel free to reach out for assistance. We aim to provide support across diverse environments to make the game enjoyable for a wide audience.

For support inquiries, please contact us at: [vibhuworkon@gmail.com](mailto:vibhuworkon@gmail.com)

## Optimizations

In the development of this Tic Tac Toe game, several optimizations have been implemented to enhance code quality, improve performance, and ensure accessibility.

### Code Refactors

- **Modularization:** The code has been structured into functions, promoting modularity and code reuse. This improves readability and maintainability.

- **Variable Naming:** Meaningful variable names have been employed to enhance code comprehension and make the logic more self-explanatory.

### Performance Improvements

- **Winner Checking Algorithm:** The algorithm for checking a winner has been optimized for efficiency, reducing unnecessary iterations and improving overall performance.

- **Button Click Handling:** The handling of button clicks has been streamlined to minimize processing time, providing a more responsive user experience.

### Accessibility

- **User Interface Clarity:** The user interface has been designed with clarity in mind, ensuring that players can easily understand the game state, current player turn, and any messages displayed.

- **Error Handling:** Robust error handling has been implemented to gracefully manage unexpected situations, providing a smoother gameplay experience.

### Continuous Contact Information

For ongoing support, inquiries, or collaboration opportunities, please feel free to reach out via email at [vibhuworkon@gmail.com](mailto:vibhuworkon@gmail.com). Your feedback and suggestions are valuable in further enhancing the game and ensuring a positive user experience.


## Installation

- Ensure you have Python installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

### Running the Game

1. **Clone the Repository:**
   Open a terminal or command prompt and clone the Tic Tac Toe repository to your local machine.

   ```bash
   git clone https://github.com/VibhuSahu/TicTacToeGame.git
   ```


2. **Activate the virtual environment:**

    Run the command to activate the virtual environment
    
    __For Linux/macOS:__

   ```bash
   source TicTacToeGame/bin/activate
   ```


    __For Windows:__
   ```bash
   TicTacToeGame/Scripts/activate.bat
   ```


3. **Navigate to the Project Directory:**
   Change your working directory to the location where you cloned the repository.

   ```bash
   cd TicTacToeGame
   ```


4. **Run the Game:**
   Execute the main Python script to run the Tic Tac Toe game.

   ```bash
   python main.py
   ```

   If you are using Python 3, you might need to use `python3` instead of `python`.

5. **Play the Game:**
   The game window should open, displaying the Tic Tac Toe board. Click on the empty spaces to place your marks, and enjoy playing!



### Exiting the Game

- To exit the game, close the game window or use the provided exit functionality within the game.

    __Deactivate the Virtual Environment:__
    ```bash
    deactivate
    ```

For any inquiries or assistance, feel free to reach out to [vibhuworkon@gmail.com](mailto:vibhuworkon@gmail.com).





## Boost Software License - Version 1.0

Permission is granted, free of charge, to use, reproduce, display, distribute, execute, and transmit the Software, and to prepare derivative works, subject to the following conditions:

- Include copyright notices and this license statement in all copies and derivative works.
- The Software is provided "AS IS," without warranty of any kind.
- The copyright holders are not liable for any damages or liability arising from the use of the Software.

For detailed terms, see the [full license](./LICENSE).

For inquiries or support, contact [vibhuworkon@gmail.com](mailto:vibhuworkon@gmail.com).



---