import google.generativeai as gem
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
from gui import *

load_dotenv()
API_KEY = os.getenv('GOOGLE_GEM_API_KEY')
PROJECT_ID = os.getenv('GOOGLE_GEM_PROJECT_ID')
model = "gemini-1.5-pro"

client = genai.Client(api_key=API_KEY)

#analyzes the board and returns only the pinned pieces to the king
def is_pinned( board, player ):
    response = client.models.generate_content(
        model = model,
                contents = ["Pretend that you're a grandmaster that has stage 4 cancer and desperate to give his apprentice all the right information to win.\n"
                    "Only state the information i am about to ask nothing else as the more you talk the faster your health deteriorates \n"
                    "reminder pinned pieces is when a piece if moved will result in check if there is none return an empty string \n"
                    f"return me a list of all {player} pieces that is pinned to the king, not the position of the pinned piece for the the player using this {board} the current player is player also explain why the piece is pinned"],
        config = types.GenerateContentConfig(
            max_output_tokens = 1000,
            temperature = 0.1
        )

    )
    return response.text
# gives us back the information of what pieces is causing the pin
#this will be used in the event manger class to determine if the piece can move
def piece_that_causes_pin(board, player):
    response = client.models.generate_content(
        model = model,
        contents=["Pretend that you're a grandmaster that has stage 4 cancer and desperate to give his apprentice all the right information to win.\n",
                  "Only state the information i am about to ask nothing else as the more you talk the faster your health detonates \n",
                  "return me in this format [(piece_name, [list of pieces pinning it])], reminder pinned pieces is a piece that next to the king and if moved will result in check or checkmate \n "
                  f"the current player is {player} and this is the board {board} and these are the pinned pieces {is_pinned(board, player)}"],
        config= types.GenerateContentConfig(
            max_output_tokens = 2000,
            temperature = 0.1
        )
    )
    return response.text



def moves_out_of_check():
    pass


def move():
    pass

