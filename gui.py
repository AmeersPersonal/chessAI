import PySimpleGUI as sg
import  configparser

class GUI:
    def __init__(self):
        self.config = configparser.ConfigParser()

    def set_up_config(self):
        self.config.read('config.ini')
        self.config["Settings"] = {
            "auto-queen-promotion": "false",
            "player-type":"Player",
            "gamemode":"None",

        }

        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)
            configfile.close()

    def write_to_config(self, key, value):
        self.config.read('config.ini')
        self.config["Settings"][key] = value
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)
            configfile.close()
    def get_config(self):
        return self.config["Settings"]
    def get_config_values(self, section):
        return self.config.get("Settings", section)

    def start_up_gui(self):
        main_layout = [
            [sg.Text("Star Menu", font=(None, 20), justification="center", expand_x=True)],
            [sg.Button("Settings", font=(None, 20))],
            [sg.Button("Free Style", font=(None, 12))],
            [sg.Button("AI", font=(None, 12)), sg.Input("Choose An Opening", key="-IN-", font=(None, 12))],
            [sg.Button("Puzzle", font=(None, 12))]
        ]
        window = sg.Window("ChessAI", main_layout, finalize=True)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break

            if event == "Settings":
                window.close()
                self.open_settings_window()

            if event == "Free Style":
                window.close()
                self.write_to_config("gamemode", "free-style")
                break

            if event == "AI":
                window.close()
                self.write_to_config("gamemode", "AI")

                break

            if event == "Puzzle":
                window.close()
                self.write_to_config("gamemode", "puzzle")
                break

        window.close()

    def open_settings_window(self):
        settings_layout = [
            [sg.Text("Settings", font=(None, 20), justification="center", expand_x=True)],
            [sg.Button("QueenPromotion", font=(None, 12))],
            [sg.Button("Player 1", font=(None, 12)), sg.Button("Player 2", font=(None, 12))],
            [sg.Button("Back", font=(None, 12))]
        ]
        window = sg.Window("ChessAI Settings", settings_layout, finalize=True)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == "Back":
                window.close()
                self.start_up_gui()
                break

            if event == "QueenPromotion":
                current_value = self.get_config_values("auto-queen-promotion")
                new_value = "true" if current_value == "false" else "false"
                self.write_to_config("auto-queen-promotion", new_value)

            if event == "Player 1":
                self.write_to_config("player-type", "player_1")

            if event == "Player 2":
                self.write_to_config("player-type", "player_2")

        window.close()

    def pawn_promotion_gui(self):
        layout =[
            [sg.Text("Select a new piece", font=(None, 20), justification="center", expand_x=True)],
            [sg.Button("Queen", font=(None, 12))],
            [sg.Button("Knight", font=(None, 12))],
            [sg.Button("Rook", font=(None, 12))],
            [sg.Button("Bishop", font=(None, 12))],
        ]
        
        window = sg.Window("ChessAI Pawn Promotion", layout, finalize=True)
        event, values = window.read()

        while True:
            if event == sg.WIN_CLOSED:
                return self.pawn_promotion_gui()

            if event == "Queen":
                window.close()
                return "queen"
            if event == "Knight":
                window.close()
                return "knight"
            if event == "Rook":
                window.close()
                return "rook"
            if event == "Bishop":
                window.close()
                return "bishop"



