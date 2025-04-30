import tkinter as tk
from tkinter import messagebox, simpledialog
import configparser


class GUI:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.window = None

    def set_up_config(self):
        self.config.read('config.ini')
        self.config["Settings"] = {
            "auto-queen-promotion": "false",
            "player-type": "Player",
            "gamemode": "None",
        }

        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)

    def write_to_config(self, key, value):
        self.config.read('config.ini')
        self.config["Settings"][key] = value
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)

    def get_config(self):
        return self.config["Settings"]

    def get_config_values(self, section):
        return self.config.get("Settings", section)

    def start_up_gui(self):
        self.window = tk.Tk()
        self.window.title("ChessAI")

        tk.Label(self.window, text="Start Menu", font=("Arial", 20)).pack(pady=10)

        tk.Button(self.window, text="Settings", font=("Arial", 20), command=self.open_settings_window).pack(pady=5)
        tk.Button(self.window, text="Free Style", font=("Arial", 12),
                  command=lambda: self.set_gamemode("free-style")).pack(pady=5)

        frame_ai = tk.Frame(self.window)
        frame_ai.pack(pady=5)
        tk.Button(frame_ai, text="AI", font=("Arial", 12),
                  command=lambda: self.set_gamemode("AI")).pack(side=tk.LEFT)
        tk.Entry(frame_ai, font=("Arial", 12), width=20).pack(side=tk.LEFT, padx=5)

        tk.Button(self.window, text="Puzzle", font=("Arial", 12),
                  command=lambda: self.set_gamemode("puzzle")).pack(pady=5)

        self.window.mainloop()

    def set_gamemode(self, mode):
        self.write_to_config("gamemode", mode)
        self.window.destroy()

    def open_settings_window(self):
        self.window.destroy()
        self.window = tk.Tk()
        self.window.title("ChessAI Settings")

        tk.Label(self.window, text="Settings", font=("Arial", 20)).pack(pady=10)

        tk.Button(self.window, text="Queen Promotion", font=("Arial", 12),
                  command=self.toggle_queen_promotion).pack(pady=5)

        tk.Button(self.window, text="Player 1", font=("Arial", 12),
                  command=lambda: self.write_to_config("player-type", "player_1")).pack(pady=5)

        tk.Button(self.window, text="Player 2", font=("Arial", 12),
                  command=lambda: self.write_to_config("player-type", "player_2")).pack(pady=5)

        tk.Button(self.window, text="Back", font=("Arial", 12),
                  command=self.start_up_gui).pack(pady=10)

        self.window.mainloop()

    def toggle_queen_promotion(self):
        current_value = self.get_config_values("auto-queen-promotion")
        new_value = "true" if current_value == "false" else "false"
        self.write_to_config("auto-queen-promotion", new_value)
        messagebox.showinfo("Queen Promotion", f"Set to {new_value}")

    def pawn_promotion_gui(self):
        options = ["Queen", "Knight", "Rook", "Bishop"]
        choice = simpledialog.askstring("Promotion", "Choose a new piece:\n(Queen, Knight, Rook, Bishop)")
        if choice and choice.lower() in [x.lower() for x in options]:
            return choice.lower()
        return self.pawn_promotion_gui()  # Retry if invalid


# Example usage
# gui = GUI()
# gui.set_up_config()
# gui.start_up_gui()
