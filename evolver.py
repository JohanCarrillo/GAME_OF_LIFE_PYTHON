from random import randint
from typing import List
from cell import Cell, EState
from board import Board

class Evolver:
    """This class is in charge of all the evolving functions of the system
    """
    def __init__(self):
        pass

    def evolve(self, old_board: Board) -> Board:
        """_summary_

        Args:
            old_board (Board): board of the last time step, used to calculate the 
                new the board

        Returns:
            Board: new board of the current time step
        """
        new_board = Board(old_board.width, old_board.height)

        for y in range(old_board.height):
            for x in range(old_board.width):
                try:
                    old_cell = old_board.get_element(x, y)
                    neighbors: List[Cell] = self.get_cell_neighbors(old_board, x, y)
                    new_cell_state: EState = old_cell.calculate_state(neighbors)
                    new_cell = Cell(new_cell_state, x, y)
                    new_board.set_element(x, y, new_cell)
                except Exception as err:
                    print(err)
                pass

    def get_init_cell_state(self, pos_x: int, pox_y: int) -> EState:
        """Here is declared the function that initializes the cell state
        TODO: use different distriution to initialize the cell state

        Args:
            pos_x (int): cell row
            pos_y (int): cell column

        Returns:
            EState: initial state of the cell
        """
        n = randint(0, 1)
        return EState.DEAD if n == 0 else EState.ALIVE

    def init_board(self, width: int, height: int) -> Board:
        board = Board(width, height)
        for y in range(height):
            for x in range(width):
                initial_state = self.get_init_cell_state(x, y)
                cell = Cell(initial_state, x, y)
                board.set_element(x, y, cell)

    def get_cell_neighbors(self, board: Board, pos_x: int, pos_y: int) -> list[Cell]:
        """Method that defines the neighbors of a cell

        Args:
            cell (Cell): cell to calculate its neighbors

        Returns:
            list[Cell]: list with the neighbors of the cell
        """        
        if (board.get_element(pos_x, pos_y)):
            neighbors = []
            for dy in [-1, 1]:
                for dx in [-1, 1]:
                    neighbor = board.get_element(pos_x + dx, pos_y + dy)
                    if (neighbor):
                        neighbors.append(neighbor)
            return neighbors
        else:
            raise ValueError("Error finding neighbors of empty cell")

if __name__ == "__main__":
    evolver = Evolver()
    evolver.init_board(10, 10)
