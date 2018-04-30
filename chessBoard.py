class chessBoard:
    def __init__(self):
        self.board = [['.']*8 for x in range(8)]

    def move(self, piece, y, x):
        self.board[piece.x][piece.y] = '.'
        self.board[x][y] = piece.symboll

        piece.x = x
        piece.y = y

    def checkIfPieceOnPos(self, y, x, piece):
        if self.board[x][y] == '.':
            print("This has a dot on this coords: {} {}".format(x,y))
            return True
        if not self.board[x][y] == '.':
            print("Yes there is a piece here it is {}".format(self.board[x][y]))
            print("x {}".format(y))
            print("y {}".format(x))
            return False
