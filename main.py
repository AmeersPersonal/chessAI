import os


from events import *
import pygame
from gui import *
from ai.googleGemResponse import *
gui = GUI()


def game():
   running = True

   pygame.init()
   player1 = Player()
   player2 = Player()
   eventManager = EventManger(player1, player2)

   mode = gui.get_config_values("gamemode")
   if mode == "free-style":
      eventManager.free_style_mode()

   image_clicked = None
   x,y = (0, 0)
   mouse_held = False
   image_orginal_pos = None
   while running:
      eventManager.register_moves()
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
         #image clicked on
         if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            for i in Piece.pieceList:
               if i["rect"].collidepoint(mouse_pos):
                  image_clicked = i
                  mouse_held = True
                  image_orginal_pos= i["rect"].topleft
                  x = i["rect"].x - mouse_pos[0]
                  y = i["rect"].y - mouse_pos[1]

         if event.type == pygame.MOUSEMOTION and image_clicked is not None:

            pos = pygame.mouse.get_pos()
            coords = eventManager.board.coordinatesToPosition(pos[0] + x, pos[1] + y)
            image_clicked["rect"].topleft = pos

         if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and mouse_held and image_clicked is not None and image_orginal_pos is not None:

            pos = pygame.mouse.get_pos()
            coords = eventManager.board.coordinatesToPosition(pos[0] + x, pos[1] + y)
            image = image_clicked
            player = player1 if image["name"] in player1.get_pieces() else player2

            # print(eventManager.isEligibleMove(player.getSpeficPiece(image["name"]), coords))

            if not eventManager.is_eligible_move(player.getSpeficPiece(image["name"]), coords):

               image_clicked = None
               mouse_held = False
               image["rect"].topleft = image_orginal_pos
               continue

            mouse_held = False
            image_clicked = None



            piece = player.getSpeficPiece(image["name"])

            image["rect"].topleft = eventManager.board.positionToCoordinates(coords)

            square = eventManager.board.get_board().get(coords, " ")

            if square != " ":
               if eventManager.is_eligible_move(piece, coords):
                  image_clicked = None
                  mouse_held = False

               if square != image["name"]:

                  if square in eventManager. potenial_captures_piece:
                     for i, img, in enumerate(Piece.pieceList):
                        if img["name"] == square:
                           del Piece.pieceList[i]
                           break




            eventManager.board.get_board()[piece.getPosition()] = ' '
            eventManager.board.get_board()[coords] = piece.getPieceName()
            piece.setPosition(coords)
            eventManager.pawn_promotion_event(player, piece, "queen")


            print(eventManager.moves_out_of_check())
            
            eventManager.new_turn()













      eventManager.board.screen.fill('black')
      eventManager.board.draw_board(100)

      for i in Piece.pieceList:
         Board.screen.blit(i["img"], i["rect"])
      pygame.display.update()
      pygame.time.Clock().tick(60)

def main():

   gui.set_up_config()
   gui.start_up_gui()
   game()




if __name__ == '__main__':
   main()