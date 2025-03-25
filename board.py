import pygame

class Board:
    X = 800
    Y = 800
    pygame.init()
    screen = pygame.display.set_mode((X, Y))


    def __init__(self):
        self.board = {}

    def get_board(self):
        return self.board
    def set_board(self, board):
        self.board = board
    def newBoard(self):
        for i in range(8):
            for j in range(8):
                self.board[chr(97+i)+str(j+1)] = " "
    def getPosition(self, piece):
        for key, value in self.board.items():
            if value == piece:
                return key
        return None
    def coordinatesToPosition(self, x, y, square_size=100):
        if 0 < x < self.X and 0 < y < self.Y:
            return chr(97 + int(x // square_size))+str(8 - int(y // square_size))

    def positionToCoordinates(self, position, square_size=100):
        row = ord(position[0]) - 97
        col = 8 - int(position[1])
        return row * square_size, col * square_size
    #stores new peice location
    def setPiecePosition(self, piece,  position):
        self.board[position] = piece

    def draw_board(self, square_size=100):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    color = (200, 200, 200)
                else:
                    color = (50, 50, 50)
                pygame.draw.rect(self.screen, color, (j * square_size, i * square_size, square_size, square_size))

    def draw_pawn_promtion_option(self):
        pass
    def draw_menu(self):
        pass
