
class Board():
    def __init__(self, l):
        self.NUM2OX = {1:'o',0:'_',-1:'x'}
        self.OX2NUM = {'o':1,'_':0,'x':-1}

        self.board = [0]*l
        for i in range(len(self.board)):
            self.board[i] = [0]*l

        self.hand = 1

    def get_hand(self):
        return self.hand

    def reverse_hand(self):
        self.hand = -self.hand 
    
    def update_board(self, x, y):
        self.board[y][x] = self.hand

    def check_hand(self, x, y):
        if self.board[y][x] == 0:
            return True
        else:
            return False
        
    def num2ox(self, num):
        return self.NUM2OX[num]

    def print_board(self):
        for y in range(len(self.board)):
            for x in range(len(self.board)):
                print(f'{self.num2ox(self.board[y][x])} ', end='')
            print()

    def check_game_end(self):
        for y in range(len(self.board)):
            if len(set(self.board[y])) == 1 and 0 not in set(self.board[y]):
                return True

        for x in range(len(self.board)):
            xy = set([self.board[y][x] for y in range(len(self.board))])
            if len(xy) == 1 and 0 not in xy:
                return True
            
        c1l=[0]*len(self.board)
        c2l=[0]*len(self.board)
        for i, y in enumerate(range(len(self.board))):
            c1l[i] = self.board[y][i]
            c2l[i] = self.board[y][len(self.board) - 1 - i]
        if len(set(c1l)) == 1 and 0 not in set(c1l):
            return True
        if len(set(c2l)) == 1 and 0 not in set(c2l):
            return True
        
        else:
            return False

    # def num2ox(num):
    #     #Enum
    #     pass

b = Board(3)
while True:
    b.print_board()

    print(f'now, {b.num2ox(b.get_hand())}s turn')
    while True:
        x, y = map(int, input('input x y:').split())
        x -= 1
        y -= 1

        if b.check_hand(x,y):
            break
        else:
            print('error')
    b.update_board(x, y)

    if b.check_game_end():
        break
    b.reverse_hand()



