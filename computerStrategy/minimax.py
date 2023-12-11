import pygame
from copy import deepcopy
from checkers.constants import RED, WHITE

def minimaxAlgorithim(depth, pos, game, maximize):
    if depth == 0 or pos.winner() != None:
        return pos.evalBoard(), pos
    
    if (maximize):
        evaluateMax = float('-inf')
        bestMove = None
        for move in getMoves(game, pos, WHITE):
            eval_node = minimaxAlgorithim(depth-1, move, game, False)[0]
            evaluateMax = max(evaluateMax, eval_node)
            if evaluateMax == eval_node:
                bestMove = move
        return evaluateMax, bestMove
    else:
        evaluateMin = float('inf')
        bestMove = None
        for move in getMoves(game, pos, RED):
            eval_node = minimaxAlgorithim(depth-1, move, game, True)[0]
            evaluateMax = min(evaluateMin, eval_node)
            if evaluateMin == eval_node:
                bestMove = move
        return evaluateMin, bestMove
    
def simulateMove(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip: 
        board.remove(skip)
    return board

def getMoves(game, board, color):
    moves = []
    for piece in board.getPeicesForColor(color):
        possibleMoves = board.get_valid_moves(piece) #returns dict (row, col) : peices
        for move, skipMove in possibleMoves.items():
            boardTemp = deepcopy(board)
            pieceTemp = boardTemp.get_piece(piece.row, piece.col)
            boardNew = simulateMove(pieceTemp, move, boardTemp, game, skipMove)
            moves.append(boardNew)
    return moves
            