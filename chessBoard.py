
import pygame



#game
class chessBoard:
    #game var
    previous_move_player_1 = ""
    previous_move_player_2 = ""
    player_1_turn = True
    player_2_turn = False
    player_turn = "player1"
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    captureMoves = []
    X = 801
    Y = 801
    #piece images
    black_pawn_1 = pygame.image.load("imgs/black_pawn.png").convert_alpha()
    black_pawn_2 = pygame.image.load("imgs/black_pawn.png").convert_alpha()
    black_pawn_3 = pygame.image.load("imgs/black_pawn.png").convert_alpha()
    black_pawn_4 = pygame.image.load("imgs/black_pawn.png").convert_alpha()
    black_pawn_5 = pygame.image.load("imgs/black_pawn.png").convert_alpha()
    black_pawn_6 = pygame.image.load("imgs/black_pawn.png").convert_alpha()
    black_pawn_7 = pygame.image.load("imgs/black_pawn.png").convert_alpha()
    black_pawn_8 = pygame.image.load("imgs/black_pawn.png").convert_alpha()
    black_queen_1 = pygame.image.load("imgs/black_queen.png").convert_alpha()
    black_king_1 = pygame.image.load("imgs/black_king.png").convert_alpha()
    black_rook_1 = pygame.image.load("imgs/black_rook.png").convert_alpha()
    black_rook_2 = pygame.image.load("imgs/black_rook.png").convert_alpha()
    black_bishop_1 = pygame.image.load("imgs/black_bishop.png").convert_alpha()
    black_bishop_2 = pygame.image.load("imgs/black_bishop.png").convert_alpha()
    black_knight_1 = pygame.image.load("imgs/black_knight.png").convert_alpha()
    black_knight_2 = pygame.image.load("imgs/black_knight.png").convert_alpha()

    white_pawn_1 = pygame.image.load("imgs/white_pawn.png").convert_alpha()
    white_pawn_2 = pygame.image.load("imgs/white_pawn.png").convert_alpha()
    white_pawn_3 = pygame.image.load("imgs/white_pawn.png").convert_alpha()
    white_pawn_4 = pygame.image.load("imgs/white_pawn.png").convert_alpha()
    white_pawn_5 = pygame.image.load("imgs/white_pawn.png").convert_alpha()
    white_pawn_6 = pygame.image.load("imgs/white_pawn.png").convert_alpha()
    white_pawn_7 = pygame.image.load("imgs/white_pawn.png").convert_alpha()
    white_pawn_8 = pygame.image.load("imgs/white_pawn.png").convert_alpha()
    white_queen_1 = pygame.image.load("imgs/white_queen.png").convert_alpha()
    white_king_1 = pygame.image.load("imgs/white_king.png").convert_alpha()
    white_rook_1 = pygame.image.load("imgs/white_rook.png").convert_alpha()
    white_rook_2 = pygame.image.load("imgs/white_rook.png").convert_alpha()
    white_bishop_1 = pygame.image.load("imgs/white_bishop.png").convert_alpha()
    white_bishop_2 = pygame.image.load("imgs/white_bishop.png").convert_alpha()
    white_knight_1 = pygame.image.load("imgs/white_knight.png").convert_alpha()
    white_knight_2 = pygame.image.load("imgs/white_knight.png").convert_alpha()


    pawns = ["black_pawn_1", "black_pawn_2", "black_pawn_3", "black_pawn_4", "black_pawn_5", "black_pawn_6", "black_pawn_7", "black_pawn_8",
                        "white_pawn_1", "white_pawn_2","white_pawn_3", "white_pawn_4","white_pawn_5", "white_pawn_6", "white_pawn_7", "white_pawn_8"]
    bishops = ["black_bishop_1", "black_bishop_2", "white_bishop_1", "white_bishop_2"]
    queens = ["white_queen_1", "black_queen_1"]
    kings = ["white_king_1", "black_king_1"]
    rooks = ["white_rook_1", "white_rook_2", "black_rook_1", "black_rook_2"]
    knights = ["white_knight_1", "white_knight_2", "black_knight_1", "black_knight_2"]

    #player pieces
    player2 = ["black_pawn_1", "black_pawn_2", "black_pawn_3", "black_pawn_4", "black_pawn_5", "black_pawn_6", "black_pawn_7", "black_pawn_8", "black_bishop_1", "black_bishop_2", "black_knight_1", "black_knight_2", "black_rook_1", "black_rook_2", "black_queen_1", "black_king_1"]
    player1 = ["white_pawn_1", "white_pawn_2", "white_pawn_3", "white_pawn_4", "white_pawn_5", "white_pawn_6", "white_pawn_7", "white_pawn_8", "white_bishop_1", "white_bishop_2", "white_knight_1", "white_knight_2", "white_rook_1", "white_rook_2", "white_queen_1", "white_king_1"]
    players = {
        "player1": player1,
        "player2": player2
    }
    #sets up the board
    def __init__(self, board):
        self.board = board
    #image list for now all decoy pos
    #TODO:
    # this honestly looks disgusting and very redundent since the image list will have to be updated regardless cuz of pawn promotion
    # the plan is to create a function to "register" add it to the image list
    image_list = [
        {
            "piece":"black_pawn_1",
            "image": pygame.transform.scale(black_pawn_1, (100, 100)),
            "rect": black_pawn_1.get_rect(topleft=(20, 20))
        },
        {
            "piece": "black_pawn_2",
            "image": pygame.transform.scale(black_pawn_2, (100, 100)),
            "rect": black_pawn_2.get_rect(topleft=(20, 20))
        },
        {
            "piece": "black_pawn_3",
            "image": pygame.transform.scale(black_pawn_3, (100, 100)),
            "rect": black_pawn_3.get_rect(topleft=(20, 20))
        },
        {
            "piece": "black_pawn_4",
            "image": pygame.transform.scale(black_pawn_4, (100, 100)),
            "rect": black_pawn_4.get_rect(topleft=(20, 20))
        },
        {
            "piece": "black_pawn_5",
            "image": pygame.transform.scale(black_pawn_5, (100, 100)),
            "rect": black_pawn_5.get_rect(topleft=(20, 20))
        },
        {
            "piece":"black_pawn_6",
            "image": pygame.transform.scale(black_pawn_6, (100, 100)),
            "rect": black_pawn_6.get_rect(topleft=(20, 20))
        },
        {
            "piece": "black_pawn_7",
            "image": pygame.transform.scale(black_pawn_7, (100, 100)),
            "rect": black_pawn_7.get_rect(topleft=(20, 20))
        },
        {
            "piece": "black_pawn_8",
            "image": pygame.transform.scale(black_pawn_8, (100, 100)),
            "rect": black_pawn_8.get_rect(topleft=(20, 20))
        },
        {
            "piece": "black_queen_1",
            "image": pygame.transform.scale(black_queen_1, (100, 100)),
            "rect": black_queen_1.get_rect(topleft=(20, 20))
        },
        {
            "piece": "black_king_1",
            "image": pygame.transform.scale(black_king_1, (100, 100)),
            "rect": black_king_1.get_rect(topleft=(20, 20))
        },
        {
            "piece": "black_rook_1",
            "image": pygame.transform.scale(black_rook_1, (100, 100)),
            "rect": black_rook_1.get_rect(topleft=(20, 20))
        },
        {
            "piece": "black_rook_2",
            "image": pygame.transform.scale(black_rook_2, (100, 100)),
            "rect": black_rook_2.get_rect(topleft=(20, 20))
        },
        {
            "piece": "black_bishop_1",
            "image": pygame.transform.scale(black_bishop_1, (100, 100)),
            "rect": black_bishop_1.get_rect(topleft=(20, 20))
        },
        {
            "piece": "black_bishop_2",
            "image": pygame.transform.scale(black_bishop_2, (100, 100)),
            "rect": black_bishop_2.get_rect(topleft=(20, 20))
        },
        {
            "piece": "black_knight_1",
            "image": pygame.transform.scale(black_knight_1, (100, 100)),
            "rect": black_knight_1.get_rect(topleft=(20, 20))
        },
        {
            "piece": "black_knight_2",
            "image": pygame.transform.scale(black_knight_1, (100, 100)),
            "rect": black_knight_1.get_rect(topleft=(20, 20))
        },
        {
            "piece": "white_pawn_1",
            "image": pygame.transform.scale(white_pawn_1, (100, 100)),
            "rect": white_pawn_1.get_rect(topleft=(40, 40))
        },
        {
            "piece": "white_pawn_2",
            "image": pygame.transform.scale(white_pawn_1, (100, 100)),
            "rect": white_pawn_2.get_rect(topleft=(40, 40))
        },
        {
            "piece": "white_pawn_3",
            "image": pygame.transform.scale(white_pawn_1, (100, 100)),
            "rect": white_pawn_3.get_rect(topleft=(40, 40))
        },
        {
            "piece": "white_pawn_4",
            "image": pygame.transform.scale(white_pawn_1, (100, 100)),
            "rect": white_pawn_4.get_rect(topleft=(40, 40))
        },
        {
            "piece": "white_pawn_5",
            "image": pygame.transform.scale(white_pawn_1, (100, 100)),
            "rect": white_pawn_5.get_rect(topleft=(40, 40))
        },        {
            "piece": "white_pawn_6",
            "image": pygame.transform.scale(white_pawn_1, (100, 100)),
            "rect": white_pawn_6.get_rect(topleft=(40, 40))
        },
        {
            "piece": "white_pawn_7",
            "image": pygame.transform.scale(white_pawn_1, (100, 100)),
            "rect": white_pawn_7.get_rect(topleft=(40, 40))
        },
        {
            "piece": "white_pawn_8",
            "image": pygame.transform.scale(white_pawn_1, (100, 100)),
            "rect": white_pawn_8.get_rect(topleft=(40, 40))
        },
        {
            "piece": "white_queen_1",
            "image": pygame.transform.scale(white_queen_1, (100, 100)),
            "rect": white_queen_1.get_rect(topleft=(40, 40))
        },
        {
            "piece": "white_king_1",
            "image": pygame.transform.scale(white_king_1, (100, 100)),
            "rect": white_king_1.get_rect(topleft=(40, 40))

        },
        {
            "piece": "white_rook_1",
            "image": pygame.transform.scale(white_rook_1, (100, 100)),
            "rect": white_rook_1.get_rect(topleft=(40, 40))
        },
        {
            "piece": "white_rook_2",
            "image": pygame.transform.scale(white_rook_1, (100, 100)),
            "rect": white_rook_2.get_rect(topleft=(40, 40))
        },
        {
            "piece": "white_bishop_1",
            "image": pygame.transform.scale(white_bishop_1, (100, 100)),
            "rect": white_bishop_1.get_rect(topleft=(40, 40))
        },
        {
            "piece": "white_bishop_2",
            "image": pygame.transform.scale(white_bishop_1, (100, 100)),
            "rect": white_bishop_2.get_rect(topleft=(40, 40))
        },
        {
            "piece": "white_knight_1",
            "image": pygame.transform.scale(white_knight_1, (100, 100)),
            "rect": white_knight_1.get_rect(topleft=(40, 40))
        },
        {
            "piece": "white_knight_2",
            "image": pygame.transform.scale(white_knight_1, (100, 100)),
            "rect": white_knight_2.get_rect(topleft=(40, 40))
        }
    ]
    #draws board on the screen and pieces
    def draw_board(self):
        square_size = 100
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    color = (200, 200, 200)
                else:
                    color = (50, 50, 50)
                pygame.draw.rect(self.screen, color, (j * square_size, i * square_size, square_size, square_size))
        for i in self.image_list:
            self.screen.blit(i["image"], i["rect"])

    def coordinatesToPosition(self, x, y, square_size=100):
        if -1<= x < self.X and -1<= y < self.Y:
            return chr(97 + int(x // square_size))+str(8 - int(y // square_size))
    def positionToCoordinates(self, position, square_size=100):
        row = ord(position[0]) - 97
        col = 8 - int(position[1])
        return row * square_size, col * square_size

    #TODO: rename this to something more meaningful
    def newBoard(self):
        for i in range(8):
            for j in range(8):
                self.board[chr(97+i)+str(j+1)] = " "
        #black pieces
        self.setPiecePosition("black_pawn_1", "a7")
        self.setPiecePosition("black_pawn_2", "b7")
        self.setPiecePosition("black_pawn_3", "c7")
        self.setPiecePosition("black_pawn_4", "d7")
        self.setPiecePosition("black_pawn_5", "e7")
        self.setPiecePosition("black_pawn_6", "f7")
        self.setPiecePosition("black_pawn_7", "g7")
        self.setPiecePosition("black_pawn_8", "h7")
        self.setPiecePosition("black_queen_1", "d8")
        self.setPiecePosition("black_king_1", "e8")
        self.setPiecePosition("black_rook_1", "a8")
        self.setPiecePosition("black_rook_2", "h8")
        self.setPiecePosition("black_bishop_1", "c8")
        self.setPiecePosition("black_bishop_2", "f8")
        self.setPiecePosition("black_knight_1", "b8")
        self.setPiecePosition("black_knight_2", "g8")
        #white pieces
        self.setPiecePosition("white_pawn_1", "a2")
        self.setPiecePosition("white_pawn_2", "b2")
        self.setPiecePosition("white_pawn_3", "c2")
        self.setPiecePosition("white_pawn_4", "d2")
        self.setPiecePosition("white_pawn_5", "e2")
        self.setPiecePosition("white_pawn_6", "f2")
        self.setPiecePosition("white_pawn_7", "g2")
        self.setPiecePosition("white_pawn_8", "h2")
        self.setPiecePosition("white_queen_1", "d1")
        self.setPiecePosition("white_king_1", "e1")
        self.setPiecePosition("white_rook_1", "a1")
        self.setPiecePosition("white_rook_2", "h1")
        self.setPiecePosition("white_bishop_1", "c1")
        self.setPiecePosition("white_bishop_2", "f1")
        self.setPiecePosition("white_knight_1", "b1")
        self.setPiecePosition("white_knight_2", "g1")


    #gets the instace of the board
    def getBoard(self):
        return self.board
    def getPlayerPieces(self, player:str)->list:
       return self.player1 if player == "player1" else self.player2
    def getPieceOwner(self, piece:str)->str:
        return "player1" if piece in self.player1 else "player2"
    def getPosition(self, piece):
        for key, value in self.board.items():
            if value == piece:
                return key
        return None

    #stores new peice location
    def setPiecePosition(self, piece, position):
        old_pos = self.getPosition(piece)
        if old_pos != position:
            for i in self.image_list:
                if i["piece"] == piece:
                    i["rect"].topleft = self.positionToCoordinates(position)
                    self.screen.blit(i["image"], i["rect"].topleft)
                    self.board[position] = piece
                    self.board[old_pos] = None
                    break
            if old_pos is not None:
                self.board[old_pos] = None

    #TODO:
    #game mechanics


    def getCurrentPlayer(self):
        return self.player_turn
    #TODO: RENAME THIS
    def getPlayer1Status(self):
        return self.player_1_turn
    def getPlayer2Status(self):
        return self.player_2_turn
    def setCurrentPlayer(self, player:str)->None:
        if player not in ["player1", "player2"]:
            return
        if player == self.player_turn:
            return
        self.player_turn = player

    def getCurrentPlayerTurn(self):
        return self.player_turn


    def avalaibleMoves(self, piece)->list:
        moves = []

        if self.isPawn(piece):
            for d in self.pawnMoves(piece):
                moves.append(d)
        if self.isBishop(piece):
            for d in self.bishopMoves(piece):
                moves.append(d)
        if self.isKnight(piece):
            for d in self.knightMovements(piece):
                moves.append(d)
        if self.isRook(piece):
            for d in self.rookMoves(piece):
                moves.append(d)
        if self.isQueen(piece):
            for x in self.rookMoves(piece):
                moves.append(x)
            for x in self.bishopMoves(piece):
                moves.append(x)
        if self.isKing(piece):
            for d in self.kingMoves(piece):
                moves.append(d)

        return moves

    def isEligbleMove(self, piece, position:str)->bool:
        availableMoves = self.avalaibleMoves(piece)
        currentPlayer = self.getCurrentPlayer()
        if currentPlayer != self.getPieceOwner(piece) :
            return False
        if position not in availableMoves:
            return False
        return True
    #TODO
    def nextTurn(self)->None:
        self.setCurrentPlayer("player2" if self.player_turn == "player1" else "player1")
    def isCheck(self, player)->bool:
        return False
    def isCheckMate(self, player)->bool:
        return False

    #peice mechanics
    def isPawn(self, piece)->bool:
        return True if piece in self.pawns else False

    def isBishop(self, piece)->bool:
        return True if piece in self.bishops else False
    def isKnight(self, piece)->bool:
        return True if piece in self.knights else False
    def isRook(self, piece)->bool:
        return True if piece in self.rooks else False
    def isQueen(self, piece)->bool:
        return True if piece in self.queens else False
    def isKing(self, piece)->bool:
        return True if piece in self.kings else False
    def instanceOfPiece(self, piece)->bool:
        for image in self.image_list:
            if image["piece"] == piece:
                return True
        return False

    def getPossibleCaptures(self):
        return  self.captureMoves
    def ableToCapture(self, piece, position, targetPiece ):
        self.captureMoves = [(piece, position, targetPiece)]
    #TODO
    def onCapture(self)->None:
        return
    def bishopMoves(self, piece)->list[str]:
        moves = []
        player = "player1" if piece in self.player1 else "player2"

        if self.instanceOfPiece(piece):
            pos = list(self.getPosition(piece))
            #coordinates not a random var name
            x = ord(pos[0])
            y=int(pos[1])
            #all possible directions
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

            for dx, dy in directions:
                for i in range(1, 8):

                    nx = x + i * dx
                    ny = y + i * dy
                    currentPiece = self.getBoard().get(chr(x + dx) + str(y + dy), " ")
                    if 97 <= nx <= 104 and 1 <= ny <= 8:
                        if currentPiece == " ":
                            moves.append(chr(x + i * dx) + str(y + i * dy))
                        elif currentPiece  != " " and currentPiece not in self.getPlayerPieces(player) :
                            moves.append(chr(x + dx) + str(y + dy))
                            self.ableToCapture(piece, (x+dx, y+dy), currentPiece)
                        else:
                            break
                    else:
                        break
        return moves

    def pawnMoves(self, piece)-> list[str]:
        moves = []
        if self.instanceOfPiece(piece):
            pos = list(self.getPosition(piece))
            x = ord(pos[0])
            y=int(pos[1])

            # white piece movement
            if piece in self.player1:
                directions = [(0, 1)]
                if y == 2:
                    print(directions)
                    directions.append((0, 2))
                for dx, dy in directions:
                    nx, ny =  x, y + dy
                    if 97 <= nx <= 104 and 1 <= ny <= 8:
                        if self.board.get(chr(x ) + str(y + dy), " ") == " ":
                            moves.append(chr(x ) + str(y + dy))
                        else:
                            break
                    else:
                        break
                #diagnol moves (special case)
                for dx, dy in [(1,1), (-1, 1)]:
                    nx, ny = x + dx, y + dy
                    if 97 <= nx <= 104 and 1 <= ny <= 8:
                        currentPiece = self.board.get(chr(x + dx) + str(y + dy), " ")
                        if currentPiece!= " " and currentPiece not in self.getPlayerPieces("player1"):
                            moves.append(chr(x + dx) + str(y + dy))
                            self.ableToCapture(piece, (x+dx, y+dy), self.getBoard().get(chr(x + dx) + str(y + dy), " "))
                        else:
                            break
                    else:
                        break
            #black pawn movements
            if piece in self.player2:
                directions = [(0, -1)]
                if y == 7:
                    directions.append((0, -2))

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 97 <= nx <= 104 and 1 <= ny <= 8:
                        if self.board.get(chr(x + dx) + str(y + dy), " ") == " ":
                            moves.append(chr(x + dx) + str(y + dy))
                        else:
                            break
                    else:
                        break
                #diagnol moves
                for dx, dy in [(1,-1), (-1, -1)]:
                    nx, ny = x + dx, y + dy
                    if 97 <= nx <= 104 and 1 <= ny <= 8:
                        currentPiece = self.board.get(chr(x + dx) + str(y + dy), " ")
                        if currentPiece != " " and currentPiece not in self.getPlayerPieces("player2"):
                            moves.append(chr(x + dx) + str(y + dy))
                            self.ableToCapture(piece, (x+dx, y+dy), self.getBoard().get(chr(x + dx) + str(y + dy), " "))
                        else:
                            break
                    else:
                        break

        return moves

    def knightMovements(self, piece)->list[str]:

        directions = [(2, 1), (1, 2), (-2, 1), (-1, 2),(2, -1), (1, -2), (-2, -1), (-1, -2)]
        player = "player1" if piece in self.player1 else "player2"
        moves = []
        if self.instanceOfPiece(piece):
            pos = list(self.getPosition(piece))
            x = ord(pos[0])
            y=int(pos[1])
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 97 <= nx <= 104 and 1 <= ny <= 8:
                    currentPiece = self.getBoard().get(chr(x + dx) + str(y + dy), " ")
                    if self.getBoard().get(chr(x + dx) + str(y + dy), " ") == " ":
                        moves.append(chr(x + dx) + str(y + dy))
                    elif currentPiece != " " and currentPiece not in self.getPlayerPieces(player):
                        moves.append(chr(x + dx) + str(y + dy))
                        self.ableToCapture(piece, (x+dx, y+dy), currentPiece)

        return  moves

    def rookMoves(self, piece)->list[str]:
            moves = []
            player = "player1" if piece in self.player1 else "player2"
            if self.instanceOfPiece(piece):
                pos = list(self.getPosition(piece))
                x = ord(pos[0])
                y=int(pos[1])
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                for dx, dy in directions:
                    for i in range(1, 8):
                        nx, ny = x + i*dx, y + i*dy
                        if 97 <= nx <= 104 and 1 <= ny <= 8:
                            currentPiece = self.getBoard().get(chr(x + dx) + str(y + dy), " ")
                            if currentPiece == " ":
                                moves.append(chr(nx) + str(ny))
                            elif currentPiece not in self.getPlayerPieces(player):
                                moves.append(chr(nx) + str(ny))
                                self.ableToCapture(piece, (x+dx, y+dy), currentPiece)
                                break
                            else:
                                break
                        else:
                            break
            return moves


    #TODO: add castling
    def kingMoves(self, piece)->list[str]:
        player = "player1" if piece in self.player1 else "player2"
        pos = list(self.getPosition(piece))
        x = ord(pos[0])
        y=int(pos[1])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        moves = []
        if self.instanceOfPiece(piece):
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 97 <= nx <= 104 and 1 <= ny <= 8:
                    currentPiece = self.getBoard().get(chr(nx) + str(ny), " ")
                    if currentPiece == " ":
                        moves.append(chr(nx) + str(ny))
                    elif currentPiece not in self.getPlayerPieces(player):
                        moves.append(chr(nx) + str(ny))
                        self.ableToCapture(piece, (nx, ny), currentPiece)
                else:
                    break
        return moves


    def newGame(self):
        self.newBoard()
