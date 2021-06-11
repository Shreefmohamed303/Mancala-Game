from rich.table import Table
from rich.console import Console

#EASY, MODERATE, DIFFICULT = 1, 2, 3

class Board:
    def __init__(self):
        self.PITS = 6
        self.TOTAL_PITS = 12
        self.BOARD_SIZE = 14
        self.PLAYER1 = 0
        self.PLAYER2 = 1
        self.mancala_board = [4, 4, 4, 4, 4, 4, 0,
                              4, 4, 4, 4, 4, 4, 0]

    def getLimit(self,player):
        return(self.PITS + 1) * player
    
    def evaluation(self, player):
        limit1 = self.getLimit(player)
        limit2 = self.getLimit(1-player)

        # Calculate the differece between stores
        evaluation1 = self.mancala_board[self.PITS + limit1] - self.mancala_board[self.PITS + limit2]

        evaluation2 = 0

        for i in range(self.PITS):
            evaluation2 = evaluation2 + abs((int((not (not self.mancala_board[i + limit1]))) - int((not (not self.mancala_board[i + limit2])))))

        result = evaluation1 + evaluation2

        return result


    # return a list of indeces of non empty pits
    def getFilledPitsIndex(self, player):
        moves = []
        limit = 7 * player
        for i in range(6):
            if(self.mancala_board[i+limit]):
                moves.append(i)
        return moves

    # Actual Move of Stones
    def Move(self, move, player,mode):
        limit = self.getLimit(player) #0
        move_index = move + limit
        stones = self.mancala_board[move_index]
        self.mancala_board[move_index] = 0

        opponent_store = self.TOTAL_PITS + 1 - limit #compute index of opponent store
        while (stones):
            move_index = (move_index + 1) % self.BOARD_SIZE

            if (move_index == opponent_store): #rule game
                continue
            self.mancala_board[move_index] = self.mancala_board[move_index] + 1
            stones = stones - 1

        # Check if last stone landed in player's store
        # In this case the player gets another turn
        if (move_index == self.PITS + limit):
            return True
        if(mode):
            # Stealing Condition Satsified
            # Check if last stone landed in player's empty bin and opposite player's bin has at least one stone
            # In this case all the stones in the opponent's bins go to the player's store
            if (move_index < (self.PITS + limit) and move_index >= limit and self.mancala_board[move_index] == 1 and self.mancala_board[self.TOTAL_PITS - move_index] > 0):
                # Collect stones from player's pit and opponent's pit and put them in player's store
                self.mancala_board[self.PITS + limit] = self.mancala_board[self.PITS +limit] + (self.mancala_board[self.TOTAL_PITS - move_index] + 1)
                # empty player's pit and opponent's pit
                self.mancala_board[self.TOTAL_PITS - move_index] = self.mancala_board[move_index] = 0
        return False


    def getScore(self, expectedPlayer):
        limit = self.getLimit(expectedPlayer)
        for i in range(self.PITS):
            self.mancala_board[limit + 6] = self.mancala_board[limit + 6] + self.mancala_board[i + limit]

        diff = self.mancala_board[6] - self.mancala_board[13]
        if (diff < 0):
            return abs(diff), 1 #LOSE
        elif (diff > 0):
            return abs(diff), 0 #WIN
        else:
            return abs(diff), 2 #DRAW

    # The game is over when one player’s pits are completely empty.
    def isGameOver(self):
        if (any(self.mancala_board[0:6]) != 0 and any(self.mancala_board[7:13]) != 0):
            return False
        return True

    def print_board(self):
        table = Table()

        table.add_column("Computer Store")
        table.add_column("Pit-1")
        table.add_column("Pit-2")
        table.add_column("Pit-3")
        table.add_column("Pit-4")
        table.add_column("Pit-5")
        table.add_column("Pit-6")
        table.add_column("Human Store")
        table.add_column("Player")


        table.add_row("", str(self.mancala_board[12]), str(self.mancala_board[11]),str(self.mancala_board[10]),str(self.mancala_board[9]), 
                        str(self.mancala_board[8]), str(self.mancala_board[7]), "", "Computer")

        table.add_row( str(self.mancala_board[13]),"", "", "", "", "", "", str(self.mancala_board[6]))

        table.add_row("", str(self.mancala_board[0]), str(self.mancala_board[1]), str(self.mancala_board[2]), str(self.mancala_board[3]),
                        str(self.mancala_board[4]), str(self.mancala_board[5]), "", "Human")

        console = Console()
        console.print(table)





