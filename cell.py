from __future__ import annotations
from enum import IntEnum

class EState(IntEnum):
    DEAD = 0
    ALIVE = 1

class Cell:
    def __init__(self, state: EState, pos_x, pos_y) -> None:
        self._state = state
        self._position = (pos_x, pos_y)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state: EState):
        if(state in EState.__members__.values()):
            self._state = state

    @property
    def pos_x(self):
        return self._position[0]

    @property
    def pos_y(self):
        return self._position[1]

    def calculate_state(self, *neighbors: Cell) -> EState:
        """
        Current rules:
            - Any live cell with fewer than two live neighbors dies, as if 
                by underpopulation.
            - Any live cell with two or three live neighbors lives on to the 
                next generation.
            - Any live cell with more than three live neighbors dies, as if 
                by overpopulation.
            - Any dead cell with exactly three live neighbors becomes a live 
                cell, as if by reproduction.
        """
        alive_neighbors = 0
        for neighbor in neighbors:
            if (neighbor.state == EState.ALIVE):
                alive_neighbors += 1

        if (self._state == EState.ALIVE):
            if (alive_neighbors == 0 or alive_neighbors == 1):
                self._state = EState.DEAD
            elif (alive_neighbors == 2 or alive_neighbors == 3):
                self._state = EState.ALIVE
            else:
                self._state = EState.DEAD
        else:
            if (alive_neighbors == 3):
                self._state = EState.ALIVE

    def __str__(self):
        return str(self._state.value)