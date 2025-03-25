from chessPiece import Piece


class Player:
    def __init__(self):
        self.player_id = None
        self.pieces = {}
        self.turn = False


    def set_player_id(self, player_id):
        self.player_id = player_id
    def get_player_id(self):
        return self.player_id
    def get_pieces(self):
        return self.pieces
    def get_turn(self):
        return self.turn
    def set_turn(self, turn):
        self.turn = turn
    def add_piece(self, piece: Piece):
        self.pieces[piece.getPieceName()] = piece
    def add_pieces(self, pieces:list):
        for piece in pieces:
            self.pieces[piece.getPieceName()] = piece
    def getSpeficPiece(self, name)-> Piece:
        for key, value in self.pieces.items():
            if value.getPieceName() == name:
                return value
    def remove_piece(self, piece):
        del self.pieces[piece.getPieceName()]
