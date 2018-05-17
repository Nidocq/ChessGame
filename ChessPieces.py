from chessBoard import *

class Pawn:
    def __init__(self, chessboard, x, y, status):
        chessBoard.__init__(self)
        self.x = x # changed R_x to x
        self.y = y # changed R_y to y
        self.symboll = 'P'
        self.isWhite = status
        self.first = True
        chessboard[self.x][self.y] = self.symboll


    def verifyMove(self, startPosX, startPosY, endPosX, endPosY, piece, board, brick, listPieces):
        print("Moving piece {}".format(piece))
        print("startPosX, {}".format(startPosX))
        print("startPosY, {}".format(startPosY))
        print("endPosX, {}".format(endPosX))
        print("endPosY, {}".format(endPosY))
        print("self.x, {}".format(self.x))
        print("self.y, {}".format(self.y))
        print("Status of THIS piece is: {}".format(piece.returnStatus()))
        print("Starting on pos {} {} - Ending on pos {} {}".format(startPosX, startPosY, endPosX, endPosY))
        try:
            if self.first == True:
                self.first = False
                print("THIS IS FIRST TIME")
                if int(endPosY-piece.returnY() < 3) & int(endPosX-piece.returnX() == 0) == True:
                    if board.checkIfPieceOnPos(endPosX, endPosY, piece): #This is for checking not defining
                        print("There is no piece")
                        board.move(piece, endPosX, endPosY)
                        print("This moves ")
                    else:
                        print("There is a chessPiece here")
                        for _piece in listPieces:
                            print("Status of THE _PIECE is: {}".format(_piece.returnStatus()))
                            if piece.returnX() == _piece.returnX():
                                print("first x piece.returnX: {}, piece {}, x {}".format(_piece.returnX(), _piece, _piece.returnX()))
                                if piece.returnY() == _piece.returnY():
                                    print("second x piece.returnY: {}, piece {}, y {}".format(_piece.returnY(), _piece, _piece.returnY()))
                                    if not _piece.returnStatus() == piece.returnStatus(): # Maybe : _piece.returnStatus() == True & piece.returnStatus() == True
                                        print("Valid move!")
                                        board.move(piece, endPosX, endPosY)
                                    else:
                                        print("This is an invalid move. Same color")
                                        self.first = True

                else:
                    print("This is an invalid move, chesspiece can not move here")
                    self.first = True
            else:

                if int(endPosY-piece.returnY() < 2) & int(endPosX-piece.returnX() == 0) == True:
                    if board.checkIfPieceOnPos(endPosX, endPosY, piece): #This is for checking not defining
                        print("There is no piece")
                        board.move(piece, endPosX, endPosY)
                        print("This moves ")
                    else:
                        print("There is a chessPiece here")
                        for _piece in listPieces:
                            print("Status of THE _PIECE is: {}".format(_piece.returnStatus()))
                            if piece.returnX() == _piece.returnX():
                                print("first x piece.returnX: {}, piece {}, x {}".format(_piece.returnX(), _piece, _piece.returnX()))
                                if piece.returnY() == _piece.returnY():
                                    print("second x piece.returnY: {}, piece {}, y {}".format(_piece.returnY(), _piece, _piece.returnY()))
                                    if not _piece.returnStatus() == piece.returnStatus(): # Maybe : _piece.returnStatus() == True & piece.returnStatus() == True
                                        print("Valid move!")
                                        board.move(piece, endPosX, endPosY)
                                    else:
                                        print("This is an invalid move. Same color")
                else:
                    print("Invalid step")
        except IndexError:
            print("This tile does not exist")

    def returnStatus(self):
        return self.isWhite

    def returnY(self):
        return self.x

    def returnX(self):
        return self.y

class Rook:
    def __init__(self, chessboard, x, y, status):
        chessBoard.__init__(self)
        self.x = x # changed R_x to x
        self.y = y # changed R_y to y
        self.symboll = 'R'
        self.Iswhite = status
        chessboard[self.x][self.y] = self.symboll

    def verifyMove(self, startPosX, startPosY, endPosX, endPosY, piece, board, brick, listPieces):
        try:
            if piece.returnX() == endPosX: # Is the axis the same, if so, we know that is moving in one direction
                if board.checkIfPieceOnPos(endPosX, endPosY, piece): #Checking if there is a piece on the desired position
                    print("There are no piece here")
                    board.move(piece, endPosX, endPosY)
                else:
                    print("There is a piece here")
                    print("Starting loop")
                    for _piece in listPieces: # We will go through the whole
                        if _piece.returnX() == endPosX: #This will look for all the pieces on THE Y AXIS. YES
                            print("The symbol of the piece on the Y axis is: {}".format(_piece.symboll))

                            if _piece.returnY() == endPosY:
                                print("The desired position")

                                if not _piece.returnStatus() == piece.returnStatus():
                                    print("Valid move!")
                                    board.move(piece, endPosX, endPosY)
                                else:
                                    print("This is an invalid move. Same color")


            elif piece.returnY() == endPosY: # Is the axis the same, if so, we know that is moving in one direction
                if board.checkIfPieceOnPos(endPosX, endPosY, piece): #Checking if there is a piece on the desired position
                    print("There are no piece here")
                    board.move(piece, endPosX, endPosY)
                else:
                    print("There is a piece here")
                    print("Starting loop")
                    for _piece in listPieces: # We will go through the whole
                        if _piece.returnY() == endPosY: #This will look for all the pieces on THE X AXIS. YES
                            print("The symbol of the piece on the x axis is: {}".format(_piece.symboll))
                            print("The desired position")

                            if _piece.returnX() == endPosX:
                                print("The desired position")

                                if not _piece.returnStatus() == piece.returnStatus():
                                    print("Valid move!")
                                    board.move(piece, endPosX, endPosY)
                                else:
                                    print("This is an invalid move. Same color")

            else:
                print("This is not a valid move, You're cossing two axises")
        except IndexError:
            print("The tile you are moving to does not exist")

    def returnStatus(self):
        return self.Iswhite

    def returnY(self):
        return self.x

    def returnX(self):
        return self.y


class Knight:
    def __init__(self, chessboard, x, y, status):
        chessBoard.__init__(self)
        self.x = x # changed R_x to x
        self.y = y # changed R_y to y
        self.symboll = 'Kn'
        self.Iswhite = status
        chessboard[self.x][self.y] = self.symboll

    def verifyMove(self, startPosY, startPosX, endPosY, endPosX, piece, board, brick, listPieces):
        try:
            if (abs(endPosX - piece.returnX())) == abs(int(1)): # if the Knight moves 1 to the right.
                print("This is true for x")
                if (abs(endPosY - piece.returnY())) == abs(int(2)): # If the Knight moves 2 to up
                    print("This is true for y")
                    board.move(piece, endPosY, endPosX)
                else:
                    print("invalid move")
            else:
                print("Invalid move")


            if (abs(endPosX - piece.returnX())) == abs(int(2)): # if the knigt moves 2 to the left
                if (abs(endPosY - piece.returnY())) == abs(int(1)): # if the knigt moves 1 up
                    board.move(piece, endPosY, endPosX)
                else:
                    print("Invalid move")
            else:
                print("Invalid move")

        except IndexError:
            print("The tile you are moving to does not exist")

    def returnStatus(self):
        return self.Iswhite

    def returnY(self):
        return self.x

    def returnX(self):
        return self.y


class Bishop:
    def __init__(self, chessboard, x, y, status):
        chessBoard.__init__(self)
        self.x = x # changed R_x to x
        self.y = y # changed R_y to y
        self.symboll = 'B'
        self.Iswhite = status
        chessboard[self.x][self.y] = self.symboll

    def verifyMove(self, startPosY, startPosX, endPosY, endPosX, piece, board, brick, listPieces):
        try:
            if (abs(piece.returnX() - piece.returnY())) == (abs(endPosX - endPosY)):
                print("Now this is true")
                board.move(piece, endPosY, endPosX)
            else:
                print("Not a legal move")

        except IndexError:
            print("The tile you are moving to does not exist")

    def returnStatus(self):
        return self.Iswhite

    def returnY(self):
        return self.x

    def returnX(self):
        return self.y


class Queen:
    def __init__(self, chessboard, x, y, status):
        chessBoard.__init__(self)
        self.x = x # changed R_x to x
        self.y = y # changed R_y to y
        self.symboll = 'Q'
        self.Iswhite = status
        chessboard[self.x][self.y] = self.symboll

    def verifyMove(self, startPosY, startPosX, endPosY, endPosX, piece, board, brick, listPieces):
        try:
            if ((abs(piece.returnX() - piece.returnY())) == (abs(endPosX - endPosY)) or (piece.returnX() == endPosX)):
                print("Now this is true")
                board.move(piece, endPosY, endPosX)

            elif ((abs(piece.returnX() - piece.returnY())) == (abs(endPosX - endPosY)) or (piece.returnY() == endPosY)):
                print("Now this is true")
            else:
                print("Not a legal move")

        except IndexError:
            print("The tile you are moving to does not exist")

    def returnStatus(self):
        return self.Iswhite

    def returnY(self):
        return self.x

    def returnX(self):
        return self.y


class King:
    def __init__(self, chessboard, x, y, status):
        chessBoard.__init__(self)
        self.x = x # changed R_x to x
        self.y = y # changed R_y to y
        self.symboll = 'K'
        self.Iswhite = status
        chessboard[self.x][self.y] = self.symboll

    def verifyMove(self, startPosY, startPosX, endPosY, endPosX, piece, board):
        print("Starting on pos {} {} - Ending on pos {} {}".format(startPosX, startPosY, endPosX, endPosY))
        print("statement {} if {} - {} < 1 (result is {})".format(endPosY-self.y < 1, endPosY,self.y,endPosY-self.y))
        board.checkIfPieceOnPos(endPosX, endPosY)
        board.move(piece, endPosX, endPosY)

    def returnStatus(self):
        return self.Iswhite

    def returnY(self):
        return self.x

    def returnX(self):
        return self.y
