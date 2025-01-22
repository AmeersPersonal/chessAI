from main import  API_KEY, PROJECT_ID
import os, json

class GoogleGemResponse:
    def __init__(self,prompt:str, difficulity:str, response:str):
        self.prompt = prompt
        self.difficulity = difficulity
        self.response = response
