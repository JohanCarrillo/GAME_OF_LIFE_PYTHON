class Board:
    def __init__(self, width: int, height: int):
        self._width, self._height = (width, height)
        self._collection = [[None for i in range(width)] for j in range(height)]

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def get_element(self, pos_x: int, pos_y: int):
        if (pos_x < 0 or pos_x >= self._width or pos_y < 0 or pos_y >= self._height):
            return None
        else:
            return self._collection[pos_y][pos_x]

    def set_element(self, pos_x: int, pos_y: int, item):
        if (pos_x < 0 or pos_x >= self._width):
            raise ValueError("Position x out of bounds")
        if (pos_y < 0 or pos_y >= self._height):
            raise ValueError("Position y out of bounds")
        else:
            self._collection[pos_y][pos_x] = item

    def __str__(self):
        str_collection = [
            [str(self._collection[i][j]) for i in range(self._width)]
            for j in range(self._height)
        ]
        return str(str_collection)

if __name__ == "__main__":
    board = Board(10, 10)
    print(board)
