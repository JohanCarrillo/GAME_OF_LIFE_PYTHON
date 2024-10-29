from classes.cell import Cell
from classes.cell_state import EState


def test_cell_initialization():
    cell = Cell(EState.ALIVE, 1, 2)
    assert cell.state == EState.ALIVE
    assert cell.pos_x == 1
    assert cell.pos_y == 2


def test_cell_state_setter():
    cell = Cell(EState.ALIVE, 1, 2)
    cell.state = EState.DEAD
    assert cell.state == EState.DEAD


def test_cell_calculate_state():
    # Setup
    alive_cell = Cell(EState.ALIVE, 1, 1)
    dead_cell = Cell(EState.DEAD, 0, 0)
    dead_cell1 = Cell(EState.DEAD, 0, 0)
    alive_cell1 = Cell(EState.ALIVE, 0, 1)
    alive_cell2 = Cell(EState.ALIVE, 0, 2)
    alive_cell3 = Cell(EState.ALIVE, 1, 0)
    alive_cell4 = Cell(EState.ALIVE, 1, 2)

    # Test underpopulation (fewer than 2 live neighbors)
    alive_cell1.calculate_state(dead_cell, dead_cell, dead_cell, dead_cell)
    assert alive_cell1.state == EState.DEAD, "Cell should die from underpopulation"

    # Test survival (2 or 3 live neighbors)
    alive_cell2.calculate_state(alive_cell, alive_cell, dead_cell, dead_cell)
    assert alive_cell2.state == EState.ALIVE, "Cell should survive with 2 live neighbors"

    # Test overpopulation (more than 3 live neighbors)
    alive_cell3.calculate_state(alive_cell, alive_cell, alive_cell, alive_cell)
    assert alive_cell3.state == EState.DEAD, "Cell should die from overpopulation"

    # Test reproduction (exactly 3 live neighbors)
    dead_cell1.calculate_state(alive_cell, alive_cell, alive_cell, dead_cell)
    assert dead_cell1.state == EState.ALIVE, "Dead cell should come alive with exactly 3 live neighbors"