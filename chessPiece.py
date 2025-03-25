import pygame



class Piece :
    pygame.init()
    def __init__(self, name :str, player_type :str, position:str):
        self.name = name
        self.player_type = player_type
        self.position = position
    #image list
    pieceList = []
    #piece list of all instances
    pieces = []
    eligbleMoves = []

    def getPlayerType(self):
        return self.player_type

    def getPosition(self):
        return self.position
    def setPosition(self, newPosition):
        self.position = newPosition
    def getPieceByPosition(self, position):
        for piece in self.pieces:
            if piece.getPosition() == position:
                return piece
    def ableToCapture(self)-> bool:
        return False
    def getPieceName(self) -> str:
        return self.name
    def addToEligibleMoves(self, pos):
        self.eligbleMoves.append([self.getPieceName(), pos])
    def getPieceType(self) -> str:
        if "pawn" in self.getPieceName():
            return "pawn"
        if "queen" in self.getPieceName():
            return "queen"
        if "king" in self.getPieceName():
            return "king"
        if "rook" in self.getPieceName():
            return "rook"
        if "bishop" in self.getPieceName():
            return "bishop"
        if "knight" in self.getPieceName():
            return "knight"

    def createPieceName(self, pieceType:str, player_type):
        color ="white" if player_type == "player_1" else "black"
        i =1
        while True:
            name = color + "_" + pieceType + "_"+str(i)
            if name not in self.pieces:
                self.pieces.append(name)
                return name
            i+=1



    def registerPiece(self):
        from events import EventManger
        player= "white" if self.player_type == "player_1" else "black"

        img = "imgs/"+player + "_" + self.getPieceType() + ".png"
        currentPiece = pygame.image.load(img).convert_alpha()
        if self.getPieceName() not in self.pieces:
            return
        pos = EventManger.board.positionToCoordinates(self.getPosition(), square_size=100)
        EventManger.board.setPiecePosition(self.getPieceName(), self.getPosition())
        self.pieceList.append(
            {
                "name":self.getPieceName(),
                "img":pygame.transform.scale(currentPiece, (100, 100)),
                "rect":currentPiece.get_rect(topleft=(pos[0], pos[1]))

            }

        )
        return




class Pawn(Piece):

    def __init__(self, player_type, position):
        super().__init__(self.createPieceName("pawn", player_type), player_type,position)
        self.position = position
        self.player_type = player_type
        self.registerPiece()


class Rook(Piece):
    def __init__(self, player_type, position):
        super().__init__(self.createPieceName("rook", player_type), player_type,position)
        self.position = position
        self.player_type = player_type
        self.registerPiece()
        self.hasMoved = False

    def setPosition(self, pos):
        self.position = pos
        self.hasMoved = True

class Knight(Piece):
    def __init__(self, player_type, position):
        super().__init__(self.createPieceName("knight", player_type), player_type,position)
        self.position = position
        self.player_type = player_type
        self.registerPiece()

class Bishop(Piece):
    def __init__(self, player_type, position):
        super().__init__(self.createPieceName("bishop", player_type), player_type, position,)
        self.position = position
        self.player_type = player_type
        self.registerPiece()



class Queen(Piece):
    def __init__(self, player_type, position):
        super().__init__(self.createPieceName("queen", player_type), player_type, position)
        self.position = position
        self.player_type = player_type
        self.registerPiece()

class King(Piece):
    def __init__(self, player_type, position):
        super().__init__(self.createPieceName("king", player_type), player_type, position)
        self.position = position
        self.player_type = player_type
        self.registerPiece()
        self.hasMoved = False

    def setPosition(self, pos):
        self.position = pos
        self.hasMoved = True


