import time
import sys

# 棋盘状态：黑棋, 白棋, 空棋
BLACK, WHITE, EMPTY = -1, 1, 0


if "idlelib" in sys.modules:
    BLACK_PIECE = " ● "
    WHITE_PIECE = " ○ "
    EMPTY_PIECE = " □ "
    END_ROW = " "
else:
    # 使用Emoji表示棋盘， BG_EMPTY设置背景色为绿色， BG_RESET是重置背景色
    BG_EMPTY, BG_RESET = "\x1b[42m", "\x1b[0m"
    BLACK_PIECE = f"{BG_EMPTY}⚫️{BG_RESET}"
    EMPTY_PIECE = f"{BG_EMPTY}🟩{BG_RESET}"
    WHITE_PIECE = f"{BG_EMPTY}⚪️{BG_RESET}"
    END_ROW = f"{BG_EMPTY} {BG_RESET}"


def stone(piece):
    """
    棋子的Emoji显示
    参数: 棋子类型(piece): -1, 0, 1, 对应黑棋、空棋、白棋
    """
    stone_coes = [
        BLACK_PIECE,
        EMPTY_PIECE,
        WHITE_PIECE,
    ]
    return stone_coes[piece + 1]


def init_board(n=8):
    """
    创建棋盘并设置初始的4枚棋子
    参数: 棋盘规格(n)
    """
    board = [[0 for _ in range(n)] for _ in range(n)]

    C0, C1 = n // 2, n // 2 - 1
    board[C0][C0], board[C1][C1] = WHITE, WHITE  # White
    board[C1][C0], board[C0][C1] = BLACK, BLACK  # Black

    return board


def display_board(board, sleep=0):
    """
    显示棋盘状态
    参数: 棋盘(board), 暂停时间(sleep)
    """
    for i, row in enumerate(board):
        for piece in row:
            print(stone(piece), end="")
        print(END_ROW, end="")
        print()  # New line after each row
    if sleep > 0:
        time.sleep(sleep)


def move_input(board, piece, name):
    """
    返回玩家下一手的位置(row, col)。
    参数: 棋盘(board), 棋子类型(piece), 玩家名称(name)
    """


def move_one_step(player, board):
    """
    玩家在棋盘上走一步。
    参数：玩家和棋盘
    """


def game(player1, player2, n=8):
    """
    游戏入口函数。
    参数: 两个玩家, 其中player1执黑, player2执白.
    """


def create_player(name, move):
    """
    创建玩家
    参数: 玩家名称(name), 玩家使用的选择下一步位置的函数(move)
    """
    return {
        "name": name,
        "move": move,
        "piece": None,
    }


def test_board():
    board = init_board()
    display_board(board)


if __name__ == "__main__":
    test_board()
