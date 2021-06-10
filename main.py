import tkinter as tk
from tkinter.ttk import *
import game


class Launcher(tk.Tk):
    def __init__(self):
        super().__init__()       
        
        self.title("Gun Mayhem Launcher")

        self.iconbitmap("assets/launcher/icon.ico")

        canvas = tk.Canvas(width=562, height=101)
        canvas.grid(row=0, column=0, columnspan=2, padx=20, pady=15)
        self.title = tk.PhotoImage(file="assets/launcher/title.gif")
        canvas.create_image(0, 0, anchor="nw", image=self.title)

        Label(text="Player 1 controls:").grid(row=1, column=0)
        
        Label(text="Move left: ←").grid(row=2, column=0)
        Label(text="Move right: →").grid(row=3, column=0)
        Label(text="Jump: ↑").grid(row=4, column=0)
        Label(text="Shoot: .").grid(row=5, column=0)
        
        Label(text="Player 2 controls:").grid(row=1, column=1)
        Label(text="Move left: A").grid(row=2, column=1)
        Label(text="Move right: D").grid(row=3, column=1)
        Label(text="Jump: W").grid(row=4, column=1)
        Label(text="Shoot: G").grid(row=5, column=1)

        Separator(orient='horizontal').grid(row=6, column=0, columnspan=2, ipadx=250, pady=10)

        color_options = [
            "Black",
            "Blue",
            "Green",
            "Red",
            "Yellow",
        ]

        Label(text="Enter Player 1's name:").grid(row=7, column=0, pady=4)
        Label(text="Enter Player 2's name:").grid(row=7, column=1, pady=4)
        self.player_1_name_input = Entry()
        self.player_2_name_input = Entry()
        self.player_1_name_input.insert(10, "Player 1")
        self.player_2_name_input.insert(10, "Player 2")
        self.player_1_name_input.grid(row=8, column=0)
        self.player_2_name_input.grid(row=8, column=1)

        self.player_1_color_variable = tk.StringVar()
        self.player_2_color_variable = tk.StringVar()

        Label(text="Choose Player 1's color:").grid(row=9, column=0, pady=4)
        self.player_1_color_input = OptionMenu(
            self, self.player_1_color_variable, color_options[2], *color_options)
        self.player_1_color_input.grid(row=10, column=0)
        self.player_1_color_input.configure(width=15)

        Label(text="Choose Player 2's color:").grid(row=9, column=1, pady=4)
        self.player_2_color_input = OptionMenu(
            self, self.player_2_color_variable, color_options[3], *color_options)
        self.player_2_color_input.grid(row=10, column=1)
        self.player_2_color_input.configure(width=15)

        Button(text="Launch", command=self.run_game).grid(
            row=11, column=0, sticky="e", pady=15)

        Button(text="Exit", command=self.quit).grid(
            row=11, column=1, sticky="w", pady=15)

    def get_input(self):
        player_1_name = self.player_1_name_input.get()
        player_2_name = self.player_2_name_input.get()
        player_1_color = self.player_1_color_variable.get().lower()
        player_2_color = self.player_2_color_variable.get().lower()

        return player_1_name, player_2_name, player_1_color, player_2_color

    def run_game(self):
        args = self.get_input()
        self.destroy()  # close launcher

        # new game
        g = game.Game(*args)
        while g.running:
            g.new()
        g.quit()


if __name__ == "__main__":
    launcher = Launcher()
    launcher.mainloop()
