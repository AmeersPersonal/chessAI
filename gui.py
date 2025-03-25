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
            [sg.Button("AI", font=(None, 12)), sg.In("Choose An Opening", key = "-IN-", font=(None, 12) )],
            [sg.Button("Puzzle", font=(None, 12))]
        ]
        window = sg.Window("ChessAI", main_layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == "Settings":
                print("settings")
                window.close()

                layout = [
                    [sg.Text("Settings", font=(None, 20), justification="center", expand_x=True)],
                    [sg.Button("QueenPromotion", font=(None,12))],
                    [sg.Button("Player 1", font=(None, 12)), sg.Button("Player 2", font=(None, 12))],
                    [sg.Button("Back", font=(None, 12))]
                ]
                window = sg.Window("ChessAI", layout)
                while True:
                    event, values = window.read()
                    if event == "QueenPromotion":
                        if self.get_config_values("auto-queen-promotion") == "false":
                            self.write_to_config("auto-queen-promotion", "true")
                        else:
                            self.write_to_config("auto-queen-promotion", "false")

                    if event == "Player 1":
                        self.write_to_config("player-type", "player_1")

                    if event == "Player 2":
                        self.write_to_config("player-type", "player_2")

                    if event == "Back":
                        
                        self.start_up_gui()



            if event == "Free Style":
                window.close()
                self.write_to_config("gamemode", "free-style")
            if event == "AI":
                window.close()
                self.write_to_config("gamemode", "AI")
            if event == "Puzzle":
                window.close()
                self.write_to_config("gamemode", "puzzle")


        window.close()

    def pawn_promotion_gui(self):
        pass

    #TODO:
    #if my intial idea does not work for pawn promotion gui
    #use pysimple gui todo it

