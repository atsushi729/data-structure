from dataclasses import dataclass
from enum import Enum


class Symbol(Enum):
    X = "X"
    O = "O"


class GameStatus(Enum):
    IN_PROGRESS = "in_progress"
    WON = "won"
    DRAW = "draw"


@dataclass(frozen=True)
class Player:
    name: str
    symbol: Symbol


class Board:
    def __init__(self):
        self._size = 3
        self._grid: list[list[Symbol | None]] = [
            [None] * self._size
            for _ in range(self._size)
        ]

    def place(
            self, row: int, col: int, symbol: Symbol
    ) -> None:
        if not (
                0 <= row < self._size
                and 0 <= col < self._size
        ):
            raise ValueError("Invalid position")

        if self._grid[row][col] is not None:
            raise ValueError("Position already occupied")

        self._grid[row][col] = symbol

    def has_winner(self, symbol: Symbol) -> bool:
        lines = [
            *self._grid,
            *zip(*self._grid),
            [
                self._grid[i][i]
                for i in range(self._size)
            ],
            [
                self._grid[i][self._size - 1 - i]
                for i in range(self._size)
            ],
        ]

        return any(
            all(cell == symbol for cell in line)
            for line in lines
        )

    def is_full(self) -> bool:
        return all(
            cell is not None
            for row in self._grid
            for cell in row
        )

    def display(self) -> str:
        return "\n---------\n".join(
            " | ".join(
                cell.value if cell is not None else " "
                for cell in row
            )
            for row in self._grid
        )


class Game:
    def __init__(self, player1: Player, player2: Player):
        if player1.symbol == player2.symbol:
            raise ValueError("Players must use different symbols")

        self._board = Board()
        self._players = (player1, player2)
        self._current_index = 0
        self._status = GameStatus.IN_PROGRESS
        self._winner: Player | None = None

    @property
    def current_player(self) -> Player:
        return self._players[self._current_index]

    @property
    def status(self) -> GameStatus:
        return self._status

    @property
    def winner(self) -> Player | None:
        return self._winner

    def play(self, row: int, col: int) -> None:
        if self._status != GameStatus.IN_PROGRESS:
            raise ValueError("Game is already over")

        player = self.current_player

        self._board.place(row, col, player.symbol)

        if self._board.has_winner(player.symbol):
            self._status = GameStatus.WON
            self._winner = player

        elif self._board.is_full():
            self._status = GameStatus.DRAW

        else:
            self._switch_turn()

    def _switch_turn(self) -> None:
        self._current_index = 1 - self._current_index

    def display_board(self) -> str:
        return self._board.display()


def main():
    player1 = Player("Player 1", Symbol.X)
    player2 = Player("Player 2", Symbol.O)

    game = Game(player1, player2)

    while game.status == GameStatus.IN_PROGRESS:
        print()
        print(game.display_board())
        print(f"\n{game.current_player.name}'s turn")

        try:
            row, col = map(
                int,
                input("Enter row and col (1-3): ").split()
            )

            game.play(row - 1, col - 1)

        except ValueError as error:
            print(error)

    print()
    print(game.display_board())

    if game.winner is not None:
        print(f"{game.winner.name} wins!")
    else:
        print("Draw!")


if __name__ == "__main__":
    main()
