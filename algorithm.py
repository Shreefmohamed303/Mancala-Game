import copy
from board_state import Board


class Algorithm:
    def __init__(self):
        self.infinity = 300

    # Calculate Max Value
    def calcMaxValue(self, board_state, player, depth, alpha, beta,mode):

        # check if the game is over or not
        if (board_state.isGameOver()): 
            score, y = board_state.getScore(player) # get Score 
            return score
            
        # get estimated score    
        if (depth==0):
            return board_state.evaluation(player)
        
        #get indix of All Filled PITS 
        filled_pits = board_state.getFilledPitsIndex(player) 

        maxValue = -self.infinity   # temp alpha initial value

        for pit_index in filled_pits:

            next_board_state = copy.deepcopy(board_state)

            # Make the actual Move 
            is_freeTurn = next_board_state.Move(pit_index, player,mode)

            if (is_freeTurn): 
                # Human --> Maximizer turn then calculate the MaxValue
                value = self.calcMaxValue(next_board_state, player, depth, alpha, beta,mode)
            else:
                # Opponent --> Minimizer turn then calculate the MinValue
                value = self.calcMinValue(next_board_state, player, depth - 1, alpha, beta,mode)

            # compare the maxValue with last claculated Value and get The Max
            maxValue = max(maxValue, value)

            # CuttOff Condition
            if (maxValue >= beta):
                return maxValue

            # Compare and Update Alpha with the New MaxValue
            alpha = max(alpha, maxValue)

        return maxValue

    # Calculate Min Value
    def calcMinValue(self, board_state, player, depth, alpha, beta,mode):

        # check if the game is over or not
        if (board_state.isGameOver()): 
            score, y = board_state.getScore(player) # get Score 
            return score
        # get estimated score    
        if (depth==0):
            return board_state.evaluation(player)

        opponent = 1 - player

        #get indix of All Filled PITS 
        filled_pits = board_state.getFilledPitsIndex(opponent)

        # temp Beta initial value
        minValue = self.infinity

        for pit_index in filled_pits:

            next_board_state = copy.deepcopy(board_state)

            # Make the actual Move 
            is_freeTurn = next_board_state.Move(pit_index, opponent,mode)
            if (is_freeTurn):
                # Opponent --> Minimizer turn then calculate the MinValue
                value = self.calcMinValue(next_board_state, player, depth, alpha, beta,mode)
            else:
                # Human --> Maximizer turn then calculate the MaxValue
                value = self.calcMaxValue(next_board_state, player, depth - 1, alpha, beta,mode)

            # Compare the minValue with last claculated Value and get The Min    
            minValue = min(minValue, value)

            # CuttOff Condition
            if (minValue <= alpha):
                return minValue

            # Compare and Update Beta with the New minValue
            beta = min(beta, minValue)

        return minValue

    # AlphaBeta algorithm
    def alphabetaAlgorithm(self, state, player, depth,mode):

        # get indix of All Filled PITS 
        filled_pits = state.getFilledPitsIndex(player)

        # Initialization of ALPHA , BETA 
        alpha = -self.infinity
        beta = self.infinity
        bestValue = -self.infinity

        for pit_index in filled_pits:

            next_state = copy.deepcopy(state)

            # Make the actual Move 
            is_freeTurn = next_state.Move(pit_index, player,mode)
            if (is_freeTurn):
                # Human --> Maximizer turn then calculate the MaxValue
                value = self.calcMaxValue(next_state, player, depth, alpha, beta,mode)
            else:
                # Opponent --> Minimizer turn then calculate the MinValue
                value = self.calcMinValue(next_state, player, depth - 1, alpha, beta,mode)
            
            # CuttOff Condition
            if (value > bestValue):
                bestValue = value
                pit_to_move = pit_index
            
            # Compare and Update Alpha with the New MaxValue
            alpha = max(alpha, value)
            
        return pit_to_move 