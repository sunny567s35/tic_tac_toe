
import pygame, sys
 
 #initializing the pygame library
 
pygame.init()

width, height = 900, 900
 
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe!")

BOARD = pygame.image.load("assets/Board.png")
x_img = pygame.image.load("assets/X.png")
o_img = pygame.image.load("assets/O.png")

back_ground_color = (214, 201, 227)

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
graphical_board = [[[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]]]

to_move = 'X'

#
screen.fill(back_ground_color)
screen.blit(BOARD, (64, 64))

pygame.display.update()

def renderBoard(board, ximg, oimg):
    global graphical_board
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                # Create an X image and rect
                graphical_board[i][j][0] = ximg
                graphical_board[i][j][1] = ximg.get_rect(center=(j*300+150, i*300+150))
            elif board[i][j] == 'O':
                graphical_board[i][j][0] = oimg
                graphical_board[i][j][1] = oimg.get_rect(center=(j*300+150, i*300+150))

def add_XO(board, graphical_board, to_move):
    current_pos = pygame.mouse.get_pos()
    converted_x = (current_pos[0]-65)/835*2
    converted_y = current_pos[1]/835*2
    if board[round(converted_y)][round(converted_x)] != 'O' and board[round(converted_y)][round(converted_x)] != 'X':
        board[round(converted_y)][round(converted_x)] = to_move
        if to_move == 'O':
            to_move = 'X'
        else:
            to_move = 'O'
    
    renderBoard(board, x_img, o_img)

    for i in range(3):
        for j in range(3):
            if graphical_board[i][j][0] is not None:
                screen.blit(graphical_board[i][j][0], graphical_board[i][j][1])
    
    return board, to_move

gameFinished = False

def checkWin(board):
    winner = None
    for row in range(0, 3):
        if((board[row][0] == board[row][1] == board[row][2]) and (board [row][0] is not None)):
            winner = board[row][0]
            for i in range(0, 3):
                graphical_board[row][i][0] = pygame.image.load(f"assets/Winning {winner}.png")
                
                screen.blit(graphical_board[row][i][0], graphical_board[row][i][1])
            pygame.display.update()
            return winner

    for col in range(0, 3):
        if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner =  board[0][col]
            for i in range(0, 3):
                graphical_board[i][col][0] = pygame.image.load(f"assets/Winning {winner}.png")
                screen.blit(graphical_board[i][col][0], graphical_board[i][col][1])
            pygame.display.update()
            return winner
   
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        winner =  board[0][0]
        graphical_board[0][0][0] = pygame.image.load(f"assets/Winning {winner}.png")
        screen.blit(graphical_board[0][0][0], graphical_board[0][0][1])
        graphical_board[1][1][0] = pygame.image.load(f"assets/Winning {winner}.png")
        screen.blit(graphical_board[1][1][0], graphical_board[1][1][1])
        graphical_board[2][2][0] = pygame.image.load(f"assets/Winning {winner}.png")
        screen.blit(graphical_board[2][2][0], graphical_board[2][2][1])
        pygame.display.update()
        return winner
          
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        winner =  board[0][2]
        graphical_board[0][2][0] = pygame.image.load(f"assets/Winning {winner}.png")
        screen.blit(graphical_board[0][2][0], graphical_board[0][2][1])
        graphical_board[1][1][0] = pygame.image.load(f"assets/Winning {winner}.png")
        screen.blit(graphical_board[1][1][0], graphical_board[1][1][1])
        graphical_board[2][0][0] = pygame.image.load(f"assets/Winning {winner}.png")
        screen.blit(graphical_board[2][0][0], graphical_board[2][0][1])
        pygame.display.update()
        return winner
    
    if winner is None:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != 'X' and board[i][j] != 'O':
                    return None
        return "DRAW"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            board, to_move = add_XO(board, graphical_board, to_move)

            if gameFinished:
                board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                graphical_board = [[[None, None], [None, None], [None, None]], 
                                    [[None, None], [None, None], [None, None]], 
                                    [[None, None], [None, None], [None, None]]]

                to_move = 'X'

                screen.fill(back_ground_color)
                screen.blit(BOARD, (64, 64))

                gameFinished = False

                pygame.display.update()
            
            if checkWin(board) is not None:
                gameFinished = True
            
            pygame.display.update()
