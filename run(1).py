from othellolib import test_board

#from othellolib import game, create_player
#from othellolib import move_input, move_AI, move_first, move_eager


def main():
    player1 = create_player('🐁  张峰', move_AI)
    player2 = create_player('🐁  李伟', move_random)
    game(player1=player1, player2=player2)


if __name__ == "__main__":
    test_board()
