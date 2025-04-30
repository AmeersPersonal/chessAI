
from board import *
from player import Player
from chessPiece import *
from ai.googleGemResponse import *
from gui import *

class EventManger:
    board = Board()
    board.newBoard()
    def __init__(self, player1: Player, player2: Player ):
        self.player1 = player1
        self.player2 = player2
        self.moves ={}
        self.opposing_moves = {}
        self.opposing_potential_captures= []
        self.potenial_captures_piece= []





    #connects boards and piece pos
    def set_position(self, piece, position):
        self.board.get_board()[piece.getPosition()] =  ' '
        piece.set_position(position)
        self.board.setPiecePosition(piece.getPieceName(), position)

    def near_by_king_pieces(self, piece):
        pieces= []
        if not isinstance(piece, Piece):
            return False

        # Movement directions
        vh_directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        diagonal_directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        directions = vh_directions + diagonal_directions

        # Identify the player and the opponent
        player = self.player1 if piece in self.player1.get_pieces().values() else self.player2
        opposing_player = self.player2 if player.get_player_id() == self.player1.get_player_id() else self.player1
        player.get_pieces()
        king = [k for k in player.get_pieces() if isinstance(k, Piece) and k.getPieceType() == "king"][0]
        king_x, king_y = ord(king.getPosition()[0]), int(king.getPosition()[1])

        for dx, dy in directions:
            pos_x, pos_y = king_x + dx, king_y + dy
            pos = chr(pos_x) +str(pos_y)
            near_by_piece = self.board.get_board().get(pos, " ")
            if near_by_piece == " ":
                continue
            if near_by_piece in player.get_pieces():
                pieces.append(near_by_piece)

        return pieces




    def game_status(self):
        # this will return an int
        # 0 -> game is continuing
        # 1 -> eneded
        # 2 -> draw

        pass

    def pawn_promotion_event(self,player, pawn, selectedPiece="queen"):
        if not isinstance(pawn, Pawn):
            return
        pos = pawn.getPosition()
        pos_1 = list(pos)
        if player.get_player_id() == "player_1" and pos_1[1] == "8":
            Piece.pieceList =[img for img in Piece.pieceList if img["name"] != pawn.getPieceName()]


        elif player.get_player_id() == "player_2" and pos_1[1] == "1":
            Piece.pieceList =[img for img in Piece.pieceList if img["name"] != pawn.getPieceName()]
        else:
            return
        new_piece = None

        if selectedPiece == "queen":
            new_piece = Queen(player.get_player_id(), pos)
        if selectedPiece == "rook":
            new_piece = Rook(player.get_player_id(), pos)
        if selectedPiece == "bishop":
            new_piece = Bishop(player.get_player_id(), pos)
        if selectedPiece == "knight":
            new_piece = Knight(player.get_player_id(), pos)


        player.add_piece(new_piece)










    def pawn_movement_event(self, piece):

        diagonal = []
        if not isinstance(piece, Pawn):

            return self.moves
        pos = list(piece.getPosition())
        # x-y coordinates
        x = ord(pos[0])
        y = int(pos[1])
        # sets up foward movements for pawns
        player = self.player1 if piece in self.player1.get_pieces().values() else self.player2

        if player.get_player_id() == self.player1.get_player_id():
            directions=[(0, 1)]
            if y == 2:
                directions.append((0,2))
            directions.append((1, 1))
            directions.append((-1, 1))
            diagonal.append((1,1))
            diagonal.append((-1,1))

        else:
            directions=[(0, -1)]

            if y == 7:

                directions.append((0,-2))
            directions.append((1, -1))
            directions.append((-1, -1))
            diagonal.append((1,-1))
            diagonal.append((-1,-1))

        # creats a new key and value if not already exists
        if piece.getPieceName() not in self.moves.keys():
            self.moves[piece.getPieceName()] = []

        for dx, dy in directions:
            nx= x+dx
            ny = y + dy
            pos2 = chr(nx) + str(ny)
            nearByPiece= self.board.get_board().get(pos2, " ")

            if pos2 in self.moves[piece.getPieceName()]:
                continue
            if x == 0  and  self.board.get_board().get(pos2, " ") != " ":
                continue
            if (dx, dy) in diagonal:
                if self.board.get_board().get(pos2) == " ":
                    continue
                if self.board.get_board().get(pos2) is  None:
                    continue
                if nearByPiece in player.get_pieces():
                    continue
                self.potenial_captures_piece.append(nearByPiece)
                self.moves[piece.getPieceName()].append(pos2)
            self.moves[piece.getPieceName()].append(pos2)

        return self.moves


    def bishop_movement_event(self, piece):

        player = self.player1 if piece in self.player1.get_pieces().values() else self.player2


        pos = list(piece.getPosition())
        # coordinates not a random var name
        x = ord(pos[0])
        y = int(pos[1])
        # all possible directions
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        if piece.getPieceName() not in self.moves.keys():
            self.moves[piece.getPieceName()] = []

        for dx, dy in directions:
            for i in range(1, 8):
                nx =x + i*dx
                ny = y + i*dy
                pos2 = chr(nx) + str(ny)


                nearByPiece = self.board.get_board().get(pos2, " ")
                if ord('a')<= nx <= ord('h') and 1 <= ny <=8:


                    if nearByPiece != " " and nearByPiece not in player.get_pieces():
                        self.moves[piece.getPieceName()].append(pos2)
                        self.potenial_captures_piece.append(nearByPiece)
                        break
                    elif nearByPiece == " ":
                        self.moves[piece.getPieceName()].append(pos2)

                    else:
                        break
                else:
                    break
      



        return self.moves

    def rook_movement_event(self, piece):
        player = self.player1 if piece in self.player1.get_pieces().values() else self.player2
        pos = list(piece.getPosition())
        x = ord(pos[0])
        y = int(pos[1])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        if piece.getPieceName() not in self.moves.keys():
            self.moves[piece.getPieceName()] = []
        for dx, dy in directions:
            for i in range (1, 8):
                nx = x + i*dx
                ny = y + i*dy
                pos2 = chr(nx) + str(ny)
                nearByPiece = self.board.get_board().get(pos2, " ")

                if ord('a')<= nx <= ord('h') and 1 <= ny <=8:
                    if nearByPiece != " " and nearByPiece not in player.get_pieces():
                        self.moves[piece.getPieceName()].append(pos2)
                        self.potenial_captures_piece.append(nearByPiece)
                        break
                    elif nearByPiece == " ":
                        self.moves[piece.getPieceName()].append(pos2)
                    else:
                        break
                else:
                    break

        return self.moves




    def knight_movement_event(self, piece):
        player = self.player1 if piece in self.player1.get_pieces().values() else self.player2
        pos = list(piece.getPosition())
        x = ord(pos[0])
        y = int(pos[1])
        directions = [(2, 1), (1, 2), (-2, 1), (-1, 2),(2, -1), (1, -2), (-2, -1), (-1, -2)]
        if piece.getPieceName() not in self.moves.keys():
            self.moves[piece.getPieceName()] = []
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            pos2 = chr(nx) + str(ny)
            nearByPiece = self.board.get_board().get(pos2, " ")
            if ord('a')<= nx <= ord('h') and 1 <= ny <=8:
                if nearByPiece != " " and nearByPiece not in player.get_pieces():
                    self.moves[piece.getPieceName()].append(pos2)
                    self.potenial_captures_piece.append(nearByPiece)
                elif nearByPiece == " ":
                    self.moves[piece.getPieceName()].append(pos2)
        return self.moves


    def queen_movement_event(self, piece):
        if not isinstance(piece, Queen):
            return

        if piece.getPieceName() not in self.moves.keys():
            self.moves[piece.getPieceName()] = []

        bishop_moves = self.bishop_movement_event(piece)
        rook_moves = self.rook_movement_event(piece)
        self.moves[piece.getPieceName()].extend(bishop_moves)
        self.moves[piece.getPieceName()].extend(rook_moves)

        return self.moves

    def king_movement_event(self, piece):
        if not isinstance(piece, King):
            return

        player = self.player1 if piece in self.player1.get_pieces().values() else self.player2
        pos= piece.getPosition()
        pos_x = ord(pos[0])
        pos_y = int(pos[1])
        vh_directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        diagonal_directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        directions = vh_directions + diagonal_directions

        if piece.getPieceName() not in self.moves.keys():
            self.moves[piece.getPieceName()] = []

        for dx, dy in directions:
            nx = pos_x + dx
            ny = pos_y + dy
            pos2 = chr(nx) + str(ny)
            nearByPiece = self.board.get_board().get(pos2, " ")
            if nearByPiece == " ":
                self.moves[piece.getPieceName()].append(pos2)
            if nearByPiece != " ":
                if nearByPiece in player.get_pieces():
                    continue
                else:
                    self.moves[piece.getPieceName()].append(pos2)




        return self.moves

    def castling_moves(self, king):

        if king.getPieceType().lower() != "king" or king.hasMoved:
            return self.moves

        player = self.player1 if king in self.player1.get_pieces() else self.player2
        back_rank = "1" if player == self.player1 else "8"
        board_state = self.board.get_board()

        # Short castling
        if self.can_castle(king, "h" + back_rank):
            self.moves[king.getPieceName()].append("h" + back_rank)

        # Long castling
        if self.can_castle(king, "a" + back_rank):
           self.moves[king.getPieceName()].append("a" + back_rank)

        return self.moves

    def can_castle(self, king, rook_pos):
        rook = self.board.get_board().get(rook_pos, " ")
        if not isinstance(king, King) or isinstance(king, King) and  king.hasMoved:
            return False

        # Determine clear path between king and rook
        king_x = ord(king.getPosition()[0])
        rook_x = ord(rook_pos[0])
        y = rook_pos[1]
        step = 1 if rook_x > king_x else -1

        for x in range(king_x + step, rook_x, step):
            pos = chr(x) + y
            if self.board.get_board().get(pos, " ") != " ":
                return False  # Path not clear

        # Optionally: Check if squares are under attack (not implemented here)
        return True

    def perform_castling_by_rook_position(self, king, rook_pos, board_state):
        """
        Executes castling by identifying the castling side from the rook's position.
        Assumes the move is legal and the king has not moved.
        Parameters:
            king: the king piece object
            rook_pos: the square (e.g., 'h1' or 'a8') where the rook is currently located
        """
        player = self.player1 if king in self.player1.get_pieces() else self.player2
        back_rank = "1" if player == self.player1 else "8"
        king_from = "e" + back_rank

        if rook_pos == "h" + back_rank:
            # Kingside castling
            king_to = "g" + back_rank
            rook_to = "f" + back_rank
        elif rook_pos == "a" + back_rank:
            # Queenside castling
            king_to = "c" + back_rank
            rook_to = "d" + back_rank
        else:
            return
        rook = board_state.get(rook_to, " ")
        if isinstance(rook, Piece):
            # Move the king
            board_state[king_to] = king
            board_state[king_from] = " "
            king.setPosition(king_to)
            for img in Piece.pieceList:
                if img["name"] == king.getPieceName():
                    img["rect"]= self.board.positionToCoordinates(king_to)
                if img["name"] == rook:
                    img["rect"]= self.board.positionToCoordinates(rook_to)

            # Move the rook
            board_state[rook_to] = rook
            board_state[rook_pos] = " "
            rook.setPosition(rook_to)

            # Optionally mark them as having moved
            king.hasMoved = True  # Assumes this method exists


    def current_player(self):
        if self.player1.get_turn():
            return self.player1
        else:
            return self.player2



    #TODO implemnt check handling
    def register_moves(self):
        self.moves = {}
        pieces = self.current_player().get_pieces()
        player_2 = self.player2 if self.current_player().get_player_id() == self.player1.get_player_id() else self.player1
        opposing_pieces = player_2.get_pieces()
        for keys, values in pieces.items():
            if "pawn" == values.getPieceType():
                self.pawn_movement_event(values)
            if "bishop" == values.getPieceType():
                self.bishop_movement_event(values)
            if "knight" == values.getPieceType():
                self.knight_movement_event(values)
            if "queen" == values.getPieceType():
                self.queen_movement_event(values)
            if "rook" == values.getPieceType():
                self.rook_movement_event(values)
            if "king" == values.getPieceType():
                self.king_movement_event(values)
        for keys, values in opposing_pieces.items():
            if "pawn" == values.getPieceType():
                self.pawn_movement_event(values)
            if "bishop" == values.getPieceType():
                self.bishop_movement_event(values)
            if "knight" == values.getPieceType():
                self.knight_movement_event(values)
            if "queen" == values.getPieceType():
                self.queen_movement_event(values)
            if "rook" == values.getPieceType():
                self.rook_movement_event(values)
            if "king" == values.getPieceType():
                self.king_movement_event(values)
                self.castling_moves(values)

    def is_check(self):
        # Ensure exactly one king is present for the current player
        king_list = [k for k in self.current_player().get_pieces().values()
                     if isinstance(k, Piece) and k.getPieceType() == "king"]

        if not king_list:
            raise Exception("No king found for the current player.")
        if len(king_list) > 1:
            raise Exception("Multiple kings found for the current player.")

        king = king_list[0]

        # Check if the king is in the list of potentially captured pieces
        if king in self.potenial_captures_piece:
            return True

        return False

    def moves_out_of_check(self):
        moves_out_of_check = {}

        # Step 1: Get the current king's position and the pieces that are checking it
        player = self.player1 if self.current_player().get_player_id() == self.player1.get_player_id() else self.player2
        opposing_player = self.player2 if player == self.player1 else self.player1

        king_name = "white_king_1" if player.get_player_id() == self.player1.get_player_id() else "black_king_1"
        king_piece = player.getSpeficPiece(king_name)
        king_pos = king_piece.getPosition()

        # Find all pieces that are attacking the king
        pieces_causing_check = []
        for piece_name, positions in self.moves.items():
            if piece_name in opposing_player.get_pieces() and king_pos in positions:
                pieces_causing_check.append(piece_name)

        if not pieces_causing_check:
            return {}  # No check situation

        # If there are multiple pieces checking the king, only king moves can get out of check
        if len(pieces_causing_check) > 1:
            # Only king moves can get out of double check
            king_moves = self.moves.get(king_name, [])
            valid_king_moves = []
            for move in king_moves:
                # Check if the move would still be under attack
                under_attack = False
                for piece_name in pieces_causing_check:
                    piece = opposing_player.getSpeficPiece(piece_name)
                    if move in self.get_possible_moves(piece):
                        under_attack = True
                        break
                if not under_attack:
                    valid_king_moves.append(move)

            if valid_king_moves:
                moves_out_of_check[king_name] = valid_king_moves
            return moves_out_of_check

        # Single check situation - can capture, block, or move king
        checking_piece_name = pieces_causing_check[0]
        checking_piece = opposing_player.getSpeficPiece(checking_piece_name)
        checking_piece_pos = checking_piece.getPosition()

        # Step 2: Check if the attacking piece is capturable
        for piece_name, positions in self.moves.items():
            if piece_name in player.get_pieces() and checking_piece_pos in positions:
                if piece_name not in moves_out_of_check:
                    moves_out_of_check[piece_name] = []
                moves_out_of_check[piece_name].append(checking_piece_pos)

        # Step 3: Check if the check can be blocked (only if the checking piece is not a knight)
        if not checking_piece_name.startswith("knight"):
            x1, y1 = ord(checking_piece_pos[0]), int(checking_piece_pos[1])
            x2, y2 = ord(king_pos[0]), int(king_pos[1])

            blocking_positions = []
            if x1 == x2 or y1 == y2:  # Rook or Queen (straight line attack)
                step_x = 0 if x1 == x2 else (1 if x2 > x1 else -1)
                step_y = 0 if y1 == y2 else (1 if y2 > y1 else -1)
                curr_x, curr_y = x1 + step_x, y1 + step_y
                while (curr_x, curr_y) != (x2, y2):
                    blocking_positions.append(f"{chr(curr_x)}{curr_y}")
                    curr_x += step_x
                    curr_y += step_y

            elif abs(x1 - x2) == abs(y1 - y2):  # Bishop or Queen (diagonal attack)
                step_x = 1 if x2 > x1 else -1
                step_y = 1 if y2 > y1 else -1
                curr_x, curr_y = x1 + step_x, y1 + step_y
                while (curr_x, curr_y) != (x2, y2):
                    blocking_positions.append(f"{chr(curr_x)}{curr_y}")
                    curr_x += step_x
                    curr_y += step_y

            for piece_name, positions in self.moves.items():
                if piece_name in player.get_pieces() and piece_name != king_name:
                    for block_pos in blocking_positions:
                        if block_pos in positions:
                            if piece_name not in moves_out_of_check:

                                moves_out_of_check[piece_name] = []
                            moves_out_of_check[piece_name].append(block_pos)

        # Step 4: Check if the king can escape
        king_moves = self.moves.get(king_name, [])
        valid_king_moves = []
        for move in king_moves:
            # Check if the move would still be under attack
            under_attack = False
            for piece_name, positions in self.moves.items():
                if piece_name in opposing_player.get_pieces() and move in positions:
                    under_attack = True
                    break
            if not under_attack:
                valid_king_moves.append(move)

        if valid_king_moves:
            moves_out_of_check[king_name] = valid_king_moves

        return moves_out_of_check

    def pinned_pieces(self):
        pinned = []
        current_player = self.player1 if self.player1.get_player_id() == self.current_player().get_player_id() else self.player2
        opponent = self.player2 if current_player == self.player1 else self.player1

        king = next((piece for piece in current_player.get_pieces()
                     if isinstance(piece, Piece) and piece.getPieceType() == "king"), None)
        if not king:
            return pinned

        king_x, king_y = ord(king.getPosition()[0]), int(king.getPosition()[1])

        directions = {
            "straight": [(1, 0), (-1, 0), (0, 1), (0, -1)],
            "diagonal": [(1, 1), (-1, 1), (-1, -1), (1, -1)]
        }

        for dir_type, dirs in directions.items():
            for dx, dy in dirs:
                path = []
                for i in range(1, 8):
                    x = king_x + dx * i
                    y = king_y + dy * i
                    if not ('a' <= chr(x) <= 'h') or not (1 <= y <= 8):
                        break
                    pos = chr(x) + str(y)
                    piece = self.board.get_board().get(pos, " ")

                    if piece == " ":
                        continue

                    if piece in current_player.get_pieces():
                        if path:
                            break  # More than one friendly piece in this direction
                        path.append(piece)
                    else:
                        if not path:
                            break  # No friendly piece to be pinned
                        pinned_piece = path[0]
                        # Check if opponent piece can pin in this direction
                        if (dir_type == "straight" and piece.getPieceType() in ("rook", "queen")) or \
                                (dir_type == "diagonal" and piece.getPieceType() in ("bishop", "queen")):
                            pinned.append(pinned_piece)
                        break
        return pinned

    def pinned_piece_moves(self, piece):
        if piece not in self.pinned_pieces():
            return []

        # Logic to generate legal moves for the pinned piece would go here
        # For now, just return an empty list or placeholder
        return []





    #prevents the opposing player from moving
    def new_turn(self):
        player = self.current_player()


        if self.player1 == player:
            self.player1.set_turn(False)
            self.player2.set_turn(True)
            self.register_moves()
        else:
            self.player1.set_turn(True)
            self.player2.set_turn(False)
            self.register_moves()


    def is_eligible_move(self, piece, position):
        moves = self.moves
        if self.pinned_piece_moves(piece):
            return False



        if self.is_check():
            moves_out_of_check = self.moves_out_of_check()
            for key, value in moves_out_of_check.items():
                if piece not in self.current_player().get_pieces().values():
                    return False
                if piece.getPieceName() in key and position in value:
                    return True
        else:

            for key, value in moves.items():
                if piece not in self.current_player().get_pieces().values():
                    return False
                if piece.getPieceName() in key and position in value:
                    return True
        return False






    #made this into a function since i have to copy this over for two game modes
    def defulalt_layout(self):
        white_pawn1 = Pawn("player_1", "a2")
        white_pawn2 = Pawn("player_1", "b2")
        white_pawn3 = Pawn("player_1", "c2")
        white_pawn4 = Pawn("player_1", "d2")
        white_pawn5 = Pawn("player_1", "e2")
        white_pawn6 = Pawn("player_1", "f2")
        white_pawn7 = Pawn("player_1", "h2")
        white_pawn8 = Pawn("player_1", "g2")
        white_rook_1 = Rook("player_1", "a1")
        white_rook_2 = Rook("player_1", "h1")
        white_queen_1 = Queen("player_1", "d1")
        white_king = King("player_1", "e1")
        white_bishop_1 = Bishop("player_1", "c1")
        white_bishop_2 = Bishop("player_1", "f1")
        white_knight_1 = Knight("player_1", "b1")
        white_knight_2 = Knight("player_1", "g1")
        p_pieces = [white_king, white_queen_1, white_rook_1, white_bishop_1, white_knight_1, white_bishop_2,
                    white_knight_2, white_rook_2, white_pawn1, white_pawn2, white_pawn3, white_pawn4, white_pawn5,
                    white_pawn6, white_pawn7, white_pawn8]
        self.player1.add_pieces(p_pieces)
        # player 2 pieces
        black_pawn1 = Pawn("player_2", "a7")
        black_pawn2 = Pawn("player_2", "b7")
        black_pawn3 = Pawn("player_2", "c7")
        black_pawn4 = Pawn("player_2", "d7")
        black_pawn5 = Pawn("player_2", "e7")
        black_pawn6 = Pawn("player_2", "f7")
        black_pawn7 = Pawn("player_2", "h7")
        black_pawn8 = Pawn("player_2", "g7")
        black_rook_1 = Rook("player_2", "a8")
        black_rook_2 = Rook("player_2", "h8")
        black_queen_1 = Queen("player_2", "d8")
        black_king = King("player_2", "e8")
        black_bishop_1 = Bishop("player_2", "c8")
        black_bishop_2 = Bishop("player_2", "f8")
        black_knight_1 = Knight("player_2", "b8")
        black_knight_2 = Knight("player_2", "g8")
        p2_piece = [black_pawn1, black_pawn2, black_pawn3, black_pawn4, black_pawn5, black_pawn6, black_pawn7,
                    black_pawn8, black_king, black_knight_2, black_knight_1, black_rook_1, black_rook_2, black_queen_1,
                    black_bishop_2, black_bishop_1]
        self.player2.add_pieces(p2_piece)
        p = p_pieces + p2_piece
        for piece in p:
            self.board.setPiecePosition(piece.getPieceName(), piece.getPosition())

    #TODO: retire player settings
    def free_style_mode(self):
        #init player
        self.player1.set_player_id("player_1")
        self.player2.set_player_id("player_2")
        self.player1.set_turn(True)
        self.player2.set_turn(False)
        self.defulalt_layout()




    #TODO: i still have to do other prerequisites to finish this
    # google gem response handling method, prompt and user chosen opening
    def player_vs_ai(self, player1, player2):
        self.player1.set_player_id("player_1")
        self.player2.set_player_id("player_2")
        self.player1.set_turn(True)
        self.player2.set_turn(False)
        self.defulalt_layout()

    def puzzle(self):
        pass



