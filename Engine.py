from chessBoard import *
from ChessPieces import *

class Engine:
    def __init__(self):
        chessBoard.__init__(self)

    def showBoard():
        for i in range(8):
            print(thisChessBoard.board[i])

thisChessBoard = chessBoard()
brickFound = False
listPieces = []
# Pawns White                               Coords: P
listPieces.append(Pawn(thisChessBoard.board, 6, 0, "White"))
listPieces.append(Pawn(thisChessBoard.board, 6, 1, "White"))
listPieces.append(Pawn(thisChessBoard.board, 6, 2, "White"))
listPieces.append(Pawn(thisChessBoard.board, 6, 3, "White"))
listPieces.append(Pawn(thisChessBoard.board, 6, 4, "White"))
listPieces.append(Pawn(thisChessBoard.board, 6, 5, "White"))
listPieces.append(Pawn(thisChessBoard.board, 6, 6, "White"))
listPieces.append(Pawn(thisChessBoard.board, 6, 7, "White"))

# Pawns Black
listPieces.append(Pawn(thisChessBoard.board, 1, 0, "Black"))
listPieces.append(Pawn(thisChessBoard.board, 1, 1, "Black"))
listPieces.append(Pawn(thisChessBoard.board, 1, 2, "Black"))
listPieces.append(Pawn(thisChessBoard.board, 1, 3, "Black"))
listPieces.append(Pawn(thisChessBoard.board, 1, 4, "Black"))
listPieces.append(Pawn(thisChessBoard.board, 1, 5, "Black"))
listPieces.append(Pawn(thisChessBoard.board, 1, 6, "Black"))
listPieces.append(Pawn(thisChessBoard.board, 1, 7, "Black"))


# ROOKS                                     Coords: R
listPieces.append(Rook(thisChessBoard.board, 7, 0, "White"))
listPieces.append(Rook(thisChessBoard.board, 7, 7, "White"))
listPieces.append(Rook(thisChessBoard.board, 0, 0, "Black"))
listPieces.append(Rook(thisChessBoard.board, 0, 7, "Black"))

# Knights                                   Coords: Kn
listPieces.append(Knight(thisChessBoard.board, 7, 1, "White"))
listPieces.append(Knight(thisChessBoard.board, 7, 6, "White"))
listPieces.append(Knight(thisChessBoard.board, 0, 1, "Black"))
listPieces.append(Knight(thisChessBoard.board, 0, 6, "Black"))

# Bishops                                   Coords: B
listPieces.append(Bishop(thisChessBoard.board, 7, 2, "White"))
listPieces.append(Bishop(thisChessBoard.board, 7, 5, "White"))
listPieces.append(Bishop(thisChessBoard.board, 0, 2, "Black"))
listPieces.append(Bishop(thisChessBoard.board, 0, 5, "Black"))

# Queens                                    Coords: Q
listPieces.append(Queen(thisChessBoard.board, 7, 3, "White"))
listPieces.append(Queen(thisChessBoard.board, 0, 3, "Black"))

# Kings                                     Coords: K
listPieces.append(King(thisChessBoard.board, 7, 4, "White"))
listPieces.append(King(thisChessBoard.board, 0, 4, "Black"))

game = True
Engine.showBoard()
while game:

    answer = str(input('\nHvad skal dine koordinater være?')) # PD2D4
    #answer = "P1113"


    for piece in listPieces:
        if piece.returnX() == int(answer[1:2]):
            if piece.returnY() == int(answer[2:3]):
                if len(answer) == 6:
                    if piece.returnX() == int(answer[2:3]):
                        if piece.returnY() == int(answer[3:4]):
                            if piece.symboll == answer[0:2]:
                                piece.verifyMove(int(answer[2:3]), int(answer[3:4]), int(answer[4:5]), int(answer[5:6]), piece, thisChessBoard, str(answer[0:2]), listPieces)
                                Engine.showBoard()
                                brickFound = True
                                break
                            else:
                                print("The symbol does not match the piece")
                        else:
                            print("The posistion of Y does not match the ")
                if len(answer) == 5:
                    if piece.returnX() == int(answer[1:2]):
                        if piece.returnY() == int(answer[2:3]):
                            if piece.symboll == answer[0:1]:
                                piece.verifyMove(int(answer[1:2]), int(answer[2:3]), int(answer[3:4]), int(answer[4:5]), piece, thisChessBoard, str(answer[0:1]), listPieces)
                                Engine.showBoard()
                                brickFound = True
                                break
                            else:
                                print("")
                                print("The symbol does not match the piece")

    if not brickFound == True:
        print("")
        print("No piece found on that posistion")

# FÅ den til kun at output 'P'
# KnG1E2 Knight moves from G1 to E2
# PD2D4 Pawn moves from D2 to D4
# QF4C7 Queen moves from F4 to C7
