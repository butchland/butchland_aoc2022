__all__ = ["match_value", "score", "find_strat_piece", "score_strat_action"]

opp_code = dict(A="Rock", B="Paper", C="Scissors")
your_code = dict(X="Rock", Y="Paper", Z="Scissors")
piece_value = dict(Rock=1, Paper=2, Scissors=3)
unmatched_values = {
    ("Rock", "Scissors"): 6,
    ("Rock", "Paper"): 0,
    ("Paper", "Scissors"): 0,
    ("Paper", "Rock"): 6,
    ("Scissors", "Rock"): 0,
    ("Scissors", "Paper"): 6,
}

strat_values = dict(X="LOSE", Y="DRAW", Z="WIN")


def match_value(
    your_piece: str,  # your piece (Rock/Paper/Scissors)
    opp_piece: str,  # opponent's piece (Rock/Paper/Scissors)
) -> int:
    """Returns the value of the match between your piece and the opponent's
    piece - if equal, returns 3, else if you win then return 6 else return 0"""
    if your_piece == opp_piece:
        return 3
    return unmatched_values[(your_piece, opp_piece)]  # type: ignore


def score(
    input: str,  # a string containing your opponent's and your move separated by a space
) -> int:
    """Returns the score of each move by you and your opponent
    based on the combination of the match value plus the piece value.

    Your opponent's and your move (Rock,Paper,Scissors) which are
    encoded A,B,C and by X,Y,Z respectively.
    """
    opp_move, your_move = input.strip().split(" ")
    opp_piece = opp_code[opp_move]
    your_piece = your_code[your_move]
    result = match_value(your_piece, opp_piece) + piece_value[your_piece]
    return result


win_strategy = dict(Rock="Paper", Paper="Scissors", Scissors="Rock")

lose_strategy = dict(Rock="Scissors", Paper="Rock", Scissors="Paper")


def find_strat_piece(
    opp_piece: str,  # your opponents piece (Rock, Paper,Scissors)
    your_strat: str,  # your strategy (WIN,LOSE, DRAW)
) -> str:
    """Finds the piece that matches the strategy you picked given the opponent's piece
    """
    if your_strat == "DRAW":
        return opp_piece
    elif your_strat == "WIN":
        return win_strategy[opp_piece]
    # LOSE
    return lose_strategy[opp_piece]


def score_strat_action(
        input:str, # a string containing your opponent's move and your strategy separated by a space
    ) -> int :
    """Returns the score given the opponents move and your strategy
    """
    opp_move, your_move = input.strip().split(" ")
    opp_piece = opp_code[opp_move]
    your_strat = strat_values[your_move]
    your_piece = find_strat_piece(opp_piece, your_strat)
    result = match_value(your_piece, opp_piece) + piece_value[your_piece]
    return result
